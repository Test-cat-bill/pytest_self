# URL： http://kdtx-test.itheima.net/api/common/upload
# 方法：Post
# 请求数据：
# 请求头：{ "Content-Type ":  " multipart/form-data ",  "Authorization":  "xxx " }
# 请求体：{" file " : 合同文件"}

# 接口信息：
# 新增合同：
# 地址：http://kdtx-test.itheima.net/api/contract
# 方法：Post
# 请求数据：
# 请求头：{ "Content-Type ":  "application/json ",  "Authorization":  "xxx " }
# 请求体：{ "name": "测试888", "phone": "13612345678", "contractNo": "HT10012003", "subject": "6", "courseId": " 99", "channel": "0", "activityId": 77, "fileName": "xxx"}

import requests

class ContractAPI:
    def __init__(self):
        self.upload_url = "http://kdtx-test.itheima.net/api/common/upload"
        self.add_contract_url = "http://kdtx-test.itheima.net/api/contract"
        self.select_url = "http://kdtx-test.itheima.net/api/contract/list"
        self.delete_url = "http://kdtx-test.itheima.net/api/contract/remove"

    def upload_contract(self, file_data, token):
        return requests.post(url=self.upload_url,files={"file":file_data},headers={"Authorization": token})

    def add_contract(self,test_data,token):
        # add_data = { "name": "测试888", "phone": "13612345678", "contractNo": "HT20230007", "subject": "6", "courseId": " 99", "channel": "0", "activityId": 77, "fileName": "xxx"}
        return requests.post(url=self.add_contract_url,json=test_data,headers={"Authorization": token})

    def select_contract(self,test_data,token):
        return requests.get(url=self.select_url,json=test_data,headers={"Authorization": token})

    # 这个接口行为很奇怪
    def delete_contract(self,test_data,token):
        return requests.post(url="{}/{}".format(self.delete_url,test_data),data=test_data,headers={"Authorization": token})