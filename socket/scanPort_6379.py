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
    for p in range(6378,6380):
    #设置需要扫描的ip段
        for d in range(127,130):
            # portScanner('192.1.50.'+ str(d),p)
            portScanner('192.168.204.'+ str(d),p)
    print(len(ipList))
    with open('ipTable.txt','w') as f:
        for i in ipList:
            f.write(i)

if __name__ == '__main__':
    main()
