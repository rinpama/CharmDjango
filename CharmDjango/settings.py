"""
Django settings for CharmDjango project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
# from decouple import config, Csv
import environ
import dj_database_url
from pathlib import Path
import os
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env('.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# from .local_settings import SECRET_KEY######
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
env = environ.Env(DEBUG=(bool, False))
DEBUG = env('DEBUG')
# or
# env.environ.Env(DEBUG=(bool,False))
# DEBUG=env.get_value('DEBUG',cast=bool,default=False)

# config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
# ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
# Application definition
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO','https')
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'accounts',
    'm3ch',
    'Soen',
    'Show',
    'actualSpot',
    'reimex',

    'storages',
]

SUMMERNOTE_THEME = 'bs4'
X_FRAME_OPTOPNS = 'SAMEORIGIN'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CharmDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'CharmDjango.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASE_URL')
    )
}
db_from_env = dj_database_url.config()  # *
DATABASES['default'].update(db_from_env)  # *

# Honor the 'X-Forwarded-Proto' header for request.is_secure()

SECURE_PROXY_SSL_HEADER = env.list('SECURE_PROXY_SSL_HEADER')
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ja-JP'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# 開発環境では、プロジェクト直下や各アプリケーションごとに静的ファイルの置き場を作成してそれぞれを呼び出す。
# デプロイする際は、個別の静的ファイルをSTATIC_ROOTで指定した場所にcollectstaticで全て集める。
# その後、web serverにSTATIC_ROOT(static/)を見に行くようにSTATIC_URLで指定

## 開発時(DEBUG=True) #
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'asset'), ]  # 共通スタティックのディレクトリを指定(manage.py同列)。
#各app直下のstaticディレクトリから、 django.contrib.staticfilesを使い、runserver実行時に自動的に各staticﾌｧｲﾙを配信

# 本番環境(Debug=False)＝＞django.contrib.staticfilesがapp/staticファイルの配信を止めるので、collectstaticで1ヶ所に集める
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# ↓ AWS S3　どちらかを使う
# STATIC_URL = '/static/'  # スタティックファイルの URL を指定します。
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# AWS S3
# from boto.s3.connection import S3Connection
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com'% AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400',}
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = None
STATIC_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATICFILES_STORAGE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_S3_REGION_NAME = 'ap-northeast-1'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/logmain'
LOGOUT_REDIRECT_URL = '/accounts/login'  # ''

if not DEBUG:
    import django_heroku
    django_heroku.settings(locals())

# # ↓　deploy時のDEBUG確認(config.urls止めてる)
# from django.views.decorators.csrf import requires_csrf_token
# from django.http import (
#     HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound,
#     HttpResponseServerError, )
# del DATABASES['default']['OPTIONS']['sslmode']
