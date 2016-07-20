#!/usr/bin/python
import os
fp = open("/etc/hadoop/mapred-site.xml","w+")
fp.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>192.168.43.160:9002</value>\n</property>\n</configuration>')
fp.close()
os.system("hadoop-daemon.sh start tasktracker")
os.system("/usr/java/jdk1.7.0_79/bin/jps")
