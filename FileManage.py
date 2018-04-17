#!/usr/bin/env python3

import os

class FileManage:
	
	filename = ''
	
	def __init__(self, filename, type='a'):
		self::file = open(filename, type, encoding'utf-8')
		
		
	def getNext(self, line=''):
		#获取文件下一行
		return self::file.__next__()
		
			
	def writeData(self, data):
		#以追加模式写入
		
		
		