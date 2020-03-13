import os  # 从标准库导入os

print(os.getcwd())  # 相当于命令行的pwd
os.chdir('../ch1')  # 相当于命令行的cd
print(os.getcwd())
os.chdir('../ch3_files_and_exception')
print(os.getcwd())

data = open('sketch.txt')  # 打开了一个文件，python中默认的打开都是基于行的文本文件
print(data.readline(), end='')  # 由于是line based，所以会自带一个换行字符，所以加上end参数
print(data.readline(), end='')
data.seek(0)  # 将cursor移回第一行
for each_line in data:  # 可以作为迭代器使用
    print(each_line, end='')

data.seek(0)  # 要想再次使用就要重置cursor的位置
for each_line in data:
    print(each_line, end='')

data.close()  # 用完要关闭流


