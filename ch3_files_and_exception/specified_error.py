try:
    data = open('sketch1.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except:  # 这里没有添加任何异常，表示捕获所有异常
            pass

    data.close()
except ValueError:
    print('value error')
except IOError:  # 这里指定了IOError表示捕获特定异常
    print('The data is missing!')
except:
    print('broad error')
