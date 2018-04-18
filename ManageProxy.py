#!/usr/bin/env python3

import re, os, requests, linecache, threading, time
from UtilFunction import checkIpValid
from GetProxy import GetProxy

# 对已存储的代理进行增加、验证可用性、获取
class ManageProxy:
	
	filename = 'ip.txt'
	
	def __init__(self):
		self.getProxy()
	
	#首次运行，存储代理
	def getProxy(self):
		file = open(self.filename, 'a+')
		file.seek(0)
		data = file.readlines()
		if(data == []):
			obj = GetProxy()
			obj.getPage()
			obj.save()
	
	#添加新代理，不能有重复
	def refreshProxy(self):
		#TODO 写入日志
		print('{} start refresh...'.format(time.strftime("%Y-%m-%d %H:%M:%S")))
		obj = GetProxy()
		obj.getPage()
		new_ip = [] # 无重复的ip
		raw_ip = obj.ip
		old_ip = self.getAllProxy()
		for item in raw_ip:
			data = item[0]+" "+item[1]+" "+item[2]
			if(data not in old_ip):
				#数据不存在，需要保存到文件中
				new_ip.append(data)
		
		file = open(self.filename, 'a+')
		for data in new_ip:
			file.write(data+" 0\n")
		file.close()
			
	#获取文件中的所有内容，返回一个list(仅包含ip和port和protocol)
	def getAllProxy(self):
		file = open(self.filename, 'r+')
		file.seek(0)
		ip = []
		pattern = ''
		data = file.readline()
		while(data != ''):
			item = data.split(' ')
			ip.append('{} {} {}'.format(item[0], item[1], item[2]))
			data = file.readline()
		file.close()
		return ip

	#检验代理可用性
	def checkAll(self, speed=30):
		print('{} start check...'.format(time.strftime("%Y-%m-%d %H:%M:%S")))
		global file, lock 
		file = open(self.filename, 'rb+')
		
		lock = threading.Lock()
		thread_list = []
		
		file.seek(0)
		
		for i in range(speed):
			t = threading.Thread(target=self.doCheck)
			thread_list.append(t)
		
		for t in thread_list:
			t.setDaemon(True)
			t.start()
		
		for t in thread_list:
			t.join()

		file.close()
		return 
		
	#从读一条数据到写入一条数据的一个完整的操作 IMPORTANT
	def doCheck(self):
		global lock, file
		#将file锁住，防止游标误移
		lock.acquire()
		data = file.readline().decode('utf-8')
		#获取游标当前位置
		cur_loc = file.tell()
		lock.release()
		#到文件结尾就return
		if(data == ''):
			return
		
		flag = self.checkItemValid(data)
		#TODO: 写入日志
		#print(">> "+data+" -> "+str(flag))
		
		#将相应行的flag更新
		#再次上锁，因为上面的checkItemValid才是真正应该多线程处理的地方
		#而这里的文件操作的游标会乱移
		#所以只能手动保存现场
		#如果把checkItemValid包含在上锁的过程中的话会严重影响速度
		#因为每个时刻只能有一个线程读文件并checkItemValid
		lock.acquire()
		loc = file.tell()
		file.seek(cur_loc)
		file.seek(file.tell()-3)
		file.write(bytes(str(flag), 'utf-8'))
		file.seek(loc)
		lock.release()
		
		#递归
		self.doCheck()
	
	#检查单条代理记录是否有效，若无效则在相应记录后的标志位+1或置为-1，返回flag
	def checkItemValid(self, proxy):		
		item = proxy.split(' ')
		ip = item[0]
		port = item[1]
		protocol = item[2].lower()
		flag = item[3][0:1]
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
		
	#获得所有可用代理(flag==1)
	def getValidProxy(self):
		file = open(self.filename, 'rb+')
		valid_proxy = []
		file.seek(0)
		data = file.readline().decode('utf-8')
		while(data != ''):
			flag = data[::-1][2:3]
			if(flag == '1'):
				#有效，放入list中
				valid_proxy.append(data)
			data = file.readline().decode('utf-8')
		file.close()
		return valid_proxy
		
	#删除相应行的记录
	def delete(self):
		#可直接将flag位设置为5
		pass
		
if __name__ == '__main__':
	obj = ManageProxy()
	item = '27.40.137.108 61234 HTTP 1'
	item = '218.72.108.38 18118 HTTP 1'
	#obj.getProxy()