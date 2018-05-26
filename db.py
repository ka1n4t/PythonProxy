from ssdb import SSDBClient


class DBClient:
	
	def __init__(self):
		name = 'raw_proxy'
		self.db = SSDBClient(name)
		
		
	#增加一条代理
	def put(self, proxy, flag=0):
		return self.db.put(proxy, flag)
	
	
	
	def changeTable(self, tablename):
		return self.db.changeTable(tablename)
		
if __name__ == '__main__':
	db = DBClient()
	#db.put('2.2.2.2:9999', '5')