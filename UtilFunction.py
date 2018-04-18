#!/usr/bin/env python3
import requests

#检查代理是否有效
def checkIpValid(ip, port, protocol):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
	proxies = {protocol: "{}://{}:{}".format(protocol, ip, port)}
	try:
		req = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
		req_noproxy = requests.get('http://httpbin.org/ip', timeout=5)
		if req.content.decode('utf-8') != req_noproxy.content.decode('utf-8'):
			#代理有效	
			return True
	except Exception as e:
		#代理无效
		return False
