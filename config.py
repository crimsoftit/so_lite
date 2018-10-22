import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "yule_mguyz"
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]


class DevConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
