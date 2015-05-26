# -*- coding:gb2312 -*-
__author__ = '云絮'
import socket
import threading
import sys
from Queue import Queue
class scanner():
    def __init__(self,address,port):
        self.address=address
        self.port=port

    def scan(self):
        try:
            sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sk.connect((self.address,self.port))
            print '%s:%d..........open'%(self.address,self.port)
        except Exception,e:
             #print '%s:%d..........close'%(self.address,self.port)
            e
        finally:
            sk.close()
class scannerWork(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue=queue
    def run(self):
        while True:
            try:
                address,port=self.queue.get(False)
                scann=scanner(address,port)
                scann.scan()
            except Exception,e:
                sys.exit(0)
if __name__ == '__main__':
    queue=Queue()
    for i in range(0,65536):
        queue.put(('127.0.0.1',i))
    for a in range(30):
        scanner1=scannerWork(queue)
        scanner1.start()
    scanner1.join()
    print 'scan done!'

