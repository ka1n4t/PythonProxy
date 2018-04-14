#!/usr/bin/env python3
import requests, re

class Xici:
	
	url = 'http://www.xicidaili.com/nn/'
	headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}
	ip = []
	page = 1
	
	def __init__(self):
		self.getPage()
	
	def getPage(self):#pageNum爬取的页数
	#爬取指定页数的页面
		pattern = re.compile('<tr.*?>.*?<td.*?>.*?<\/td>.*?<td>(.*?)<\/td>.*?<td>(.*?)<\/td>', re.S)
		i = 1
		while(i <= self.page):
			req = requests.get(self.url+str(i), headers=self.headers)
			content = req.content.decode('utf-8')
			self.getIp(content, pattern)
			i+=1
			
	def getIp(self, html, pattern):
	#用正则获取页面中的IP地址
		item = re.findall(pattern, html)
		#ip = item[0][0]
		#port = item[0][1]
		self.ip.append(item)
		
	def showIp(self):
	#显示已爬到的IP地址
		print(self.ip)
		
	def checkValid(self):
	#检验代理是否有效
		pass
		
		