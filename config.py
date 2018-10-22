import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "\xd2x\xbb\x85q/"
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]


class DevConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
