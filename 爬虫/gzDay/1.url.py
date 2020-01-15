#encoding:utf-8

# import urllib.request
# url = "http://www.baidu.com"
# response = urllib.request.urlopen(url)
# code = response.getcode()
# html = response.read()
# mystr = html.decode("utf-8")
# response.close()
# print(mystr)

import urllib.request
def download1(url):
    return urllib.request.urlopen(url).read()  #读取全部网页

def download2(url):
    return urllib.request.urlopen(url).readlines()  #读取网页的每一行，压入列表

def download3(url):
    response = urllib.request.urlopen(url)   #网页抽象为文件

    while True:
        line = response.readline()  #读取一行
        if not line:
            break


url="http://www.baidu.com"
# print(download1(url).decode("utf-8"))
# print(download2(url).decode("utf-8"))
print(download3(url))
