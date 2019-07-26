from util.operation_excel import OperationExcel
from util.operation_json import OperationJson
import sys
import os
import json
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
rootPath = rootPath + '/data/'
sys.path.append(rootPath)
import data_config


class  GetData:
	def __init__(self):
		self.opera_excel = OperationExcel()
		self.opera_json = OperationJson()

	#获取excel行数，
	def get_case_lines(self):
		return self.opera_excel.get_lines()

	#获取是否执行
	def get_is_run(self, row):
		flag = None
		col = int(data_config.get_run())
		run_model = self.opera_excel.get_cell_value(row, col)
		if run_model == 'yes':
			flag = True
		else:
			flag = False
		return flag

	#是否携带hearder
	def is_header(self, row):
		col = int(data_config.get_header())
		header = self.opera_excel.get_cell_value(row, col)
		if header == 'yes':
			headerJson = data_config.get_header_value()
			return headerJson
		else:
			return None

	#获取请求方式
	def get_request_method(self,row):
		col = int(data_config.get_run_way())
		request_method = self.opera_excel.get_cell_value(row,col)
		return request_method

	#获取url
	def get_request_url(self, row):
		col = int(data_config.get_url())
		url = self.opera_excel.get_cell_value(row, col)
		return url

	#获取请求数据
	def get_request_data(self, row):
		col = int(data_config.get_data())
		data = self.opera_excel.get_cell_value(row, col)
		if data == '':
			return None
		return data

	#通过获取关键字拿到data数据
	def get_data_for_json(self, row):
		res = self.get_request_data(row)
		request_data = self.opera_json.get_data(res)
		return request_data

	#获取预期结果
	def get_expcet_data(self, row):
		col = int(data_config.get_expect())
		expect = self.opera_excel.get_cell_value(row, col)
		if expect == '':
			return None
		else:
			return expect

	#结果写入
	def write_res(self, row, value):
		col = int(data_config.get_result_value())
		self.opera_excel.write_value(row, col, value)
	
	#状态写入
	def write_status(self, row, value):
		col = int(data_config.get_result())
		self.opera_excel.write_value(row, col, value)
	
	def get_case_depend(self, row):
		case_col = int(data_config.get_case_depend())
		case = self.opera_excel.get_cell_value(row, case_col)
		rowRes = self.opera_excel.get_cell_row(case)
		res = None
		if rowRes:
			result_col = int(data_config.get_result_value())
			resData = self.opera_excel.get_value(rowRes, result_col)
			if resData:
				resData = json.loads(resData)
				data_col = int(data_config.get_data_depend())
				data = self.opera_excel.get_cell_value(row, data_col)
				field_col = int(data_config.get_field_depend())
				field = self.opera_excel.get_cell_value(row, field_col)
				if field:
					res = resData[data][field]
				else:
					res = resData[data]
		return res

