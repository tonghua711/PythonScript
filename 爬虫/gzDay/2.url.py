# encoding:utf-8
import re

mystr = """<div class="rt">
    共3474条职位
</div>"""

#正则表达式，括号代表只要括号内的数据
restr = "共(\\d+)条"
regex = re.compile(restr,re.IGNORECASE)  #不区分大小写
mylist = regex.findall(mystr)
print(mylist)
print(mylist[0])