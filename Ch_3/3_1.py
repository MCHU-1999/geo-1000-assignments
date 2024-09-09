def right_justify(string: str):
    concat_string = ' ' * (70-len(string)) + string
    return concat_string


if __name__ == '__main__':
    print('monty')
    print(right_justify('monty'))
