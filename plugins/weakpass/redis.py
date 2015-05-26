#coding:utf-8
import sys
sys.path.append('../../')

from lib.plugin import *

__all__ = ["redis"]

class redis(Plugin):
   
    name = "redis"
    version = '0.0.1'

    def __init__(self):
        self.infopayload = '\x2a\x31\x0d\x0a\x24\x34\x0d\x0a\x69\x6e\x66\x6f\x0d\x0a'
        self.apayload = '\x2a\x32\x0d\x0a\x24\x34\x0d\x0a\x41\x55\x54\x48\x0d\x0a\x24'
        self.bpayload = '\x0d\x0a'
        Plugin.__init__(self)
        
    def getPDList(self):
            pwlist =[]
            host = ""
            pass_list = util.load_password_dict(
               host,
               userfile=None, 
               passfile='database/ftp_pass.txt',
               userlist=['sa:sa','username'],
               passlist=['123456'],
               mix=True,
               )
            for u ,p in pass_list:
                if len(p) ==0:
                    p = 'bugscan'
                pwlist.append(p)
            pwlist =  list(set(pwlist))
            return pwlist        
    
    def executeFun(self,target,port):
        ip=target
        port=int(port)
        authpadload = None
        pwlist =self.getPDList()
        try:
            s = socket.socket()
            s.connect((ip,port))
            s.send(self.infopayload)
            data = s.recv(1024)
            if 'redis_version' not in data:
                for p in pwlist:
                    authpadload = self.apayload  + str(len(p)) +self.bpayload + p +  self.bpayload
                    s.send(authpadload)
                    data = s.recv(1024)
                    if 'OK' in data:
                        security_hole('password :' + p)
                        break
                   
            s.close()
            
        except:
            security_info(u"扫描失败！")
        
        
        
        
  
   
        
        
        