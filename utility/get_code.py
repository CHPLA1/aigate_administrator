# encoding:utf-8
import requests
import base64
from PIL import Image
import  time

class GetCode:
    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, file_name):
        # 获取验证码图片
        self.driver.save_screenshot(file_name)  # 截图为取验证码使用
        code_element = self.driver.find_element_by_class_name('login-rcg')  # 获取验证码的区域
        left = code_element.location['x'] + 250
        top = code_element.location['y'] + 100
        right = code_element.size['width'] + left + 20
        height = code_element.size['height'] + top + 20
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        time.sleep(2)

    def turnText(self, file_name):
        self.screenshot(file_name)
        #  将图片识别为文本
        with open("%s" % file_name, "rb") as f:

            # b64encode是编码，b64decode是解码
            base64_data = str(base64.b64encode(f.read()))  # 将图片转为base64   turnText
            ima = base64_data.lstrip('b').strip("''")

        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = ('https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&'
                'client_id=MfNXwlPwu79kdOaChQuGLw4d&client_secret=icEaa545U8HUkXxqqaGOFUKfE6nTAVG7')
        response = requests.get(host)
        access_token = str(response.json()["access_token"])  # 将登录后的token提取出来
        # 识别验证码接口
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=%s' % access_token
        data = {
            'image': '%s' % ima
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url=url, data=data, headers=headers)
        words = str(response.json()["words_result"][0]["words"]).replace(" ", "")  # 将文字提取出来
        time.sleep(2)
        return words







if __name__=='__main__':
    get_code = GetCode()
    print(get_code.turnText("E:\\imooc1.png"))