# coding:utf-8

"""
通过python调用jenkins接口实现Jenkins服务的检索，打印相关信息
Version:0.1
Author:钟增辉
Date:2019-06-09
#从jenkins1.426开始，jenkins实例对用户进行身份验证是指定API令牌而不是你真实密码

"""

import jenkins

server = jenkins.Jenkins('http://192.168.204.128:8080',username='administrator',password='888888')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'],version))
