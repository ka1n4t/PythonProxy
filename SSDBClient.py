import redis

class SSDBClient:
	
	def __init__(self, name):
		self.tablename = name
		pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True) #连接池
		self.db=  redis.Redis(connection_pool=pool) #使用连接池
		
	#添加一条记录
	def put(self, key, value):
		self.db.hset(self.tablename, key, value)

	#返回所有记录
	def getAll(self):
		return self.db.hgetall(self.tablename)
		
	#查询一条记录
	def get(self, key):
		self.db.hget(self.tablename, key)
	
	#删除一条记录
	def delete(self, tablename, key):
		return self.db.hdel(tablename, key)
		
	#修改一条记录
	def update(self, tablename, key, value):
		return self.db.hset(tablename, key, value)
	
	#按序弹出记录
	def pop(self, tablename):
		pass
	
	#返回当前表名
	def getTableName(self):
		return self.tablename
	
	def isKeyExists(self, keyname):
		return self.db.hexists(name=self.tablename, key=keyname)
	
	#修改表名
	def changeTable(self, tablename):
		self.tablename = tablename
	
if __name__ == '__main__':
	#test
	db = SSDBClient()
	db.set('1.1.1.1:999')