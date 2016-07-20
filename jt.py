#!/usr/bin/python
import os
fp = open("/etc/hadoop/mapred-site.xml","w+")
fp.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>hdfs://192.168.43.160:9002</value>\n</property>\n</configuration>')
fp.close()
fp4 = open("/etc/hadoop/core-site.xml","w+")
fp4.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://192.168.43.150:9001</value>\n</property>\n</configuration>')
fp4.close()

os.system("hadoop-daemon.sh start jobtracker")
os.system("/usr/java/jdk1.7.0_79/bin/jps")
