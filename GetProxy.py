#!/usr/bin/env python3
import requests, re, os

class GetProxy:
	
	url = 'http://www.xicidaili.com/nn/'
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
	ip = []
	page = 1
	
	def __init__(self):
		self.getPage()
	
	def getPage(self):#pageNum爬取的页数
	#爬取指定页数的页面
		#text="<tr><td></td><td>ip</td><td>port</td><td><a></td><td></td><td>http</td>"
		pattern = re.compile('<tr.*?\/td>.*?<td>(.*?)<\/td>.*?<td>(.*?)<\/td>.*?<td>.*?<\/td>.*?<td>(.*?)<\/td>', re.S)
		#print(re.findall(pattern, text))
		#exit()
		i = 1
		while(i <= self.page):
			req = requests.get(self.url+str(i), headers=self.headers)
			content = req.content.decode('utf-8')
			self.getIp(content, pattern)
			i+=1
			
	def getIp(self, html, pattern):
	#用正则获取页面中的IP地址
		item = re.findall(pattern, html)
		self.ip.append(item)
		
	def getOne(self):
	#获取一条数据
	#在ManageProxy中管理
		pass
		
	def showIp(self):
	#显示已爬到的IP地址
		print(self.ip)
		
	def save(self, save_name):
	#保存ip到文件
		cur_dir = os.getcwd() #当前路径
		fullname = cur_dir+'\\'+save_name
		with open(fullname, 'w+', encoding='utf-8') as file:
			for value in self.ip[0]:
				file.write(value[0]+' '+value[1]+' '+value[2]+' 0'+'\n') #0为标志位，新增ip标志为0，每次检查后，若成功则置为1，若失败则置为2。下一次，若失败则置为3，到5则直接置为-1，即下次不会再检测
	
	def checkValid(self):
	#检验代理是否有效
		pass
		
		