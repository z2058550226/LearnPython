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

try:
    out_man = open('man_data.txt', 'w')
    out_other = open('other_data.txt', 'w')
    print(man, file=out_man)
    print(other, file=out_other)
except IOError as err:
    print('Write file error: ' + str(err))
finally:
    if 'out_man' in locals():
        out_man.close()
    if 'out_other' in locals():
        out_other.close()
