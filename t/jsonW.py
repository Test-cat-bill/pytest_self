import json

my_list = [('admin', '123456', '登录成功'), ('root', '123456', '登录失败'), ('admin', '123123', '登录失败')]

# with open('info4.json', 'w', encoding='utf-8') as f:
#     # json.dump(my_list, f)
#     # json.dump(my_list, f, ensure_ascii=False)  # 直接显示中文,不以 ASCII 的方式显示
#     # 显示缩进
#     # json.dump(my_list, f, ensure_ascii=False, indent=2)
#     json.dump(my_list, f, ensure_ascii=False, indent=4)

with open('info4.json', 'r', encoding='utf-8') as f:
    res = json.load(f)
    for i in res:
        print(i)