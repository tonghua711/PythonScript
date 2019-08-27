# coding:utf-8

import dns.resolver

domain = input("请输入域名：")

A = dns.resolver.query(domain,'A')
for i in A.response.answer:
    for j in i.items:
        print(j)