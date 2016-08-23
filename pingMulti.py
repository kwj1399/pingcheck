#!/usr/bin/python
#_*_coding:utf-8_*_
''' 多线程多主机ping'''
import pexpect
import datetime
from threading import Thread

host=[
'10.247.8.214',
'10.247.8.215',
'10.247.8.216',
'10.247.8.217',
'10.247.8.218',
'10.247.8.219',
'10.247.8.220',
'10.247.8.221',
'10.247.8.222',
'10.247.8.223',
'10.247.8.224',
'10.247.8.225',
'10.247.8.226',
'10.247.8.231',
'10.247.8.232',
'10.247.8.233',
'10.247.8.15'
]
class PING(Thread):
    def __init__(self,ip):
        Thread.__init__(self)
        self.ip = ip
    def run(self):
        Curtime = datetime.datetime.now()
        ping = pexpect.spawn("ping -c1 %s"%(self.ip))
        check = ping.expect([pexpect.TIMEOUT,
                             "1 packets transmitted, 1 received, 0% packet loss"],2)
        if check == 0:
            print("[%s] %s 超时")%(Curtime,self.ip)
        elif check == 1:
            print("[%s] %s 正常")%(Curtime,self.ip)
        else:
            print("[%s] %s不可达")%(Curtime,self.ip)
            
if __name__ == '__main__':
    T_thread=[]
    for i in host:
        t = PING(i)
        T_thread.append(t)
    for i in range(len(T_thread)):
        T_thread[i].start()
    
            