import json
import os
from pathlib import Path
from typing import Union
import logging

import structlog


class CustomPrintLogger:
    def __init__(self, log_file: str) -> None:
        self.log_file = Path(log_file)
        if not os.path.exists(self.log_file):
            self.log_file.parent.mkdir(exist_ok=True, parents=True)
            with open(self.log_file, 'w') as f:
                ...

    def _dump(self, event_dict: dict):
        event_dict = str(event_dict)
        try:
            with open(self.log_file, encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            data = []
        data.append(event_dict)
        data: list
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

    def __call__(
        self, logger, name: str, event_dict
    ) -> Union[str, bytes]:
        self._dump(event_dict)
        return repr(event_dict)


def get_struct_logger(name: str, log_file):
    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            CustomPrintLogger(log_file)
        ],
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    )
    log = structlog.get_logger()
    log = log.bind(module=name)
    return log
