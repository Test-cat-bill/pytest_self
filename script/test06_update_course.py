from api.login import LoginAPI
from api.course import CourseAPI

class TestCourseAPI:
    TOKEN = None
    def setup(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()

        response = self.login_api.verify_code()
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": response.json().get("uuid")
        }
        res_login = self.login_api.login(test_data=login_data)
        TestCourseAPI.TOKEN = res_login.json().get("token")

    def teardown(self):
        pass

    def test01_update_success(self):
        update_data = {
            "id": 5000,
            "name": "接口测试001001001",
            "subject": "6",
            "price": 999998,
            "applicablePerson": "2",
            "info": "课程介绍000101"
        }
        response = self.course_api.update_course(test_data=update_data, token=TestCourseAPI.TOKEN)
        print(response.json())

        print("status code: ", response.status_code)
        assert response.status_code == 200
        # assert '成功' in response.text
        assert '成功' in response.json().get("msg")
        assert 200 == response.json().get("code")

    def test14_update_fail(self):
        update_data = {
            "id": 5000,
            "name": "接口测试001001001",
            "subject": "6",
            "price": 999998,
            "applicablePerson": "2",
            "info": "课程介绍000101"
        }
        response = self.course_api.update_course(test_data=update_data, token="xxx")
        print(response.json())
        print("status code: ",response.status_code)

        # 断言响应状态码
        assert 200 == response.status_code
        # 断言msg中包含指定的文字
        assert "认证失败" in response.text
        # 断言json返回数据中code值
        assert 401 == response.json().get("code")