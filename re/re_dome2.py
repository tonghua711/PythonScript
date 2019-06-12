# coding:utf-8

import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-5555-4242.')
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.group())
# print(mo.group(3))

print(mo.groups())