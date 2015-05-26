#coding:utf-8
from common import *
import util
from message import *
import socket
_G = {
    'scanport':False,
    'subdomain': False,
    'target': 'www.abc.com',
    'disallow_ip':['127.0.0.1'],
    'kv' : {}
    }

util._G = _G
class Plugin(object):
    """ 定义一个接口，其他 插件必须实现这个接口，name 属性必须赋值 """
    name = ''
    description = ''
    version = ''
    
    def __init__(self):
        pass
    
    def executeFun(self):
        pass