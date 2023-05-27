import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv("SECRET_KEY")



ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'unniku$db',
        'USER': 'unniku',
        'PASSWORD': os.getenv("MYSQL_PASSWORD"),
        'HOST':'unniku.mysql.pythonanywhere-services.com',
        'PORT':'3306',
    }
}