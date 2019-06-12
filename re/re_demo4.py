# coding:utf-8
"""
字符?表明它前面的分组有或者没有都可以。匹配1次或者0次
"""
import re
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())



