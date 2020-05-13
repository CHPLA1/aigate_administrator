from aigate_login.business.login_business import LoginBusiness
from selenium import webdriver
import time
import unittest
import HTMLTestRunner
import os
from aigate_login.log.user_log import UserLog
log = UserLog()
logger = log.get_log()


class FirstCase(unittest.TestCase):

    def setUp(self):
        self.driver = self.get_driver('https://www.aigates.cn/v3/')
        self.login = LoginBusiness(self.driver)
        logger.debug('this is chrome')
        self.file_name = 'E:/code/PyChram_python/aigate_login/report/test001.png'

    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
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

    def test_login_username_error(self):
        username_error = self.login.login_username_error('jstsign1', 'shone19861205', self.file_name)
        self.assertFalse(username_error, '输入失败了，此条case成功了------1')
        # if username_error:
        #     # print("登录成功了，此条case失败了")
        #     print("登录失败了，此条case成功了------1")
        # else:
        #     print("用户名输入正确")

    def test_login_password_error(self):
        password_error = self.login.login_password_error('jstsign', '', self.file_name)
        self.assertFalse(password_error, '登录失败了，此条case成功了------2')
        # if password_error:
        #     # print("登录成功了，此条case失败了")
        #     print("登录失败了，此条case成功了------2")

    def test_login_inputcode_error(self):
        inputcode_error = self.login.login_inputcode_error('jstsign', 'shone19861205', self.file_name)
        self.assertFalse(inputcode_error, '验证码输入失败，此条case成功了------3')



'''
def main():
    fist = FirstCase('https://www.aigates.cn/v3/')
    fist.test_login_username_error()
    time.sleep(5)
    fist.driver.close()
    # fist.test_login_password_error()
    # fist.test_login_inputcode_error()
'''

if __name__ == '__main__':
    path = os.path.abspath(os.path.join(os.getcwd(), ".."))  # 获取当前层级的上级目录
    file_path = os.path.join(path+'\\report\\'+'first_case.html')  # 获取测试报告所在的文件目录
    # file_path = os.path.join(os.getcwd(), ".."+'\\report\\'+'first_case.html')
    f = open(file_path, 'wb')  # 打开文件进行读写
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_username_error'))
    # suite.addTest(FirstCase('test_login_password_error'))
    # suite.addTest(FirstCase('test_login_inputcode_error'))
    # unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='This is first report', description=u'这是我们第一次测试报告',
                                           verbosity=2)
    runner.run(suite)

