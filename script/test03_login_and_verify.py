"""
登录测试
"""
from api.login import LoginAPI


class TestLoginAPI:
    uuid = None

    def setup(self):
        self.login_api = LoginAPI()
        response = self.login_api.verify_code()
        TestLoginAPI.uuid = response.json().get("uuid")

    def teardown(self):
        pass

    def test01_success(self):
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data=login_data)
        print(response.json())
        assert response.status_code == 200
        assert '成功' in response.text
        assert '成功' in response.json().get("msg")
        assert 200 == response.json().get("code")

    # 登录失败（用户名为空）
    def test02_without_username(self):
        login_data = {
            "username": "",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data=login_data)
        print(response.json())
        # 断言响应状态码为200
        assert 200 == response.status_code
        # 断言响应数据包含'错误'
        assert '错误' in response.text
        # 断言响应json数据中code值
        assert 500 == response.json().get("code")

    # 登录失败（未注册用户）
    def test03_username_not_exist(self):
        login_data = {
            "username": "jack66796",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response = self.login_api.login(test_data=login_data)
        print(response.json())
        # 断言响应状态码为200
        assert 200 == response.status_code
        # 断言响应数据包含'错误'
        assert '错误' in response.text
        # 断言响应json数据中code值
        assert 500 == response.json().get("code")
