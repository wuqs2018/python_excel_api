import xlrd
from xlutils.copy import copy
import sys
import os

class OperationExcel:

	def __init__(self, file_name=None, sheet_id=None):
		if file_name:
			self.file_name = file_name
			self.sheet_id = sheet_id
		else:
			curPath = os.path.abspath(os.path.dirname(__file__))
			rootPath = os.path.split(curPath)[0]
			self.file_name = rootPath + '/util/word.xls'
			self.sheet_id = 0
		self.num = 0
		self.data = self.get_data()
		
	#获取表格信息
	def get_data(self):
		data = xlrd.open_workbook(self.file_name)
		tables = data.sheets()[self.sheet_id]
		return tables

	#获取单元的行数
	def get_lines(self):
		tables = self.data
		return tables.nrows
	
	#根据字段获取单元行数
	def get_cell_row(self, case_name):
		case_col = self.data.col_values(self.num)
		col = None
		if case_name:
			case_name = str(case_name)
			col = case_col.index(case_name)
		return col

	#重新读取Excel表中数据
	def get_value(self, row, col):
		data = xlrd.open_workbook(self.file_name)
		read_data = data.sheets()[self.num]
		return read_data.cell_value(row, col)

	#获取某一个单元格的内容
	def get_cell_value(self,row, col):
		return self.data.cell_value(row, col)

	#写入数据
	def write_value(self, row, col, value):
		read_data = xlrd.open_workbook(self.file_name)
		write_data = copy(read_data)
		sheet_data = write_data.get_sheet(self.num)
		sheet_data.write(row, col, value)
		write_data.save(self.file_name)