import requests

response =requests.get(url="http://kdtx-test.itheima.net/api/captchaImage")
# print(response.content)
print(response.status_code)
print(response.apparent_encoding)

print(response.text)

print(response.json()['uuid'])