#!/usr/bin/python
#coding:utf-8
import paramiko
import sys
import datetime
import threading
import queue
import getopt


def usage():
    print("""
            -h,-H,--help         帮助页面 
              -C, --cmd            执行命令模式 
              -M, --command        执行具体命令 
              -S, --sendfile       传输文件模式 
              -L, --localpath      本地文件路径 
              -R, --remotepath     远程服务器路径 
             IP列表格式:
         IP地址		用户名     密码     端口
         192.168.1.1        root	  123456    22
      	e.g.
              批量执行命令格式： -C "IP列表" -M '执行的命令'
              批量传送文件：     -S "IP列表" -L "本地文件路径" -R "远程文件路径"
          错误日志文件：$PWD/ssh_errors.log
    """)

def ssh(queue_get,cmd):
    try:
        hostip = queue_get[0]
        username = queue_get[1]
        password = queue_get[2]
        port = queue_get[3]
        s = paramiko.SSHClient()
        s.load_system_host_keys()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        s.connect(hostname=hostip,port=port,username=username,password=password)
        stdin,stdout,stderr=s.exec_command(cmd)
        print("\033[42m----------------------------------%s-------------------------\033[0m \n %s" %(hostip,stdout.read()))
        s.close()
    except Exception as ex:
        print("\033[42m----------------------------------%s-------------------------\033[0m \n %s" %(hostip,stdout.read()))
        ssh_errors = open("ssh_errors.log","a")
        ssh_errors.write("%s\t%s\n" %(now,hostip,ex))
        ssh_errors.close()
        pass
def sftp(queue_get,localpath,remotepath):
    try:
        hostip = queue_get[0]
        username = queue_get[1]
        