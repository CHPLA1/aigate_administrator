from aigate_login.base.find_element import FindElement


class LoginPage(object):
    def __init__(self, driver):
        self.find_element = FindElement(driver)

    # 获取用户名
    def get_username_element(self):
        return self.find_element.get_element('username')

    # 获取密码
    def get_password_element(self):
        return self.find_element.get_element('password')

    # 获取验证码输入框
    def get_inputcode_element(self):
        return self.find_element.get_element('inputcode')

    # 获取验证码区域
    def get_login_rcg_element(self):
        return self.find_element.get_element('login_rcg')

    # 获取账号的错误文本
    def get_username_error_element(self):
        return self.find_element.get_element('username_error')

    # 获取密码的错误文本
    def get_password_error_element(self):
        return self.find_element.get_element('password_error')

    # 获取验证码的错误文本
    def get_inputcode_error_element(self):
        return self.find_element.get_element('inputcode_error')

    # 获取登录按钮
    def get_login_button_element(self):
        return self.find_element.get_element('login_button')
