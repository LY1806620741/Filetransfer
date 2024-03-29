"""
Django settings for filetransfer project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# config path
RUN_DIR = os.getcwd()
MEDIA_ROOT = RUN_DIR #文件路径不是绝对路径是项目路径
MEDIA_URL = '/public/'
MEDIA_LIMIT_SIZE = 2*1024**3 #单位字节 三次方G
MEDIA_SIZE=None
LOGNAME = "server.log"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w38djes5_ra2kjne0a7gt18867#ag!x#_3$&tnoswyglj5_@k%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'app.filetransfer.urls'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True

#日志https://docs.djangoproject.com/zh-hans/2.1/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False, 
    'formatters': {
        # 详细的日志格式https://docs.python.org/3/library/logging.html#logrecord-attributes
        'standard': {
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                      '[%(levelname)s][%(message)s]'
        },
        'accessformatter': {
            'format': '[%(asctime)s][%(levelname)s][%(message)s]'
        },
    },
    # 处理器
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(RUN_DIR, LOGNAME),
            'encoding': 'utf-8',
            'formatter': 'standard',
        },
        'fileaccess': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(RUN_DIR, LOGNAME),
            'encoding': 'utf-8',
            'formatter': 'accessformatter',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'views': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'access': {
            'handlers': ['fileaccess', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['fileaccess', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
