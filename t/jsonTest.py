import json

with open('test.json',encoding='utf-8') as f:
    result = json.load(f)
    print(type(result))
    # 姓名
    print(result.get('name'))
    # 年龄
    print(result.get('age'))
    # 城市
    print(result.get('address').get('city'))

    print(result.get('address'))

# with open('info.json', encoding='utf-8') as f:
#     # 3. 读取文件
#     # buf = f.read()
#     # print(type(buf), buf)
#     result = json.load(f)
#     print(type(result))  # <class 'dict'>
#     # 姓名
#     print(result.get('name'))
#     # 年龄
#     print(result.get('age'))
#     # 城市
#     print(result.get('address').get('city'))