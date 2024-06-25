import requests

# 发送请求
url = "http://kdtx-test.itheima.net/api/login"

header_data = {
    "Content-Type": "application/json"
}
login_data = {
    "username": "admin",
    "password": "HM_2023_test",
    "code": 2,
    "uuid": "a262272c2c9c43168ca42b58ac0d417a"
}
response = requests.post(url=url, headers=header_data, json=login_data)

# 查看响应
print(response.status_code)
print(response.json())

