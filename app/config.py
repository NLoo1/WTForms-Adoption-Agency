import os

class Config:
    os.environ['DB_USERNAME'] = 'N'
    os.environ['DB_PASSWORD'] = ' '
    os.environ['DB_NAME'] = 'pets'
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ['DB_USERNAME']}:{os.environ['DB_PASSWORD']}@localhost/{os.environ['DB_NAME']}"
    SECRET_KEY = 'abc123'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class TestConfig(Config):
    os.environ['DB_USERNAME'] = 'N'
    os.environ['DB_PASSWORD'] = ' '
    os.environ['DB_NAME'] = 'pets_test'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ['DB_USERNAME']}:{os.environ['DB_PASSWORD']}@localhost/{os.environ['DB_NAME']}"

    SECRET_KEY = 'abc123'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False