# +----+----+||| ||| ||| ||| +----+----+ ||| ||| ||| ||| +----+----+

def grid(row_num: int, col_num: int, size = 4):
    floor = '+' + (' -' * size + ' +') * col_num
    pillars = '|' + (' '*(2*size+1) + '|') * col_num
    string = floor + '\n' + ((pillars + '\n') * size + floor + '\n') * row_num
    # print(string)
    return string


if __name__ == '__main__':
    print('GRID:\n')
    print(grid(3, 3, 4))
    