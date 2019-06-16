# coding:utf-8


import jenkins

#连接
def connet_jenkinsjob(self):  # 连接Jenkins
    server = Jenkins(jenkins_url, username=jenkins_user, password=jenkins_password,
                     requester=CrumbRequester(username=jenkins_user, password=jenkins_password,
                                              baseurl=jenkins_url))
    return server


def stats_jenkinsjob(self):  # 连接Jenkins
    server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_password)
    return server


def bulids_job(self):
    global get_number2
    server = self.stats_jenkinsjob()
    server_build = self.connet_jenkinsjob()
        server_build.build_job(jobname, params=param_dict)  # 待观察这个问题有解决方案不  进行项目的编译
            sql = "update auto_caseList  SET runStart='运行中' WHERE id= '" + key + "'""
            try:
                get_number2 = server.get_job_info(jobname)['nextBuildNumber']  # 获取下一个编译版本号
                get_number = server.get_job_info(jobname)['lastBuild']['number']  # 获取编译的版本号
            except Exception, e:
                print("首次创建所以获取不到编译的版本号", e)
                self.mysql_uptate_operation(sql)
            else:
                get_buildstats = server.get_build_info(jobname, get_number)['building']  # 获取编译的状态，是否在编译
                if get_buildstats == False:
                    print("编译中，数据状态进行更新")
                else:
                    print("没有编译")
            finally:
                sleep(23)  # 一定要加，在启动编译后，不能马上获取编译状态，不然一直是编译成功，如果Jenkins编译失败是会在20-23S之间
                status = server.get_build_info(jobname, get_number2)['result']  # 获取编译的状态，编译是否成功，如果不成功，就会返回FAILURE，编译成功是返回NONE
                if status == "FAILURE":
                    print
                    "构建出错: %s | 构建项目编号:%s" % (jobname, get_number2)
                    sql = "update auto_caseList  SET runStart='构建出错' WHERE id= '" + key + "'""
                    self.mysql_uptate_operation(sql)
                else:
                    print
                    "构建成功:%s | 构建项目编号:%s" % (jobname, get_number2)