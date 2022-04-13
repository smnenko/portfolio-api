from .settings import *

import environ


env = environ.Env()
environ.Env.read_env(open(BASE_DIR / '.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(' ')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT')
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': (
            f'redis://'
            f'{env("REDIS_USER", default="")}:{env("REDIS_PASS", default="")}@'
            f'{env("REDIS_HOST")}:{env("REDIS_PORT")}/'
            f'{env("REDIS_TABLE")}'
        ),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
