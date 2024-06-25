# 课程模块接口封装：核心在于依据接口文档实现接口信息封装、重点关注接口如何被调用
# 接口信息：
# URL：http://kdtx-test.itheima.net/api/clues/course
# 方法：Post
# 请求数据：
# 请求头：{ "Content-Type ":  "application/json ",  "Authorization":  "xxx " }
# 请求体：{ "name": "测试开发提升课01", "subject": "6","price": 899,"applicablePerson": "2",  "info": "测试开发提升课01"}

# 导包
import requests

class CourseAPI:
    def __init__(self):
        self.add_course_url = "http://kdtx-test.itheima.net/api/clues/course"
        self.select_course_url = "http://kdtx-test.itheima.net/api/clues/course/list"

    def select_course(self, test_data, token):
        return requests.get(url="{}/{}".format(self.select_course_url,test_data),headers={"Authorization": token})

    def add_course(self, test_data, token):
        return requests.post(url=self.add_course_url, json=test_data, headers={"Authorization": token})

    def update_course(self, test_data, token):
        return requests.put(url=self.add_course_url, json=test_data, headers={"Authorization": token})

    def delete_course(self, course_id, token):
        return requests.delete(url="{}/{}".format(self.add_course_url,course_id), headers={"Authorization": token})



