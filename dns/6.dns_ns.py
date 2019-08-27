#coding:utf-8

import dns.resolver

domain = input('请输入域名：')
domain = 'qq.com'

ns = dns.resolver.query(domain,'NS')
for i in ns.response.answer:
    for j in i.items:
        print(j.to_text())