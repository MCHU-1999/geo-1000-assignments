def right_justify(string: str):
    concat_string = ' ' * (70-len(string)) + string
    return concat_string

# +----+----+||| ||| ||| ||| +----+----+ ||| ||| ||| ||| +----+----+

def grid(row_num: int, col_num: int, size = 4):
    floor = '+' + (' -' * size + ' +') * col_num
    pillars = '|' + (' '*(2*size+1) + '|') * col_num
    string = floor + '\n' + ((pillars + '\n') * size + floor + '\n') * row_num
    # print(string)
    return string


if __name__ == '__main__':
    print('monty')
    print(right_justify('monty'))

    print('\n')

    print('GRID:\n')
    print(grid(3, 3, 4))
    