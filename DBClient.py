from SSDBClient import SSDBClient

# 1. 两个hash：
#   a. raw_proxy 存储原始代理数据，格式为： 1.1.1.1:80 http/https
#   b. verified_proxy 存储验证后的代理，格式为： 1.1.1.1：80 0-5
#
# 2. 如何使用？
#   a. 先在verified_hash中获取一个flag为1（即可用的）的代理
#   b. 再在raw_hash中查找此键，获取代理格式（http/https)

class DBClient:
	
	def __init__(self):
		name = 'raw_proxy'
		self.db = SSDBClient(name)
		
		
	#增加一条代理
	def put(self, proxy, flag=0):
		return self.db.put(proxy, flag)
	
	def getAll(self):
		return self.db.getAll()
	
	def update(self, tablename, key, value):
		return self.db.update(tablename, key, value)
	
	def delete(self, tablename, key):
		return self.db.delete(tablename, key)
	
	#返回hash所有值
	def getAllFromHash(self, tablename):
		self.changeTable(tablename)
		return self.db.getAll()
	
	#更换哈希表
	def changeTable(self, tablename):
		return self.db.changeTable(tablename)
		
	def isKeyExists(self, keyname):
		return self.db.isKeyExists(keyname)
		
if __name__ == '__main__':
	db = DBClient()
	#db.delete('verified_proxy', '58.19.80.227:808')
	#db.update('verified_proxy', '58.19.80.227:808', '5')
	#db.put('2.2.2.2:9999', '5')