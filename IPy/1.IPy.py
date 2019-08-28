#coding:utf-8

from IPy import IP

#测试是ip4
print(IP('10.0.0.1').version())
#ipv 6
print(IP('::1').version())

ip=IP('192.168.0.0/16')
print(ip)
print(ip.len())
for x in ip:
    print(x)
