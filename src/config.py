import ast
from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    kafka_bootstrap_servers: list[str]
    kafka_topic: str
    kafka_host: str
    kafka_port: int

    clickhouse_host: str
    auth_servise: str

    class Config:
        @classmethod    
        def parse_env_var(cls, field_name: str, raw_val: str):
            if field_name == 'kafka_bootstrap_servers':
                return ast.literal_eval(raw_val)
    
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
