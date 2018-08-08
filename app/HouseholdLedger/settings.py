"""
Django settings for HouseholdLedger project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nl)itz7d-+*y6az&^c%o6bvs!kyo5n3(g&ve885#-5+set95_v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # RestFul FrameWork
    'rest_framework',
    # RestFul FrameWork Swagger
    'rest_framework_swagger',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',

    'corsheaders',
    # application list
    'home',
    'transaction',
    'budget'
]

MIDDLEWARE = [
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'middleware.authCheck.JwtExpiCheck'
]
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'HouseholdLedger.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],

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

WSGI_APPLICATION = 'HouseholdLedger.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'django',
    'USER': 'django',
    'PASSWORD': 'password',
    'HOST': 'db',
    'PORT': '5432',
  },
  'test': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'dist'),
  os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'public')
STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/account/login'


# Configure the JWTs to expire after 1 hour, and allow users to refresh near-expiration tokens
JWT_AUTH = {
  'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=3),
  'JWT_ALLOW_REFRESH': True,

}

# Make JWT Auth the default authentication mechanism for Django
REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
  ),
}
AUTHENTICATION_BACKENDS = (
  # Needed to login by username in Django admin, regardless of `allauth`
  'django.contrib.auth.backends.ModelBackend',

  # `allauth` specific authentication methods, such as login by e-mail
  'allauth.account.auth_backends.AuthenticationBackend',
)
# Enables django-rest-auth to use JWT tokens instead of regular tokens.
REST_USE_JWT = True
SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_AUTHENTICATION = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SWAGGER_SETTINGS = {
  'SECURITY_DEFINITIONS': {
    'basic': {
      'type': 'basic'
    }
  },
}

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
    'verbose': {
      'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
    },
    'simple': {
      'format': '%(levelname)s %(message)s'
    },
  },
  'handlers': {
    'debug': {
      'level': 'DEBUG',
      'class': 'logging.FileHandler',
      'filename': './log/django/debug.log',
      'formatter': 'verbose',
    },
    'error': {
      'level': 'ERROR',
      'class': 'logging.FileHandler',
      'filename': './log/django/error.log',
      'formatter': 'verbose',
    },
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler',
      'formatter': 'verbose'
    },
  },
  'loggers': {
    'django': {
      'handlers': ['console', 'debug', 'error'],
      'level': 'DEBUG',
      'propagate': True,
    },
  },
}

import sys

if 'test' in sys.argv:

   DATABASES['default'] = DATABASES['test']

