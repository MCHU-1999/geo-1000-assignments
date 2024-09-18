import math

# Exercise 8.3
def is_palindrome(word):
    return word == word[::-1]


# Exercise 8.4
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True             # will return False if any character isn't lowercase.
        else:
            return False
        
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'           # always true.
        else:
            return 'False'
        
def any_lowercase3(s):
    for c in s:
        flag = c.islower()          # flag value assign every iteration, it works only for last character.
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()  # works properly
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():         # return False if an non-lower case character occured.
            return False
    return True



if __name__ == '__main__':

    # Exercise 8.1
    # Exercise 8.2
    print('banana'.count('a'))

    # Exercise 8.3
    print(is_palindrome('redivider'))

    # Exercise 8.4
    print('\n\nExercise 8.4')
    print(any_lowercase1('Qwerty')) # will return False if any character isn't lowercase.
    print(any_lowercase2('QWERTY')) # always true.
    print(any_lowercase3('QwertY')) # flag value assign every iteration, it works only for last character.
    print(any_lowercase4('Qwerty')) # normal
    print(any_lowercase5('qwertY')) # return False if an non-lower case character occured.

