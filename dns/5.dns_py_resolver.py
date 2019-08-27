#coding:utf-8

import dns.resolver

# domain = input('请输入一个域名：')
domain='baidu.com'
MX = dns.resolver.query(domain,'MX')
i: object
for i in MX:
    print('MX preference =',i.preference,'mail exchanger =',i.exchange)