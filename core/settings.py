
import os
from pathlib import Path
from pathlib import Path
from environ import Env
from datetime import timedelta

from core.database import get_db_config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = Env()
env.read_env(BASE_DIR / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", True)

# If debug true, all host allowed
ALLOWED_HOSTS = [
    "*",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    *[f"http://{x}:5173" for x in env.list("DEVELOPING_CORS_ALLOWED")]
]

CORS_ORIGIN_WHITELIST = CORS_ALLOWED_ORIGINS

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'none'
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAdminUser',
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter'
    ],
}

SESSION_COOKIE_AGE = 60 * 30

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Application definition
BASE_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    # 'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    'simple_history',
    'drf_yasg',
    'debug_toolbar'
]

MY_APPS = [
    'apps.base',
    'apps.medicos',
    'apps.ubicaciones'
]

INSTALLED_APPS = BASE_APPS + MY_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [],
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

JAZZMIN_SETTINGS = {
    "site_title": "SOCIMED",
    "site_brand": "SOCIMED",
    "site_logo": "../media/logo-white-sm.png",
    "login_logo": "../media/logo-dark-sm.png",
    "welcome_sign": "Sistema de directorio sociedad medica.",
    "order_with_respect_to": ["auth", "medicos", "ubicaciones"],
    "icons": {
        "auth.user": "fa fa-user",
        "auth.group": "fa fa-users",
        "medicos.especialidad": "fa fa-book-medical",
        "medicos.medico": "fa fa-stethoscope",
        "medicos.ubicacion": "fa fa-globe",
        "ubicaciones.torre": "fa fa-building",
        "ubicaciones.piso": "fas fa-arrow-right",
        "ubicaciones.localidad": "fa fa-location-arrow"
    },
    "topmenu_links": [
        {
            "name": "Inicio",
            "url": "admin:index",
            "permissions": ["auth.view_user"]
        },
        {
            "name": "Generar Carnet",
            "url": "http://socimed.cpv.com.ve/",
            "permissions": ["auth.view_user"]
        },
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=5),  
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=8),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True
}

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        **get_db_config(env.str("DB_ENGINE"), BASE_DIR),
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]

WSGI_APPLICATION = 'core.wsgi.application'

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

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_TZ = True

TIME_INPUT_FORMATS = [
    "%I:%M %p",
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CONFIGURACION DE SERVIDOR DE EMAILS PARA REPORTE DE ERRORES

ADMINS = [
    # ("Leandro", "programador3@cpv.com.ve"),
    ("Giancarlo", "programador2@cpv.com.ve"),
    # ("Danny", "programador1@cpv.com.ve"),
]
DEFAULT_FROM_EMAIL = env.str("EMAIL_ADDRESS")
SERVER_EMAIL = env.str("EMAIL_ADDRESS")
EMAIL_HOST = "localhost"
EMAIL_PORT = 8025

if not DEBUG:
    ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
    CORS_ALLOWED_ORIGINS = [f"http://{x}" for x in env.list("PRODUCTION_CORS_ALLOWED")]
    CORS_ORIGIN_WHITELIST = CORS_ALLOWED_ORIGINS
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAdminUser',
            'rest_framework.permissions.IsAuthenticated',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
        'DEFAULT_FILTER_BACKENDS': [
            'django_filters.rest_framework.DjangoFilterBackend',
            'rest_framework.filters.SearchFilter',
            'rest_framework.filters.OrderingFilter'
        ],
    }
    # Servidor SMTP para envío de correos
    ADMINS = [
    ("Leandro", "programador3@cpv.com.ve"),
    ("Giancarlo", "programador2@cpv.com.ve"),
    ("Danny", "programador1@cpv.com.ve"),
    ]
    EMAIL_HOST = env.str("EMAIL_SERVER")
    EMAIL_PORT = env.int("EMAIL_PORT")
