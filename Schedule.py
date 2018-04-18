#!/usr/bin/env python3

from apscheduler.schedulers.blocking import BlockingScheduler
from ManageProxy import ManageProxy
import time

# 定时任务类
class Schedule:
	
	def __init__(self):
		pass
	
	#定时检验代理的可用性
	def checkValid(self):
		obj = ManageProxy()
		obj.checkAll()
		
	#定时获取新代理
	def refresh(self):
		obj = ManageProxy()
		obj.refreshProxy()
	
	#执行schedule
	def main(self):
		print('{} Schedule Started'.format(time.strftime("%Y-%m-%d %H:%M:%S")))
		sched = BlockingScheduler()
		# 5min运行一次
		sched.add_job(self.checkValid, 'interval', seconds=60, id='check_valid')
		sched.add_job(self.refresh, 'interval', seconds=60, id='refresh_proxy')
		sched.start()

#执行schedule
def run():
	obj = Schedule()
	obj.main()
		
if __name__ == '__main__':
	obj = Schedule()
	obj.main()
	#obj.checkValid()
	#obj.refresh()
	#print('{} Schedule Ended'.format(time.strftime("%Y-%m-%d %H:%M:%S")))