import math

def get_long_words(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    lines = ''.join(lines)
    lines = lines.strip(",.'-\n")

    words = []
    word = []

    for char in lines:
        if char.isalpha():
            word.append(char)
        else:
            if word:
                if len(word)>=20:
                    words.append(''.join(word))
                word = []

    print(words)
    return words

def has_no_e(word: str):
    for char in word:
        if char.casefold() == 'e':
            return False
    return True

def get_no_e_words(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    lines = ''.join(lines)
    lines = lines.strip(",.'-\n")

    words = []
    word = []

    for char in lines:
        if char.isalpha():
            word.append(char)
        else:
            if word:
                if has_no_e(word):
                    words.append(''.join(word))
                word = []

    print(words)
    return words

def avoids(word: str, forbidden: str):
    for char in word.casefold():
        if char in forbidden.casefold():
            return False
    return True

def uses_only(word: str, limit: str):
    for char in word.casefold():
        if not char in limit.casefold():
            return False
    return True

def uses_all(word: str, limit: str):
    limit_copy = limit.casefold()
    for char in word.casefold():
        if char in limit_copy:
            limit_copy = limit_copy.replace(char, '')
            # print(limit_copy)
    if limit_copy:
        return False
    else:
        return True
    
def is_abecedarian(word: str):
    word_copy = word.casefold()
    first = '0'
    for char in word_copy:
        if first > char:
            return False
        first = char

    return True


if __name__ == '__main__':
    # Exercise 9.1
    text_file = 'ch9-words.txt'
    get_long_words(text_file)

    # Exercise 9.2
    get_no_e_words(text_file)

    # Exercise 9.3
    print(avoids('lung', 'abcdefhijk'))

    # Exercise 9.4
    print(uses_only('a', 'abcd'))

    # Exercise 9.5
    print(uses_all('silica', 'acsil'))

    # Exercise 9.6
    print(is_abecedarian('ace'))

