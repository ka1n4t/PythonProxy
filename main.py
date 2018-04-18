#!/usr/bin/env python3
from Schedule import run as ScheduleRun
from ProxyApi import run as ApiRun
from multiprocessing import Process

def run():
	p_list = list()
	p1 = Process(target=ScheduleRun, name='ScheduleRun')
	p_list.append(p1)
	p2 = Process(target=ApiRun, name='ApiRun')
	p_list.append(p2)
	
	for p in p_list:
		p.daemon = True
		p.start()
	for p in p_list:
		p.join()

if __name__ == '__main__':
	run()
	
	