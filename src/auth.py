from fastapi import Cookie
import requests
from src.config import config

URL_SERVISE_AUTH = f'http://{config.auth_servise}//api/v1/users/verify_token'

def token_verification(func):
    def wrapper(access_token_cookie = Cookie(), refresh_token_cookie = Cookie()):
        cookies  = dict(access_token_cookie = access_token_cookie,
                        refresh_token_cookie = refresh_token_cookie)
        resp = requests.get(URL_SERVISE_AUTH, cookies=cookies)
        if not resp.json():
            return {'error':'Token expired'}
        return func()
    return wrapper