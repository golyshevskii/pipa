"""
Django settings for pipa project.
Generated by 'django-admin startproject' using Django 3.1.7.
"""

from pathlib import Path
# импорт метода reverse_lazy для возвращения, относительно имени, одного из абсолютных путей приложения до его инициализации
# import of the reverse_lazy method to return, relative to the name, one of the absolute paths of the application before it was initialized
from django.urls import reverse_lazy
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
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
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pipa.urls'

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

WSGI_APPLICATION = 'pipa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# LOGIN_REDIRECT_URL: cообщает о том, на какой URL перенаправлять пользователя после входа в систему; tells you which URL to redirect the user to after login
# LOGIN_URL: URL-адрес для перенаправления пользователя на вход; URL to redirect user to login
# LOGOUT_URL: URL-адрес для перенаправления пользователя на выход; URL to redirect user to logout
LOGIN_REDIRECT_URL = reverse_lazy('account:profile')
LOGIN_URL = reverse_lazy('account:login')
LOGOUT_URL = reverse_lazy('account:logout')

# использование отладочного сервера SMTP python -m smtpd -n -c DebuggingServer localhost:1025, для отправки сообщений пользователям
# using the SMTP debug server python -m smtpd -n -c DebuggingServer localhost: 1025, to send messages to users
EMAIL_PORT = 1025

# указание модели пользователя для создания базы данных о пользователе
# specifying a user model for creating a user database
AUTH_USER_MODEL = 'account.Profile'

# маршруты хранения статических файлов(изображения)
# paths for storing static files (images)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',   # настройки входа через email; email login settings
    'social_core.backends.google.GoogleOAuth2',  # настройки входа google аккаунт; google account login settings
    ]

# API настройки для google авторизации
# API settings for google authorization
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'KEY'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'SECRET KEY'
SOCIAL_AUTH_URL_NAMESPACE = 'social'

