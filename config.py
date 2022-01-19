import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

# MAIL_SERVER = os.environ.get('MAIL_SERVER')
# MAIL_PORT = os.environ.get('MAIL_PORT')
# MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
# MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
# MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
# MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
# RECIPIENTS = os.environ.get('RECIPIENTS')
