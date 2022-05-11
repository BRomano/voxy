import os
from dotenv import load_dotenv

basedir = os.getcwd()


def _str_to_bool(s):
    if s in ['True', 'true', '1', True]:
        return True
    elif s in ['False', 'false', '0', False]:
        return False
    else:
        raise ValueError


def _get_bool_env(key, default_value):
    return _str_to_bool(os.getenv(key, default_value))


def _get_arr_env(key, default_value='[]'):
    ret_value = os.getenv(key, default_value)
    return eval(ret_value)


class BaseConfig(object):
    def __init__(self):
        pass

    SECRET_KEY = os.getenv('SECRET_KEY') or 'SECRET_KEY'


class DevConfig(BaseConfig):
    def __init__(self):
        super(DevConfig, self).__init__()

    load_dotenv(os.path.join(basedir, '.env'))
    # Global COnfigurations
    DEBUG = _str_to_bool(os.getenv('DEBUG', False))
    APP_NAME = os.getenv("APP_NAME")
    APP_LONG_NAME = os.getenv('APP_LONG_NAME')
    # SERVER_NAME = os.getenv('SERVER_NAME', "localhost:5000")

    SECRET_KEY = os.getenv('SECRET_KEY') or 'SECRET_KEY'

    # Open API
    SWAGGER = {
        "title": "Interview voxy",
        "uiversion": 3,
    }

    # CORS
    CORS_SUPPORTS_ORIGIN = os.getenv('CORS_SUPPORTS_ORIGIN', '*')
