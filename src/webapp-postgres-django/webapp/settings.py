"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 3.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import environ
import sys
import os

# Read Env vars from ../.env
env = environ.Env()
environ.Env.read_env()

# Debug
##print(sys.path)                                       ## ['/opt/webapp-postgres-django', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/opt/webapp-postgres-django/env/lib/python3.6/site-packages']
sys.path.append('/opt/webapp-postgres-django/webapp')   ## FIXED
##print(sys.path)                                       ## ['/opt/webapp-postgres-django', '/opt/webapp-postgres-django/webapp', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/opt/webapp-postgres-django/env/lib/python3.6/site-packages']


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-4igz*4u!5_c9p1l9z$5=clv&@mq5l35bd25#a1%ok+$uskk^=c'
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'greetings',                                     ## ModuleNotFoundError: No module named 'greetings' -- ЭТО БЫЛО ПРАВИЛЬНО, НО ПУТЬ К МОДУЛЮ НЕ ИСКАЛСЯ (исправлено в settings.py)
    #'greetings.apps.GreetingsConfig',               ## ModuleNotFoundError: No module named 'greetings'
    #'webapp.greetings',                             ## django.core.exceptions.ImproperlyConfigured: Cannot import 'greetings'. Check that 'webapp.greetings.apps.GreetingsConfig.name' is correct.
    #'webapp.greetings.apps.GreetingsConfig',        ## django.core.exceptions.ImproperlyConfigured: Cannot import 'greetings'. Check that 'webapp.greetings.apps.GreetingsConfig.name' is correct
    #'Greetings',                                    ## ModuleNotFoundError: No module named 'Greetings'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [],
        #'DIRS': [BASE_DIR / 'templates'],
        #
        #--version1: personal "templates" folder for each app
        #'APP_DIRS': True,
        #'DIRS': [BASE_DIR / 'webapp'],
        #
        #--version2: personal "templates" folder for each app
        'APP_DIRS': False,
        'DIRS': [BASE_DIR / 'webapp', BASE_DIR / 'webapp/templates'],
        #
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

WSGI_APPLICATION = 'webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
#
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

# CUSTOM SETTINGS - PosgreSQL Database
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'vagrant',
#        'USER': 'vagrant',
#        'PASSWORD': 'vagrant@pass',
#        'HOST': '192.168.0.70', 
#        'PORT': '5432',
#    }
#}
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Apps static directories
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'webapp/bonus/static/'),
   os.path.join(BASE_DIR, 'webapp/greetings/static/')
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
