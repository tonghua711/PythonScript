#coding:utf-8

from IPy import IP

ip = IP('192.168.10.20')
#ip反转 ['20.10.168.192.in-addr.arpa.']
print(ip.reverseNames())
#ip类型，私有还是公有
print(ip.iptype())
