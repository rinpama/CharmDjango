"""
Django settings for CharmDjango project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import django_heroku
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# from .local_settings import SECRET_KEY######

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG=False

try:
    from CharmDjango.local_settings import *
except ImportError:
    pass
if not DEBUG:
    import django_heroku
    django_heroku.settings(locals())

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'markdownx',
    'accounts',
    'm3ch',
    'Soen',
    'Show',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
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
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

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

STATIC_URL = '/static/'
# 開発時
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')]
# 本番環境 # STATIC_ROOT='/var/www/static' # 例
STATIC_ROOT='staticfiles'


MEDIA_URL = '/media/'
if DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# else:
#     PROJECT_NAME = os.path.basename(BASE_DIR)
#     # ↓ は一般的なLinuxサーバーにデプロイする場合のパス。クラウドにデプロイする場合、下記は要修正。
#     MEDIA_ROOT = "/var/www/{}/media".format(PROJECT_NAME)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/logmain'
LOGOUT_REDIRECT_URL = '/accounts/login'  # ''

# https://python-markdown.github.io/extensions/
MARKDOWNX_MARKDOWN_EXTENSIONS = [
    # HTMLでのマークダウン'markdown.extensions.md_in_html'
    'md_in_html',
    # テーブル'markdown.extensions.tables'
    'tables',
]
MARKDOWNX_IMAGE_MAX_SIZE = {
    'size': (500, 500), 'quality': 90
}

SUMMERNOTE_THEME = 'bs4'
X_FRAME_OPTOPNS = 'SAMEORIGIN'




django_heroku.settings(locals())