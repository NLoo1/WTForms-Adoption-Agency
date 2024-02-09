class Config:
    DB_USERNAME = 'N'
    DB_PASSWORD = ' '
    DB_NAME = 'pets'
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}"
    SECRET_KEY = 'abc123'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class TestConfig(Config):
    DB_USERNAME = 'N'
    DB_PASSWORD= ' '
    DB_NAME = 'pets_test'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}"
    SECRET_KEY = 'abc123'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False