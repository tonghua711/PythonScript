#coding:utf-8
"""
例子添加、配置、启动和删除Jenkins 节点

"""
import jenkins
server = jenkins.Jenkins('http://192.168.204.128:8080',username='administrator',password='888888')
server.create_node('slave1')
nodes = server.get_nodes()
print(nodes)
# node_config = server.get_node_info('slave1')
# print(node_config)
# server.disable_node('slave1')
# server.enable_node('slave1')
#
# # create node with parameters
params = {
    'port': '22',
    'username': 'juser',
    'credentialsId': '10f3a3c8-be35-327e-b60b-a3e5edb0e45f',
    'host': 'my.jenkins.slave1'
}
server.create_node(
    'slave1',
    nodeDescription='my test slave',
    remoteFS='/home/juser',
    labels='precise',
    exclusive=True,
    launcher=jenkins.LAUNCHER_SSH,
    launcher_params=params)