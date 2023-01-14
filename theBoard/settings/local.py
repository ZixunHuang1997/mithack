from .base import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_test',
        'OPTIONS': {
            # Tell MySQLdb to connect with 'utf8mb4' character set
            # https://blog.csdn.net/weixin_36646275/article/details/106278550
            'charset': 'utf8mb4',
        },
        'USER':'tester',
        'PASSWORD':'363837',
        'HOST':'127.0.0.1',
        'PORT':3306,
        'CHARSET':'utf8'
    }
}