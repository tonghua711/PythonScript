#coding:utf-8

from IPy import IP

ip_s = input("请输入一个IP或者域名：")
ips = IP(ip_s)

if len(ips) > 1:
    print('net:%s' % ips.net())  #输出网络地址
    print('netmask:%s' % ips.netmask()) #输出网络掩码地址
    print('broadcast:%s' % ips.broadcast()) #输出网络广播地址
    print('reverse address:%s' % ips.reverseNames()[0])  #输出地址反向解析
    print('subnet:%s' % len(ips))
else:
    print('reverse address:%s' % ips.reverseNames()[0]) #输出Ip反向地址解析

print('hexadecimal:%s' % ips.strHex()) #输出十六进制地址
print('binary ip:%s' % ips.strBin())
print('iptype:%s' % ips.iptype())  #输出地址类型