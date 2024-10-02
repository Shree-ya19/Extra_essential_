#IN DJANGO PROJECT THIS CODE IS USED AT LAST AFTER (DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField') IN SETTING.PY
#logger = logging.getLogger("django") the name django here is the name django in ine 27 ( if we place any other name in line 27 than we have to change name here also)
#logger = logging.getLogger("django") this is declared or used in views.py

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