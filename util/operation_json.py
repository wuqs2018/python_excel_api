import json
import sys
import os
class OperationJson:
	def __init__(self, file_path=None):
		if file_path == None:
			curPath = os.path.abspath(os.path.dirname(__file__))
			rootPath = os.path.split(curPath)[0]
			self.file_path = rootPath + '/util/data.json'
		else:
			self.file_path = file_path
		self.data = self.read_data()

	#读取json文件
	def read_data(self):
		with open(self.file_path, 'r', encoding='UTF-8') as fp:
			data = json.load(fp)
			return data

	#根据关键字获取数据
	def get_data(self, id):
		return self.data[id]
