# coding:utf-8
from socket import *
ipList = []
def portScanner(host,port):
    try:
        # print(type(host))
        # print(host)
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        ipList.append(host)
        print('[+] %s %d open' % (host, port))
        s.close()
    except:
        print('[-] %s %d close' % (host, port))

def main():
    setdefaulttimeout(1)
    #设置需要扫描的端口
    for p in range(1521,1522):
    #设置需要扫描的ip段
        for d in range(1,245):
            portScanner('192.1.50.'+ str(d),p)
    print(len(ipList))
if __name__ == '__main__':
    main()
