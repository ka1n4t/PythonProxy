#!/usr/bin/env python3

import re, os, requests, linecache, threading, time
from UtilFunction import checkIpValid
from GetProxy import GetProxy
from random import choice
from DBClient import DBClient

# 对已存储的代理进行增加、验证可用性、获取
class ManageProxy:
	
	def __init__(self):
		obj =  GetProxy()
		obj.getPage()
		obj.save()
		self.db = DBClient()
		self.nextline = 0
	
	#添加新代理
	def refreshProxy(self):
		#TODO 写入日志
		print('{} start refresh...'.format(time.strftime("%Y-%m-%d %H:%M:%S")))
		obj = GetProxy()
		obj.getPage()
		obj.save()

			
	#获取raw_proxy中的所有内容，返回一个list(仅包含ip和port和protocol)
	def getAllRawProxy(self):
		self.db.changeTable('raw_proxy')
		ip = self.db.getAll()
		return ip

	def getAllVerifiedProxy(self):
		self.db.changeTable('verified_proxy')
		ip = self.db.getAll()
		return ip
		
	#检验代理可用性
	def checkAll(self, speed=30):
		print('{} start check...'.format(time.strftime("%Y-%m-%d %H:%M:%S")))
		
		raw_proxy = self.getAllRawProxy()
		verified_proxy = self.getAllVerifiedProxy()
		
		thread_list = []
		#多线程
		for i in range(speed):
			t = threading.Thread(target=self.doCheck)
			thread_list.append(t)
		
		for t in thread_list:
			t.setDaemon(True)
			t.start()
		
		for t in thread_list:
			t.join()

		print('{} end check...'.format(time.strftime("%Y-%m-%d %H:%M:%S")))
		return 
		
	#从读一条数据到写入一条数据的一个完整的操作
	def doCheck(self):
		
		global lock
		lock = threading.Lock()
		
		data = self.getNextLine()
		if(data == ''):
			return
			
		proxy = data.split(' ')[0]
		flag = data.split(' ')[1]
		raw_proxy = self.getAllRawProxy()
		
		if(not raw_proxy[proxy]):
			#raw_proxy中没有对应的记录，删除verified_proxy中的此项记录
			self.doCheck()
			
		protocol = raw_proxy[proxy].lower()
		flag = self.checkProxyValid(proxy, protocol, flag)
		#更新proxy对应的flag值
		self.db.update('verified_proxy', proxy, flag)
		
		self.doCheck()
		
	
	#检查单条代理记录是否有效，若无效则修改verified_proxy，将对应key的flag+1或置为-1
	def checkProxyValid(self, proxy, protocol='http' ,flag=0):
		ip = proxy.split(':')[0]
		port = proxy.split(':')[1]
		flag = int(flag)
		
		if(not checkIpValid(ip, port, protocol)):
			#ip无效，将flag+1
			if(flag == 0):
				flag = 2
			elif(flag < 5):
				flag += 1
		else:
			flag = 1	
		flag = str(flag)
		return flag

	def getNextLine(self):
		global lock
		verified_proxy = self.getAllVerifiedProxy()
		
		index = 0
		
		lock.acquire()
		cur = self.nextline
		self.nextline = self.nextline + 1
		lock.release()
		
		for key, value in verified_proxy.items():
			if(index == cur):
				break
			index = index + 1
		if(index == len(verified_proxy)):
			return ''
		else:
			return key+' '+value
		
	#获得所有可用代理(flag==1)
	def getValidProxy(self):
		verified_proxy = self.getAllVerifiedProxy()
		valid_proxy = []
		
		for key, value in verified_proxy.items():
			if(value == '1'):
				valid_proxy.append(key)

		return valid_proxy
	
	def getRandomValidProxy(self):
		return choice(self.getValidProxy())


		
if __name__ == '__main__':
	obj = ManageProxy()
	obj.getRandomValidProxy()
	#item = '27.40.137.108 61234 HTTP 1'
	#item = '218.72.108.38 18118 HTTP 1'
	#obj.getProxy()