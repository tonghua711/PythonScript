#coding:utf-8

import dns.resolver
#获取MX目标和名称的首选项：
answers = dns.resolver.query('dnspython.org','MX')
for rdata in answers:
    print('Host',rdata.exchange,'has preference',rdata.preference)