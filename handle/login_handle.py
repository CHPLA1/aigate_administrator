from aigate_login.page.login_page import LoginPage
from aigate_login.utility.get_code import GetCode


class LoginHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.login_p = LoginPage(self.driver)

    # 输入用户名
    def send_username(self, usernamne):
        self.login_p.get_username_element().send_keys(usernamne)

    # 输入密码
    def send_password(self, password):
        self.login_p.get_password_element().send_keys(password)

    # 输入验证码
    def send_inputcode(self, file_name):
        get_code_text = GetCode(self.driver)
        code = get_code_text.turnText(file_name)
        self.login_p.get_inputcode_element().send_keys(code)

    # 获取用户文字信息
    def get_user_text(self, info, user_info):
        try:
            if info == 'username_error':
                # text = self.login_p.get_username_error_element().get_attribute('value')
                text = self.login_p.get_username_error_element().text
            elif info == 'password_error':
                # text = self.login_p.get_password_error_element().get_attribute('value')
                text = self.login_p.get_password_error_element().text
            else:
                # text = self.login_p.get_inputcode_error_element().get_attribute('value')
                text = self.login_p.get_inputcode_error_element().text
        except:
            text = None

        return text

    # 点击登录按钮
    def click_login_button(self):
        self.login_p.get_login_button_element().click()
