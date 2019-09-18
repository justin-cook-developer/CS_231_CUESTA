# Justin Cook / justin_cook3@my.cuesta.edu
# CIS 231 / Scovil
# Lab 8


def charCount(char, word):
    counter = 0

    for character in word:
        if char == character:
            counter += 1

    return counter


def filterOutChar(char, word):
    new_word = ''

    for character in word:
        if character != char:
            new_word += character

    return new_word


print("charCount('h', 'hello') == 1 :", charCount('h', 'hello') == 1)
print("charCount('l', 'hello') == 2 :", charCount('l', 'hello') == 2)
print("charCount('b', 'brother') == 1 :", charCount('b', 'brother') == 1)


print("\nfilterOutChar('h', 'hello') == 'ello' :",
      filterOutChar('h', 'hello') == 'ello')
print("filterOutChar('l', 'hello') == 'heo' :",
      filterOutChar('l', 'hello') == 'heo')
print("filterOutChar('o', 'hello') == 'hell' :",
      filterOutChar('o', 'hello') == 'hell')
