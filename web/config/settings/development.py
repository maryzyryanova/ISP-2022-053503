from .base import * 

DEBUG = True
ALLOWED_HOSTS = ['*']
# INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar']
# MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'formatters': {
        'dev':{
            'format': '{levelname} {message}',
            'style': '{',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
        },
    },
    'root': {
        'handlers': ['console'],
    }
}