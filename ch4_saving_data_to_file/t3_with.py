man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
except IOError:
    print('The data file is missing!')

# 使用with相当于kotlin的use和java的try-with-resource
try:
    with open('man_data.txt', 'w') as out_man:
        print(man, file=out_man)
    with open('other_data.txt', 'w') as out_other:
        print(other, file=out_other)
except IOError as err:
    print('File error: ' + str(err))

# 也可以用逗号合并声明
# try:
#     with open('man_data.txt', 'w') as out_man, open('other_data.txt', 'w') as out_other:
#         print(man, file=out_man)
#         print(other, file=out_other)
# except IOError as err:
#     print('File error: ' + str(err))
