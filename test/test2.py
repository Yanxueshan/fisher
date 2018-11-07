__author__ = 'larry'
__date__ = '2018/7/17 1:04'
from random import randint

def get_secure_key(nums=16):
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    secure_key = ''
    for i in range(nums):
        secure_key += str[randint(0, len(str)-1)]
    return secure_key

result = get_secure_key()
print(result)
