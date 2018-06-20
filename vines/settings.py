"""
Django settings for vines project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from os.path import dirname
from os.path import join
from decouple import config


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR = dirname(dirname(__file__))

#MEDIA_ROOT2 = (os.path.join(BASE_DIR, 'vinesF/static/vinef/Videos'))  
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['127.0.0.2','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'utils.apps.utilsConfig',
    'vinesF.apps.VinesfConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'hitcount',
    'simple_search',
    'crispy_forms',
    'bootstrap4',
    'bootstrap3',
    'el_pagination',
    'search',
    'storages',
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

ROOT_URLCONF = 'vines.urls'
LOGIN_URL = 'public_Signin'
LOGIN_REDIRECT_URL ='/'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                # "django.core.context_processors.static", #Added when fixing js 8-6-18
            ],
        },
    },
]

WSGI_APPLICATION = 'vines.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'DB_NAME'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# STATIC_URL = '/static/' #deactivated on 20-06-18: for amazon s3 purpose
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'vinesF/static'),
# ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
#STATIC_URL2 = '/static/vinef/'
#STATIC_URL2 =os.path.realpath('/static/vinef/Videos')

#Added this to for same template not found error
#TEMPLATE_DIRS = (
##)
# Hit Count setting
HITCOUNT_HITS_PER_IP_LIMIT = 0
HITCOUNT_KEEP_HIT_IN_DATABASE = { 'days': 30 }
CRISPY_TEMPLATE_PACK = 'bootstrap3'
BOOTSTRAP3 = {'include_jquery': True}
CRISPY_FAIL_SILENTLY = DEBUG


AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
AWS_STORAGE_BUCKET_NAME = 'vines-static'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'vinesF/static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_FILE_STORAGE = 'settings.storage_backends.MediaStorage'

#Activate this at code clean-up, version control and deployment stage as an easy alternative to conf
# try:
# execfile(os.path.join(
# os.path.dirname(__file__), "local_settings.py"
# ))
# except IOError:
# pass