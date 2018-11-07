from enum import Enum

__author__ = 'larry'
__date__ = '2018/7/25 13:26'

class PendingStatus(Enum):
    '''
        记录交易的4种状态
    '''
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4

print(PendingStatus.Waiting)
print(type(PendingStatus.Waiting.value))
