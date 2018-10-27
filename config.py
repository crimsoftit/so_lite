import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "\xd2x\xbb\x85q/"
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    # print(SQLALCHEMY_DATABASE_URI)


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
