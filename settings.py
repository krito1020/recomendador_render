import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()  # Carga el archivo .env automáticamente

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = os.getenv('SECRET_KEY', 'clave_por_defecto_insegura')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '.onrender.com,localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.auth', 
    'django.contrib.contenttypes',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.messages',
    'apps.recomendador',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'apps/recomendador/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

DATABASE_URL = os.getenv('DATABASE_URL')

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'apps/recomendador/static'),
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')