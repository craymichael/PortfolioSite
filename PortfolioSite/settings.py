"""
Django settings for PortfolioSite project.
"""

import os
from configparser import RawConfigParser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Discover config file for project
_config_filename = 'settings.ini'

_config_local_name = os.path.join(BASE_DIR, _config_filename)
_config_home_name = os.path.join('~', '.portfoliosite', _config_filename)
_config_etc_name = os.path.join('etc', 'portfoliosite', _config_filename)

if os.path.isfile(_config_local_name):
    _config_path = _config_local_name
elif os.path.isfile(_config_home_name):
    _config_path = _config_home_name
elif os.path.isfile(_config_etc_name):
    _config_path = _config_etc_name
else:
    raise RuntimeError('Could not discover project settings file in: "{}", "{}", or "{}"'.format(
        _config_local_name, _config_home_name, _config_etc_name))

_config = RawConfigParser()
_config.read(_config_path)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = _config.get('security', 'SECRET_KEY')

RECAPTCHA_SECRET_KEY = _config.get('security', 'RECAPTCHA_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = _config.get('hosts', 'ALLOWED_HOSTS')
ALLOWED_HOSTS = [_host.strip() for _host in ALLOWED_HOSTS.split(',')]

# Application definition

INSTALLED_APPS = [
    'portfolio.apps.PortfolioConfig',
    #'django.contrib.admin',
    #'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
]

ROOT_URLCONF = 'PortfolioSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                #'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PortfolioSite.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Email

EMAIL_HOST = _config.get('email', 'EMAIL_HOST')
EMAIL_PORT = _config.getint('email', 'EMAIL_PORT')
EMAIL_HOST_USER = _config.get('email', 'EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = _config.get('email', 'EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = _config.getboolean('email', 'EMAIL_USE_TLS')

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

CONTACT_EMAIL = _config.get('email', 'CONTACT_EMAIL')


# Password validation

#AUTH_PASSWORD_VALIDATORS = [
    #{
    #    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #},
#]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# HTTPS
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_REFERRER_POLICY = 'same-origin'
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS= True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 86400
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS='DENY'

# No auth
#REST_FRAMEWORK = {
#    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
#    'UNAUTHENTICATED_USER': None,
#    'DEFAULT_AUTHENTICATION_CLASSES': [],
#    'DEFAULT_PERMISSION_CLASSES': [],
#}

# 500 error if this is not here rather than at top...
import django
django.setup()

