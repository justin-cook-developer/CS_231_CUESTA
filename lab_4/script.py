import math


def printNameFiveTimes(name):
    for i in range(5):
        print(name)


printNameFiveTimes('Justin')
printNameFiveTimes('Ethan')
printNameFiveTimes('Blake')


def printNameXTimes(name, iterations):
    for i in range(iterations):
        print(name)


printNameXTimes('Justin', 1)
printNameXTimes('Ethan', 2)
printNameXTimes('Blake', 3)


def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


print(hypotenuse(3, 4))  # expect 5
print(hypotenuse(1, 2))  # expect 5 ^ 1/2


def quadratic(a, b, c):
    root = math.sqrt(b ** 2 - (4 * a * c))
    denominator = 2 * a
    x1 = (-b + root) / denominator
    x2 = (-b - root) / denominator
    return [x1, x2]


print(quadratic(1, 3, -4))  # expect [1, -4]
