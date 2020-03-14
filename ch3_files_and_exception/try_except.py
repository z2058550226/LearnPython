import os

if os.path.exists('sketch.txt'):
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except:  # 这里没有添加任何异常，表示捕获所有异常
            pass

    data.close()
else:
    print('The data is missing!')
