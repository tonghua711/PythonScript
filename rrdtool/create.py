# coding:utf-8
#!/usr/bin/python

import rrdtool
import time

cur_time=str(int(time.time()))
rrd=rrdtool.create