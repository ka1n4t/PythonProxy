#!/usr/bin/env python3
import requests, re, os

# 获取新代理类
class GetProxy:
	
	url = 'http://www.xicidaili.com/nn/'
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
	ip = []
	page = 1 #爬取的页数
	
	def __init__(self):
		pass
		
	#爬取西刺的页面
	def getPage(self):
		pattern = re.compile('<tr.*?\/td>.*?<td>(.*?)<\/td>.*?<td>(.*?)<\/td>.*?<td>.*?<\/td>.*?<td>(.*?)<\/td>', re.S)
		i = 1
		while(i <= self.page):
			req = requests.get(self.url+str(i), headers=self.headers)
			content = req.content.decode('utf-8')
			self.crawlIp(content, pattern)
			i+=1
			
	#用正则获取页面中的IP地址
	def crawlIp(self, html, pattern):
		item = re.findall(pattern, html)
		self.ip = item
		
	#保存ip到文件
	def save(self, save_name='ip.txt'):
		cur_dir = os.getcwd() #当前路径
		fullname = cur_dir+'\\'+save_name
		with open(fullname, 'a+', encoding='utf-8') as file:
			for value in self.ip:
				file.write(value[0]+' '+value[1]+' '+value[2]+' 0'+'\n') #0为标志位，新增ip标志为0，每次检查后，若成功则置为1，若失败则置为2。下一次，若失败则置为3，最大为5
	

		
		