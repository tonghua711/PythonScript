# encoding:utf-8

import selenium #测试框架
import selenium.webdriver   #模拟浏览器
import re
from threading import Timer
import datetime

def printHello():
    print('TimeNow:%s' %(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    # t = Timer(2,printHello())
    t = Timer(10,pajob)
    t.start()


def getnumberbyname(searchname,adderss):
    url="https://search.51job.com/list/"+ adderss +",000000,0000,00,9,99,"+ searchname  + ",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    # driver = selenium.webdriver.Firefox()#调用火狐狸浏览器
    driver = selenium.webdriver.Chrome()#调用谷歌浏览器

    driver.get(url) #访问链接
    pagesource = driver.page_source #抓取网页源代码
    restr = "共(\\d+)条"
    regex = re.compile(restr, re.IGNORECASE)  # 不区分大小写
    mylist = regex.findall(pagesource)
    driver.close()#关闭
    return (mylist[0])

# print(getnumberbyname("go"))

def pajob():
    pythonlist = ["python", "python 运维", "python 测试", "python 数据", "python web"]
    addressdict = {'上海': '020000', '北京': '010000', '深圳': '040000'}
    # 020000,代表上海
    # 010000,代表北京
    # 040000,代表深圳
    for pyaddr in addressdict:
        print('*'*80)
        for pystr in pythonlist:
            print(pyaddr,pystr, getnumberbyname(pystr,addressdict.get(pyaddr)))
            # print(pyaddr,pystr,addressdict.get(pyaddr))

if __name__ == "__main__":
    printHello()