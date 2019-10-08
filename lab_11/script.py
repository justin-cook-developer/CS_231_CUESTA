# Justin Cook / justin_cook3@my.cuesta.edu
# CIS 231 / Scovil
# Lab 11


def histogram(string):
    dictionary = dict()

    for char in string:
        dictionary[char] = dictionary.get(char, 0) + 1

    return dictionary


def reverse_lookup(dictionary, value):
    keys = []

    for key in dictionary:
        if dictionary[key] == value:
            keys.append(key)

    return keys


# I know prints shouldn't normally go in a function,
# but I wanted to show that the memo is working.
# I couldn't figure out how to do that w/o returning an array containing the value
# and a boolean to indicate whether the value was in the memo
# like so [value : int, inMemo : bool]


def factorial(n, known={1: 1}):
    if n in known:
        print('factorial(' + str(n) + ') in memo')
        return known[n]
    else:
        res = n * factorial(n - 1, known)
        known[n] = res
        return res


# ----- histogram tests -----
def print_hist(h):
    if len(h) == 0:
        print('Empty histogram')
    else:
        for key in h:
            print(key, h[key])


print('Histogram of "abcdefghijkl"')
print_hist(histogram('abcdefghijkl'))
print('\nHistogram of "hello there"')
print_hist(histogram('hello there'))
print('\nHistogram of ""')
print_hist(histogram(''))


# ----- reverse_lookup tests -----
hello_hist = histogram('hello')
print('\nKeys with value 1 in histogram("hello") :',
      reverse_lookup(hello_hist, 1))
print('Keys with value 2 in histogram("hello") :', reverse_lookup(hello_hist, 2))
print('Keys with value 5 in histogram("hello") :', reverse_lookup(hello_hist, 4))


# ----- factorial tests -----
print('')
for i in range(1, 11):
    print('Factorial of', i, 'is', factorial(i), '\n')
