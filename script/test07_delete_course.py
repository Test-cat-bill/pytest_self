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

    def test01_delete_success(self):

        response = self.course_api.delete_course(course_id=5000, token=TestCourseAPI.TOKEN)
        print(response.json())

        print("status code: ", response.status_code)
        assert response.status_code == 200
        # assert '成功' in response.text
        assert '成功' in response.json().get("msg")
        assert 200 == response.json().get("code")

    def test02_delete_fail_no_id(self):

        response = self.course_api.delete_course(course_id=536737, token=TestCourseAPI.TOKEN)
        print(response.json())

        print("status code: ", response.status_code)
        assert response.status_code == 200
        # assert '成功' in response.text
        assert '失败' in response.json().get("msg")
        assert 500 == response.json().get("code")

    def test03_delete_fail(self):
        response = self.course_api.delete_course(course_id=5000, token="")
        print(response.json())

        print("status code: ", response.status_code)
        assert response.status_code == 200
        # assert '成功' in response.text
        assert '失败' in response.json().get("msg")
        assert 401 == response.json().get("code")