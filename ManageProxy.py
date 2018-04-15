#!/usr/bin/env python3

import re, os, requests
from UtilFunction import checkIpValid

class ManageProxy:
	
	def __init__(self):
		pass
	
	def findOne(self):
		#获取从文件中一条数据
		pass
	
	def checkValid(self, proxy):
	#检查代理是否有效，若无效则在相应记录后的标志位置为0
		pattern = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s(\d{1,5})\s(\w{1,5})\s', re.S)
		item = re.findall(pattern, proxy)
		ip = item[0][0]
		port = item[0][1]
		protocol = item[0][2].lower()
		if(checkIpValid(ip, port, protocol)):
			print("valid")
		else:
			print("invalid")
		
		
	def delete(self):
	#删除相应行的记录
		pass
		
if __name__ == '__main__':
	obj = ManageProxy()
	item = '27.40.137.108 61234 HTTP 1'
	item = '218.72.108.38 18118 HTTP 1'
	obj.checkValid(item)