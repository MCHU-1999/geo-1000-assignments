def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x=x+1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

# ===================================================

def Ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return Ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return Ackermann(m - 1, Ackermann(m, n- 1))
    else:
        pass

# ===================================================

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    word = word.split(' ')
    word = ''.join(word)
    length = len(word)
    for i in range(length//2):
        if word[i] != word[-1 - i]:
            return False
    return True


if __name__ == '__main__':

    # Exercise 6.1
    print('Exercise 6.1')
    x = 1
    y = x + 1
    print(c(x, y + 3, x + y))

    # Exercise 6.2
    print('Exercise 6.2')
    print(Ackermann(3, 4))

    # Exercise 6.3
    print('Exercise 6.3')
    print(middle('abcd'))
    print(middle('abc'))
    print(middle('ab'))
    print(middle('a'))
    print(middle(''))
    print(is_palindrome('nurses run'))
    print(is_palindrome('redivider'))