#!/usr/bin/env python3
from GetProxy import GetProxy

if __name__ == '__main__':
	xici = GetProxy()
	xici.showIp()
	xici.save('ip.txt')