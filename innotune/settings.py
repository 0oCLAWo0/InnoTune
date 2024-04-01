"""
Django settings for innotune project.

Generated by 'django-admin startproject' using Django 4.0.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

import cloudinary
import cloudinary.uploader
import cloudinary.api
from pathlib import Path
import dj_database_url
from channels.layers import get_channel_layer

from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', '0').lower() in ['true', 't', '1']

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # cors
    'corsheaders',

    # default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party apps
    'drf_spectacular',
    'cloudinary',
    'cloudinary_storage',
    'rest_framework',
    'rest_framework.authtoken',
    'channels',

    # project apps
    'colab',
    'user',
    'comment',
    'music',
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
]

ROOT_URLCONF = 'innotune.urls'

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5173',
    'http://127.0.0.1:3000',
    'http://localhost:5173',
    'http://localhost:3000',
    'http://192.168.1.106:3000',
    'http://192.168.1.87:3000',
    'https://innotune.vercel.app',
    ]



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

# WSGI_APPLICATION = 'innotune.wsgi.application'
ASGI_APPLICATION = 'innotune.asgi.application'

# redis
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [(os.getenv('REDIS_BACKEND_ENDPOINT'), 6379)],
#         },
#     },
# }
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': os.getenv('DB_NAME'),
    #     'HOST': os.getenv('DB_HOST'),
    #     'USER': os.getenv('DB_USER'),
    #     'PORT': os.getenv('DB_PORT'),
    #     'PASSWORD': os.getenv('DB_PASSWORD')
    # }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# our user model
AUTH_USER_MODEL = 'user.User'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10

}

# cloudinary
cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECRET'),
    secure=True
)
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# APP_LOG_FILENAME = os.path.join(BASE_DIR, 'log/app.log')
# 
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     # "handlers": {
#     #     "app_log_file": {
#     #         "level": "INFO",
#     #         "class": "logging.FileHandler",
#     #         "filename": APP_LOG_FILENAME,
#     #     },
#     # },
#     # "root": {
#     #     "handlers": ["app_log_file"],
#     #     "level": "INFO",
#     # },
#     # "loggers": {
#     #     "django": {
#     #         "handlers": ["app_log_file"],
#     #         "level": "INFO",
#     #         "propagate": False,
#     #     },
#     # },
#     'handlers': {
#         'console': {
#             'level': 'INFO',  # Adjust log level as needed
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'INFO',  # Adjust log level as needed
#             'propagate': True,
#         },
#     },
# }

# # cron job
# CRONJOBS = [
#     ('* */6 * * *', 'music.cron.remove_recent_songs'),
#     ('* */6 * * *', 'user.cron.remove_inactive_users'),
# ]

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}


# MAIL
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAI_HOST = os.getenv('EMAI_HOST')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER') # this is temporary mail change it with ypur mail
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')