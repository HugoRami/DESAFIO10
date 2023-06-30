from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@(#$8vv8=u3_%02msbr$a=tn3k)-gutu%(8z$v-8(&_a%tt4p4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] # SOLO DURANTE EL DESARROLLO !!!!

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
