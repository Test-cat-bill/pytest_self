# 接口信息：
# 验证码：
# 地址：http://kdtx-test.itheima.net/api/captchaImage
# 方法：get
#
# 登录：
# 地址：http://kdtx-test.itheima.net/api/login
# 方法：Post
# 请求数据：
# 请求头：Content-Type: application/json
# 请求体：{"username":”admin", "password": " HM_2023_test","code":"2", "uuid":"验证码接口返回数据"}
#

# 接口封装时，重点是依据接口文档封装接口信息，需要使用的测试数据是从测试用例传递的、接口方法被调用时需要返回对应的响应结果
import requests
import config

class LoginAPI:
    def __init__(self):
        # self.verify_url = "http://kdtx-test.itheima.net/api/captchaImage"
        # self.login_url = "http://kdtx-test.itheima.net/api/login"

        self.verify_url = config.BASE_URL+"/api/captchaImage"
        self.login_url = config.BASE_URL+"/api/login"

    def verify_code(self):
        return requests.get(url=self.verify_url)

    def login(self, test_data):
        return requests.post(url=self.login_url,json=test_data)
