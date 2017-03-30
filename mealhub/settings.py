import os
import dj_database_url
from django.core.urlresolvers import reverse_lazy

LOGIN_REDIRECT_URL = reverse_lazy('user_hub')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

DJANGO_MODE = os.getenv('DJANGO_MODE', "local").lower()
USE_TZ=True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "!8%1z5^yu$%n(rluc$!3g6y%+*rg0gh$gf5gd9v3+423shea_e"
#SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if DJANGO_MODE == 'local' or DJANGO_MODE == 'prod_debug':
	DEBUG = True
else:
	DEBUG = False

# Application definition

INSTALLED_APPS = [
	'mealhub',
	'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
	'easy_maps',
]

EASY_MAPS_CENTER = (-41.3, 32)
EASY_MAPS_GOOGLE_MAPS_API_KEY = 'AIzaSyDSQDa_Q7WD8hGNvCnKNdv7N75YQTVwzV8'

# mealhub.email@gmail.com SMTP server config:
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mealhub.email@gmail.com'
EMAIL_HOST_PASSWORD = 'RfkgjZCisCwyc3iLMAMbbLBwH'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mealhub.urls'

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
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'mealhub.wsgi.application'

if DJANGO_MODE == 'local':
	DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
    		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		 }
     }

elif DJANGO_MODE == 'production' or DJANGO_MODE == 'prod_debug':
	import dj_database_url
    # Handles DATABASE_URL environment variable on Heroku
	DATABASES = {'default': dj_database_url.config(conn_max_age=500)}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'MST'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['localhost','127.0.0.1','www.mealhub.com', 'mealhub.com']

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
