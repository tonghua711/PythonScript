#coding:utf-8

import filecmp

#定义2个目录
a="E:\\temp\\test\\d1"
b="E:\\temp\\test\\d2"

dirobj = filecmp.dircmp(a,b,['test.py'])

# print(("-"*10).join("报告"))
print(("-"*10) + "报告" + ("-"*10))
dirobj.report()
print(("-"*10) + "报表部分关闭" + ("-"*10))
dirobj.report_partial_closure()
print(("-"*10) + "报表全部打开" + ("-"*10))
dirobj.report_full_closure()
#
print("*"*40)
print("left_list:"+ str(dirobj.left_list))
print("right_list:"+ str(dirobj.right_list))
print("common:"+ str(dirobj.common))
print("left_only:"+ str(dirobj.left_only))
print("right_only:"+ str(dirobj.right_only))
print("common_dirs:"+ str(dirobj.common_dirs))
print("common_files:"+ str(dirobj.common_files))
print("common_funny:"+ str(dirobj.common_funny))
print("same_file:"+ str(dirobj.same_files))
print("diff_files:"+ str(dirobj.diff_files))
print("funny_files:"+ str(dirobj.funny_files))