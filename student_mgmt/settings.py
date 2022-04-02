
import os
from pathlib import Path
# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--+x^m!5d^0o98)7%9u@gp3$0o8zb^97gc#8@)&=x#$*rn1w$mq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
    #'admin_interface',
    #'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'studentapp',
    # "debug_toolbar",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'student_mgmt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'student_mgmt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = (BASE_DIR / 'staticfile')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]

MEDIA_URL='/media/'

MEDIA_ROOT=BASE_DIR / 'media'

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
    
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# sentry_sdk.init(
#     dsn="https://examplePublicKey@o0.ingest.sentry.io/0",
#     integrations=[DjangoIntegration()],

#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production,
#     traces_sample_rate=1.0,
# )
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

AUTH_USER_MODEL = 'studentapp.CustomUser'

# RAZORPAY_KEY_ID = 'rzp_live_i4OVIpsxBoHieZ'
# RAZORPAY_KEY_SECRET = "tWbWS8vpbMSFzcXyadmk5YVT"

RAZORPAY_KEY_ID = 'rzp_test_czVP739sBN5blU'
RAZORPAY_KEY_SECRET = "MBpgYsg92tAkraZtv5BMyLeq"