from random import randint


def get_secret_key(nums=16):
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    secret_key = ''
    for i in range(nums):
        secret_key += str[randint(0, len(str)-1)]
    return secret_key


DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/fisher'
SECRET_KEY = 'X5SEspNO8LwgPJjdK379WOJzZWMTQek7'

# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '327218155@qq.com'
MAIL_PASSWORD = 'root'

# 缓存配置Cache
CACHE_TYPE = 'redis'
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = 6379
CACHE_REDIS_DBTYPE = 0
CACHE_PASSWORD = ''


