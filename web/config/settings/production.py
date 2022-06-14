from .base import *

DEBUG = False
ALLOWED_HOSTS = ['yourproject.example.com']

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'formatters': {
        'prod':{
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'INFO',
        },
    },
    'root': {
        'handlers': ['console'],
    }
}