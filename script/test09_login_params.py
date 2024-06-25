"""
登录测试
"""
import pytest
import json
from api.login import LoginAPI
import config


# test_data_t =[
#   {
#     "username": "admin",
#     "password": "HM_2023_test",
#     "status": 200,
#     "message": "成功",
#     "code": 200
#   },
#   {
#     "username": "",
#     "password": "123456",
#     "status": 200,
#     "message": "错误",
#     "code": 500
#   },
#   {
#     "username": "jack666",
#     "password": "123456",
#     "status": 200,
#     "message": "错误",
#     "code": 500
#   }
# ]
#
# test_data=[]
# for case_data in test_data_t:
#     # 转换数据格式[{},{}] ==> [(),()]
#     username = case_data.get("username")
#     password = case_data.get("password")
#     status = case_data.get("status")
#     message = case_data.get("message")
#     code = case_data.get("code")
#     test_data.append((username, password, status, message, code))
def build_data(json_file):
    # 定义空列表
    test_data = []
    # 打开json文件
    with open(json_file, "r",encoding="UTF-8") as f:
        # 加载json文件数据
        json_data = json.load(f)
        # 循环遍历测试数据
        for case_data in json_data:
            # 转换数据格式[{},{}] ==> [(),()]
            username = case_data.get("username")
            password = case_data.get("password")
            status = case_data.get("status")
            message = case_data.get("message")
            code = case_data.get("code")
            test_data.append((username, password, status, message, code))
    # 返回处理之后测试数据
    return test_data



class TestLoginAPI:
    uuid = None

    def setup_method(self):
        self.login_api = LoginAPI()

        response = self.login_api.verify_code()
        TestLoginAPI.uuid = response.json().get("uuid")

    def teardown_method(self):
        pass

    # @pytest.mark.parametrize("username, password, status, message, code",test_data)
    @pytest.mark.parametrize("username, password, status, message, code", build_data(json_file=config.BASE_PATH+"/data/login.json"))
    def test01_(self,username, password, status, message, code):
        login_data = {
            "username": username,
            "password": password,
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }

        response = self.login_api.login(test_data=login_data)
        print(response.json())

        # assert response.status_code == status
        # assert message in response.text
        # assert message in response.json().get("msg")
        # assert code == response.json().get("code")

        pytest.assume(response.status_code == status)
        pytest.assume(message in response.text)
        pytest.assume(message in response.json().get("msg"))
        pytest.assume(code == response.json().get("code"))




