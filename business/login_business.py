from aigate_login.handle.login_handle import LoginHandle


class LoginBusiness(object):
    def __init__(self, driver):
        self.login_h = LoginHandle(driver)

    def user_base(self, username, password, code):
        self.login_h.send_username(username)
        self.login_h.send_password(password)
        self.login_h.send_inputcode(code)
        self.login_h.click_login_button()

    def login_function(self, username, password, code, assertCode, assertText):
        self.user_base(username, password, code)
        if self.login_h.get_user_text(assertCode, assertText) == None:
            print('用户名校验不成功')
            return False
        else:
            print('校验成功')
            return True



    # 执行操作
    def login_username_error(self, username, password, file_name):
        self.user_base(username, password, file_name)
        if self.login_h.get_user_text('username_error', '请输入用户名') == None:
            print('用户名校验不成功')
            return False
        else:
            print('用户名校验不成功')
            return True

"""
    def login_password_error(self, username, password, file_name):
        self.user_base(username, password, file_name)
        if self.login_h.get_user_text('password_error', '请输入密码') == None:
            print('密码校验不成功')
            return True
        else:
            return False

    def login_inputcode_error(self, username, password, file_name):
        self.user_base(username, password, file_name)
        if self.login_h.get_user_text('inputcode_error', '验证码不正确') != '验证码不正确':
            print('验证码校验成功')
            return True
        else:
            print('验证码校验失败')
            return False
"""