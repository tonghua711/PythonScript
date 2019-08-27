# coding:utf-8

import dns.query
import dns.zone

#从服务器传输区域并使用以DNSSEC顺序排序的名称打印它

z = dns.zone.from_xfr(dns.query.xfr('14.215.177.39','www.baidu.com'))
names = z.nodes.keys()
names.sort()
for n in names:
    print(z[n].to_text(n))