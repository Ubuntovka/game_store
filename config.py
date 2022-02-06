import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()  # take environment variables from .env.


class Config:
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):
    ENV = "development"  # be default production
    DEBUG = True
    PSWRD_DB_SERVER = os.environ.get('PSWRD_DB_SERVER')
    MONGODB_DB = os.environ.get('MONGODB_DB')
    MONGODB_HOST = os.environ.get('MONGODB_HOST')
    MONGODB_PORT = int(os.environ.get('MONGODB_PORT'))
    MONGODB_URI = os.environ.get('MONGODB_URI')

