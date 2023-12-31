import platform
import environ
import os


DEBUG = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'S#dsaqw23234342kl;j44%&%^7$%67%54^%Y^%h'

# Assets Management
ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')
HOME_ASSET_ROOT = '/static/home_assets'

# load production server from .env
ALLOWED_HOSTS = ['*', 'localhost', 'btlabs.tech', 'www.btlabs.tech', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1', 'https://www.btlabs.tech', 'https://btlabs.tech']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'apps.home.HomeConfig',
    'apps.projects.ProjectsConfig',
    'apps.epicweb.EpicwebConfig',
    'apps.funding.FundingConfig',
    'apps.easyminer.EasyminerConfig',
    'apps.miningcalc.MiningcalcConfig',
    'apps.epicradar.EpicradarConfig',
    'apps.giverofepic.GiverofepicConfig',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    ]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.context_processors.cfg_assets_root',
                ],
            },
        },
    ]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
#
# if os.environ.get('DB_ENGINE') and os.environ.get('DB_ENGINE') == "mysql":
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': os.getenv('DB_NAME', 'appseed_db'),
#             'USER': os.getenv('DB_USERNAME', 'appseed_db_usr'),
#             'PASSWORD': os.getenv('DB_PASS', 'pass'),
#             'HOST': os.getenv('DB_HOST', 'localhost'),
#             'PORT': os.getenv('DB_PORT', 3306),
#             },
#         }
# else:
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
            }
        }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
    )

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# PRODUCTION
if 'PRODUCTION' in os.environ and os.environ['PRODUCTION'] == 'true':
    print(f"RUN IN PRODUCTION MODE")
    DEBUG = False
    STATIC_ROOT = "/var/www/html/btlabs.tech/staticfiles/"

#############################################################
#############################################################
