def is_divisible_by(left, right):
    return left % right == 0


def factorials_up_to_ten():
    factorial = 1

    for i in range(1, 11):
        factorial = factorial * i
        print('factorial of', i, 'is', factorial)


def in_ascending_order(a, b, c):
    return a < b < c


print(is_divisible_by(20, 10))
print(is_divisible_by(20, 11))

factorials_up_to_ten()

print(in_ascending_order('a', 'b', 'c'))
print(in_ascending_order('a', 'c', 'b'))
