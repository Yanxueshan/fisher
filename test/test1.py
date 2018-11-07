__author__ = 'larry'
__date__ = '2018/7/16 21:06'

from werkzeug.local import LocalStack
import threading
import time

my_stack = LocalStack()
my_stack.push(1)
print('in main thread value is after push: ' + str(my_stack.top))

def worker():
    print('in new thread value is ' + str(my_stack.top))
    my_stack.push(2)
    print('in new thread value is after push: ' + str(my_stack.top))

thread_one = threading.Thread(target=worker)
thread_one.start()
time.sleep(1)
print('finally, in main thread value is: ' + str(my_stack.top))