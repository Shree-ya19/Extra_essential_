#IN DJANGO PROJECT THIS CODE IS USED AT LAST AFTER (DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField') IN SETTING.PY



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'timestamp': {
            'format': '{asctime} {levelname} {message} {lineno} ',
            'style': '{',

        },

    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'timestamp'
        },


    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },

    },
}