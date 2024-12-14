"""
Django settings for api_orden_pago project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$ho75k5pw@)5_hjvd-#@yn!i0h&j(sw#mjhxtsc7uj)7lbo5^k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

ALLOWED_HOSTS_ENV = os.environ.get('ALLOWED_HOSTS')
if(ALLOWED_HOSTS_ENV):
    ALLOWED_HOSTS.extend(ALLOWED_HOSTS_ENV.split(','))

CORS_ALLOW_ALL_ORIGINS = True


# Permitir conexiones desde localhost y 127.0.0.1
ALLOWED_HOSTS.append('localhost')
ALLOWED_HOSTS.append('127.0.0.1')

# Permitir 0.0.0.0 para conexiones de prueba, pero no en producción
if DEBUG:  # Solo si estás en modo de desarrollo (DEBUG=True)
    ALLOWED_HOSTS.append('0.0.0.0')

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'api_pago',
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
    'api_orden_pago.middleware.ProcessExceptionMiddleware',
]

ROOT_URLCONF = 'api_orden_pago.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'api_orden_pago.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'NAME': os.environ.get('DB_NAME', 'mydatabase'),
        'USER': os.environ.get('DB_USER', 'myuser'),
        'PASSWORD': os.environ.get('DB_PASS', 'mypassword'),
        'OPTIONS': {
            'charset': 'utf8mb4',
            'use_unicode': True,
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = '/app/staticfiles'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_datatables.renderers.DatatablesRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_datatables.filters.DatatablesFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_datatables.pagination.DatatablesPageNumberPagination',
    'PAGE_SIZE': 50,
}

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'ERROR',  # Guarda los logs de nivel ERROR y superiores
#             'class': 'logging.FileHandler',
#             'filename': '/webapps/api_orden_pago/logs/error.log',  # Asegúrate de que esta carpeta exista
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'ERROR',  # Puedes cambiar el nivel según lo que necesites
#             'propagate': True,
#         },
#     },
# }

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
