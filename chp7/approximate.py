import math


def calculateStep(k):
    constant = (2 * math.sqrt(2)) / 9801

    numerator = math.factorial(4 * k) * (1103 + (26390 * k))
    denominator = (math.factorial(k) ** 4) * (396 ** (4 * k))

    return (numerator / denominator) * constant


def approximate():
    sum = 0
    k = 0

    last_term = calculateStep(k)
    sum += last_term
    k += 1

    while last_term >= (10 ** -15):
        last_term = calculateStep(k)
        sum += last_term
        k += 1

    return sum


print(approximate() == (1 / math.pi))
