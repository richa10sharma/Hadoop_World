#!/usr/bin/python
import os
fp3 = open("/etc/hadoop/hdfs-site.xml","w+")
fp3.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/haa</value>\n</property>\n</configuration>')
fp3.close()
fp4 = open("/etc/hadoop/core-site.xml","w+")
fp4.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://192.168.43.150:9001</value>\n</property>\n</configuration>')
fp4.close()
os.system("hadoop-daemon.sh start datanode")
os.system("/usr/java/jdk1.7.0_79/bin/jps")
