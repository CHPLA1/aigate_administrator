from aigate_login.business.login_business import LoginBusiness
from aigate_login.utility.excel_util import ExcelUtil
from selenium import webdriver
import time
import unittest
import HTMLTestRunner
import os
import ddt
# 获取数据
data = ExcelUtil().get_data()


@ddt.ddt
class LoginDdtCase(unittest.TestCase):

    def setUp(self):
        self.driver = self.get_driver('https://www.aigates.cn/v3/')
        self.login = LoginBusiness(self.driver)
        self.file_name = 'E:/code/PyChram_python/aigate_login/report/test001.png'

    def tearDown(self):
        time.sleep(2)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                path = os.path.abspath(os.path.join(os.getcwd(), ".."))  # 获取当前层级的上级目录
                file_path = os.path.join(path + '\\report\\' +case_name+'.png')  # 获取测试报告所在的文件目录
                self.driver.save_screenshot(file_path)
        self.driver.close()

    def get_driver(self, url):
        driver = webdriver.Chrome()
        driver.maximize_window()  # 将浏览器最大化
        driver.get(url)  # 打开网页
        return driver

    @ddt.data(*data)
    def test_login_case(self, data):
        username, password, code, assertCode, assertText = data
        # 判断用户名的case
        username_error = self.login.login_function(username, password, code, assertCode, assertText)
        self.assertFalse(username_error, '测试失败')


if __name__ == '__main__':
    path = os.path.abspath(os.path.join(os.getcwd(), ".."))  # 获取当前层级的上级目录
    file_path = os.path.join(path + '/report/' + 'login_ddt_case.html')  # 获取测试报告所在的文件目录
    print(file_path)
    f = open(file_path, 'wb')  # 打开文件进行读写
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='This is first report', description=u'这是我们第一次测试报告',
                                           verbosity=2)
    runner.run(suite)
