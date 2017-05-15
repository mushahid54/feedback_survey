from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "vaultekbaar",
        'USER': "summerlabel",
        'PASSWORD': "postgres",
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

