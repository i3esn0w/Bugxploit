#coding:utf-8
import sys
sys.path.append('../')

from lib.plugin import *

__all__ = ["test"]

class test(Plugin):
   
    name = "test"
    version = '0.0.1'

    def __init__(self):
        #self.a=param["a"]
        Plugin.__init__(self)
    
    def executeFun(self,target):
        security_info("aaaaaaaaa")
        security_note(target)
        
        
        