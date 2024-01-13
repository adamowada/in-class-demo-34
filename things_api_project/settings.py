"""
Django settings for things_api_project project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import environ  # new for .env files

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# new for .env
env = environ.Env(
    DEBUG=(bool, False),
    ENVIRONMENT=(str, "PRODUCTION"),

    ALLOW_ALL_ORIGINS=(bool, False),
    ALLOWED_HOSTS=(list, []),
    ALLOWED_ORIGINS=(list, []),

    DATABASE_ENGINE=(str, "django.db.backends.sqlite3"),
    DATABASE_NAME=(str, BASE_DIR / "db.sqlite3"),
    DATABASE_USER=(str, ""),
    DATABASE_PASSWORD=(str, ""),
    DATABASE_HOST=(str, ""),
    DATABASE_PORT=(int, 5432),
)

environ.Env.read_env()

ENVIRONMENT = env.str("ENVIRONMENT")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-k&+1cet2d8qdjt_$-e_=^qv3p%%d1wo&^-hp+sc3lvjpnjz%%-'
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = env.bool("DEBUG")

# ALLOWED_HOSTS = ['*']  # insecure but will work for all hosts, good for development
ALLOWED_HOSTS = tuple(env.list("ALLOWED_HOSTS"))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'rest_framework',
    'corsheaders',

    # Local
    'things',
    'wishlists',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",  # new for cors
    "whitenoise.middleware.WhiteNoiseMiddleware",  # new for whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'things_api_project.urls'

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

WSGI_APPLICATION = 'things_api_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "postgres",
#         "USER": "postgres",
#         "PASSWORD": "postgres",
#         "HOST": "db",
#         "PORT": 5432,
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": env.str("DATABASE_ENGINE"),
        "NAME": env.str("DATABASE_NAME"),
        "USER": env.str("DATABASE_USER"),
        "PASSWORD": env.str("DATABASE_PASSWORD"),
        "HOST": env.str("DATABASE_HOST"),
        "PORT": env.int("DATABASE_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# https://docs.djangoproject.com/en/5.0/ref/settings/#static-root
# new for whitenoise
STATIC_ROOT = BASE_DIR / "staticfiles"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = "accounts.CustomUser"  # must agree with the app's models.py


# New setting for DRF
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.AllowAny',  # Insecure!
        'rest_framework.permissions.IsAuthenticated',  # new, if the user is signed in or not
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # This authentication class is part of the djangorestframework-simplejwt package. It is used for handling
        # JSON Web Tokens (JWT) authentication. JWTs are an open standard (RFC 7519) that define a compact and
        # self-contained way for securely transmitting information between parties as a JSON object. This method is
        # often used in RESTful APIs and is particularly useful for Single Page Applications (SPAs) and mobile apps.
        'rest_framework_simplejwt.authentication.JWTAuthentication',

        # This is a Django REST framework's built-in authentication class. It authenticates users based on their
        # session. This method is typically used in traditional web applications where the user logs in and the
        # session is stored in the server-side session store. It uses Django's session framework and is therefore
        # dependent on Django's session middleware.
        'rest_framework.authentication.SessionAuthentication',  # optional

        # Also a built-in authentication class of Django REST framework. It provides a simple, HTTP basic
        # authentication method. Basic authentication uses standard fields in the HTTP header to include a username
        # and password. This method is simple but not very secure on its own, as credentials are only encoded with
        # Base64 and not encrypted. It's generally recommended to use this in conjunction with HTTPS.
        # 'rest_framework.authentication.BasicAuthentication',  # optional
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        seconds=60 * 60
    ),  # lasts for 60 minutes
}

# set in .env
CORS_ORIGIN_WHITELIST = tuple(env.list("ALLOWED_ORIGINS"))
CORS_ALLOW_ALL_ORIGINS = env.bool("ALLOW_ALL_ORIGINS")

# Tests will use sqlite:
import sys  # move to the top


# When you run python manage.py test, the sys.argv would include 'test'.
if 'test' in sys.argv:
    # reassign DATABASES setting if testing
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }