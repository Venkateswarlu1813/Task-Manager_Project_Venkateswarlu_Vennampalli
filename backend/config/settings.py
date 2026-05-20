from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta

import os
import cloudinary


# -------------------- LOAD ENV --------------------

load_dotenv()


# -------------------- BASE DIR --------------------

BASE_DIR = Path(__file__).resolve().parent.parent


# -------------------- SECURITY --------------------

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG') == 'True'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]


# -------------------- CLOUDINARY --------------------

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)


# -------------------- INSTALLED APPS --------------------

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'drf_yasg',

    'apps.authentication',
    'apps.users',
    'apps.teams',
    'apps.tasks',
    'apps.notifications',
    'apps.common',
]


# -------------------- MIDDLEWARE --------------------

MIDDLEWARE = [

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# -------------------- ROOT URL --------------------

ROOT_URLCONF = 'config.urls'


# -------------------- TEMPLATES --------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# -------------------- WSGI --------------------

WSGI_APPLICATION = 'config.wsgi.application'


# -------------------- DATABASE --------------------

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': os.getenv('DB_NAME'),

        'USER': os.getenv('DB_USER'),

        'PASSWORD': os.getenv('DB_PASSWORD'),

        'HOST': os.getenv('DB_HOST'),

        'PORT': os.getenv('DB_PORT'),
    }
}


# -------------------- AUTH USER --------------------

AUTH_USER_MODEL = 'users.User'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]


# -------------------- PASSWORD VALIDATION --------------------

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


# -------------------- INTERNATIONALIZATION --------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# -------------------- STATIC FILES --------------------

STATIC_URL = 'static/'


# -------------------- MEDIA --------------------

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# -------------------- JWT --------------------

SIMPLE_JWT = {

    'ACCESS_TOKEN_LIFETIME': timedelta(hours=5),

    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}


# -------------------- REST FRAMEWORK --------------------

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


# -------------------- EMAIL --------------------

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.getenv('EMAIL_HOST')

EMAIL_PORT = int(os.getenv('EMAIL_PORT'))

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == 'True'


# -------------------- CORS --------------------

CORS_ALLOW_ALL_ORIGINS = True


# -------------------- DEFAULT AUTO FIELD --------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'