# coding:utf-8
"""
jenkins 作业，如何创建，配置和删除Jenkins作业
Version :0.1
Author: 钟增辉
Date: 2019-06-09
"""
import jenkins
#登陆Jenkins
server = jenkins.Jenkins('http://192.168.204.128:8080',username='administrator',password='888888')
#创建新job
# server.create_job('api-test',jenkins.EMPTY_CONFIG_XML)
# jobs = server.get_jobs()
# print(jobs)
#打印job信息，显示xml格式
# my_job = server.get_job_config('empty')
# print(my_job)
#运行job
# server.build_job('empty')
#禁用job
# server.disable_job('empty')
#拷贝jenkins job
# server.copy_job('empty','emppty_copy')
#开启job
# server.enable_job('emppty_copy')
# try:
#     server.reconfig_job('emppty_copy',jenkins.RECONFIG_XML)
# except Exception as e:
#     print(e)
#     pass
#删除job
# server.delete_job('empty')
# server.delete_job('empty_copy')
#传入参数构建
# server.build_job('api-test',{'param1':'test value 1','param2':'test value 2'})
# last_build_number = server.get_job_info('api-test')['lastCompletedBuild']['number']
# build_info = server.get_build_info('api-test',last_build_number)
# print(build_info)
#查看job 相关信息
jobs = server.get_jobs(view_name='View Name')
print(jobs)