# Justin Cook / justin_cook3@my.cuesta.edu
# CIS 231 / Scovil
# Lab 6


import math


def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


def square(num):
    return num ** 2


def hypotenuse(a, b):
    c = math.sqrt(square(a) + square(b))
    return float(c)


def is_between(x, y, z):
    return x <= y and y <= z


# test compare
print('comapare(1, 2) == -1', compare(1, 2) == -1)
print('comapare(2, 1) == 1', compare(2, 1) == 1)
print('comapare(1, 1) == 0', compare(1, 1) == 0)


print('----------')


# test hypotenuse
print('hypotenuse(3, 4) == 5', hypotenuse(3, 4) == 5.0)
print('hypotenuse(1, 2) == 5 ** 1/2', hypotenuse(1, 2) == math.sqrt(5))
print('hypotenuse(2, 2) == 8 ** 1/2', hypotenuse(2, 2) == math.sqrt(8))


print('----------')


# test in_between
print('is_between(1, 2, 3) == True', is_between(1, 2, 3) == True)
print('is_between(1, 1, 1) == True', is_between(1, 1, 1) == True)
print('is_between(1, 2, 1) == False', is_between(1, 2, 1) == False)
print('is_between(2, 2, 1) == False', is_between(2, 2, 1) == False)
print('is_between(3, 2, 2) == False', is_between(3, 2, 2) == False)
