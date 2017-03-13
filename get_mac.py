#-*- coding:utf-8 -*-
__author__ = 'tony'

import uuid
import socket
import time

def get_mac_address():
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ':'.join([mac[e:e+2] for e in range(0,11,2)])

myname = socket.getfqdn(socket.gethostname( ))
myaddr = socket.gethostbyname(myname)
print(u'计算机名：%s'%myname)
print(u'IP地址：%s'%myaddr)
print(u'MAC地址：%s'%get_mac_address())
time.sleep(120)