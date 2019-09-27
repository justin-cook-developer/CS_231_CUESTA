def formatToOneDec(num):
    return "{:.1f}".format(num)


def get_num_values():
    numInputs = int(input(
        'How many values would you like to input? Please enter a number between 2 and 15: '
    ))

    while (numInputs < 2 or numInputs > 15):
        numInputs = int(input(
            '\nHow many values would you like to input? Please enter a number between 2 and 15: '
        ))

    return numInputs


def input_nums(numVaues):
    nums = []

    for i in range(0, numVaues):
        nums.append(float(
            input('\nPlease enter a float: ')
        ))

    return nums


def rev_order(arr):
    length = len(arr)

    for i in range(1, length + 1):
        print(formatToOneDec(arr[length - i]), '\n')


def average(nums):
    total = 0.0

    for num in nums:
        total = float(total + num)

    return total / len(nums)


def abo_bel_equ(nums):
    avg = average(nums)

    below = 0
    equal = 0
    above = 0

    for num in nums:
        if num > avg:
            above += 1
        elif num == avg:
            equal += 1
        else:
            below += 1

    print('\nThe average is: ', formatToOneDec(avg))
    print('\nThere are ', formatToOneDec(above), ' numbers above the average.')
    print('\nThere are ', formatToOneDec(below), ' numbers below the average.')
    print('\nThere are ', formatToOneDec(equal),
          ' numbers equal to the average.')


def hi_lo(nums):
    lowest = None
    highest = None

    for num in nums:
        if (lowest == None or num < lowest):
            lowest = num
        if (highest == None or num > highest):
            highest = num

    print('\nThe lowest number you inputted is:', formatToOneDec(lowest))

    print('\nThe highest number you inputted is:', formatToOneDec(highest))


def main():
    print('\n')

    nums = input_nums(get_num_values())

    print('\nIn reverse order:\n')

    rev_order(nums)

    abo_bel_equ(nums)

    hi_lo(nums)


main()
