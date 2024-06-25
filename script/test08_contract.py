import requests

from api.login import LoginAPI
from api.course import CourseAPI
from api.contract import ContractAPI

class TestContractBusiness:
    TOKEN = None
    def setup(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        self.contract_api =ContractAPI()

        response = self.login_api.verify_code()
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": response.json().get("uuid")
        }
        res_login = self.login_api.login(test_data=login_data)
        TestContractBusiness.TOKEN = res_login.json().get("token")

    def teardown(self):
        pass

    def test01_upload(self):
        f = open("../data/test.pdf", "rb")
        response = self.contract_api.upload_contract(file_data=f,token=TestContractBusiness.TOKEN)
        print(response.json())
        print(response.status_code)
        assert response.status_code == 200
        assert '成功' in response.json().get("msg")
        assert 200 == response.json().get("code")

    def test02_add_contract(self):
        f = open("../data/test.pdf", "rb")
        response1 = self.contract_api.upload_contract(file_data=f,token=TestContractBusiness.TOKEN)
        file_name = response1.json().get('url')

        add_data = {"name": "测试888", "phone": "13612345678", "contractNo": "HT202307105327007", "subject": "6",
                    "courseId": " 99", "channel": "0", "activityId": 77, "fileName": "11"}

        response = self.contract_api.add_contract(test_data=add_data,token=TestContractBusiness.TOKEN)
        print(response.json())
        print(response.status_code)
        assert response.status_code == 200
        assert '成功' in response.json().get("msg")
        assert 200 == response.json().get("code")

    def test03_select_contract(self):
        test_data = {
            "phone": "13612345678"
        }
        response = self.contract_api.select_contract(test_data=test_data, token=TestContractBusiness.TOKEN)
        print(response.json())
        print(response.status_code)

        assert response.status_code == 200
        assert '成功' in response.json().get("msg")
        assert 200 == response.json().get("code")

    def test04_delete_contract(self):
        test_data = {
            "id": "99"
        }
        print(test_data.get("id"))
        response = self.contract_api.delete_contract(test_data=test_data.get("id"), token=TestContractBusiness.TOKEN)
        print(response.json())
        print(response.status_code)

        # assert response.status_code == 200
        # assert '成功' in response.json().get("msg")
        # assert 200 == response.json().get("code")
