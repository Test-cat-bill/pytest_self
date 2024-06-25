# # 1, 打开文件
# f = open('a.txt', 'w', encoding='utf-8')
# # 2, 写文件
# f.write('好好学习\n')
# f.write('天天向上')
# # 3, 关闭文件
# f.close()

# # 1, 打开文件
# f = open('a.txt', 'r', encoding='utf-8')
# # 2, 读文件
# buf = f.read()
# print(buf)  # 目前只是打印读取的内容,可以做其它的事
# # 3. 关闭文件
# f.close()
# # r 方式打开文件 ,如果文件不存在,代码会报错

# with open('a.txt', 'a', encoding='utf-8') as f:
#     f.write('good good study ')


# read() 和 readline() 读到文件末尾, 返回一个空字符串, 即长度为 0

# with open('a.txt', encoding='utf-8') as f:
#     while True:
#         buf = f.readline()
#         if len(buf) == 0:
#             break
#         else:
#             print(buf, end='')

# 在容器中 , 容器为空,即容器中的数据的个数为 0 ,表示 False, 其余情况都是 True
with open('a.txt', encoding='utf-8') as f:
    while True:
        buf = f.readline()
        if buf:  # if len(buf) != 0
            print(buf)
        else:
            break