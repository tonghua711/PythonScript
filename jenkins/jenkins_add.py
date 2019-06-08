# coding: utf-8

import jenkins

#登陆Jenkins
server = jenkins.Jenkins('http://192.168.204.128:8080',username='administrator',password='888888')
# view_config = server.get_view_config('View Name')
# view = server.get_views()
# server.delete_view('EMPTY')
# print(view)

#######################
# plugins = server.get_plugin_info('jenkins')
# print(plugins)
#************************
