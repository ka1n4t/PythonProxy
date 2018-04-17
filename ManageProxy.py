#!/usr/bin/env python3

import re, os, requests, linecache
from UtilFunction import checkIpValid

class ManageProxy:
	
	
	def __init__(self):
		pass
	
	def checkAll(self):
		#获取从文件中一条数据
		filename = 'ip.txt'
		file = open(filename, 'rb+')
		lineNum = 1
		#data = linecache.getline(filename, lineNum)
		file.seek(0)
		data = file.readline().decode('utf-8')
		while( data != ''):
			#未到最后一行，读取数据，并check
			#TODO: 使用多线程
			data = self.checkProxyValid(data)
			#TODO: 写入日志
			#print(data)
			
			#将相应行替换
			file.seek(file.tell()-3)
			file.write(bytes(str(data), 'utf-8'))
			file.seek(file.tell()+2)
			
			lineNum += 1
			data = file.readline().decode('utf-8')
			#data = linecache.getline(filename, lineNum)
		lineNum -= 1
		file.close()
		exit()
		
		
	
	def checkProxyValid(self, proxy):
		#检查代理是否有效，若无效则在相应记录后的标志位置为0，返回修改后的字符串
		#proxy = '27.40.137.108 61234 HTTP 1'
		#pattern = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s(\d{1,5})\s(\w{1,5})\s(\d)', re.S)
		#item = re.findall(pattern, proxy)
		item = proxy.split(' ')
		ip = item[0]
		port = item[1]
		protocol = item[2].lower()
		flag = item[3][0:1]
		if(not checkIpValid(ip, port, protocol)):
			#ip无效，将flag+1或-1
			if(flag == 0):
				flag = 2
			else:
				flag = int(flag) + 1
			if(flag > 5):
				#flag>5则直接删除此条记录，即flag置为-1
				flag = -1
			proxy = ip+" "+port+" "+protocol+" "+str(flag)
		else:
			flag = 1
		return flag
		
		
	def delete(self):
	#删除相应行的记录
		pass
		
if __name__ == '__main__':
	obj = ManageProxy()
	item = '27.40.137.108 61234 HTTP 1'
	item = '218.72.108.38 18118 HTTP 1'
	obj.checkAll()
	#obj.checkProxyValid(item)
	#print(obj.getOne())