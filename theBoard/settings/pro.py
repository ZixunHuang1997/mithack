
from .base import *
DEBUG = True
ADMINS = (
    ('zixun HUANG', 'zixunhuang@outlook.com'),
)
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbtest',
        'OPTIONS': {
            # https://blog.csdn.net/weixin_36646275/article/details/106278550
            'charset': 'utf8mb4',
        },
        'USER':'tester',
        'PASSWORD':'Zixun363837#',
        'HOST':'127.0.0.1',
        'PORT':3306,
        'CHARSET':'utf8'
    }
}
# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379
# REDIS_DB = 0