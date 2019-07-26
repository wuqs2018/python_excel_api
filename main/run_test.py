import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import json
from base.runMethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from util.send_email import SendEmail

class RunTest:
	def __init__(self):
		self.run_method = RunMethod()
		self.data = GetData()
		self.common_util = CommonUtil()
		self.send_email = SendEmail()

	def go_on_run(self):
		res = None
		pass_count = []
		fail_count = []
		rows_count = self.data.get_case_lines()
		for i in range(1, rows_count):
			url = self.data.get_request_url(i)
			method = self.data.get_request_method(i)
			is_run = self.data.get_is_run(i)
			data = self.data.get_data_for_json(i)
			expect = self.data.get_expcet_data(i)
			header = self.data.is_header(i)
			case_depend = self.data.get_case_depend(i)
			if case_depend:
				case_depend = "'" + str(case_depend) + "'"
				jsontodata = str(data).replace("'@@@'", case_depend)
				jsontodata = jsontodata.replace("'", '"')
				data = json.loads(jsontodata)
				
			if is_run:
				res = self.run_method.run_main(method, url, data, header)
				if self.common_util.is_contain(expect, res):
					self.data.write_status(i, 'pass')
					pass_count.append(i)
				else:
					self.data.write_status(i, 'fail')
					fail_count.append(i)
				self.data.write_res(i, res)
				
		# self.send_email.send_main(pass_count, fail_count)

if __name__ == '__main__':
	run = RunTest()
	print(run.go_on_run())

