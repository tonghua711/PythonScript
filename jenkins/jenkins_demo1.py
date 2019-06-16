# coding:utf-8

"""
通过jenkins api 调用传参

Version:0.1
Auther:钟增辉
Date :2019-06-07
https://python-jenkins.readthedocs.io/en/latest/api.html
"""

import jenkins
import time

# demo01 = 'demo01'
server = jenkins.Jenkins('http://192.168.204.128:8080',username='administrator',password='888888')
user = server.get_whoami()
version = server.get_version()
# print('Hello %s from Jenkins %s' % (user['fullName'], version))
server.build_job('新建任务jenkins测试', {'IT_TEST': 'it112', 'SVN_NUM': '2345','SVN_BRANCH':'V3.16.0'})
#调用get_build_info  查看job相关信息
# sleep(23)
try:
    last_build_number = server.get_job_info('新建任务jenkins测试')['lastCompletedBuild']['number']
    print(last_build_number)
except TypeError as e:
    print(e)
build_number = server.get_job_info('新建任务jenkins测试')['lastBuild']['number']
build_status = server.get_build_info('新建任务jenkins测试', build_number)['building']

print(build_number)
print(build_status)

# print(server.get_build_console_output('新建任务jenkins测试',9))
# print(server.get_build_env_vars('新建任务jenkins测试',8))
# print(server.get_build_test_report('新建任务jenkins测试',8))
# # result_st = server.get_build_info('result',)