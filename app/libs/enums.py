__author__ = 'larry'
__date__ = '2018/7/24 23:23'

from enum import Enum


class PendingStatus(Enum):
    '''
        记录交易的4种状态
    '''
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4

    @classmethod
    def pendingstr(cls, status, key):
        key_map = {
            cls.Waiting: {
                'requester': '等待对方邮寄',
                'gifter': '等待您邮寄'
            },
            cls.Reject: {
                'requester': '对方已拒绝',
                'gifter': '您已拒绝'
            },
            cls.Redraw: {
                'requester': '您已撤销',
                'gifter': '对方已撤销'
            },
            cls.Success: {
                'requester': '对方已邮寄',
                'gifter': '您已邮寄，交易完成'
            }
        }
        return key_map[status][key]