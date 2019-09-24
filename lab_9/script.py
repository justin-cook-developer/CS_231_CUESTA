def getFloatInput():
    return float(input('\nPlease enter a float: '))


def printElemsFirstToLast(arr):
    for elem in arr:
        print('\n', "{:.1f}".format(elem))


def printElemsLastToFirst(arr):
    for i in range(15):
        print('\n', "{:.1f}".format(arr[14 - i]))


def printHighestAndLowest(nums):
    lowest = None
    highest = None

    for num in nums:
        if (lowest == None or num < lowest):
            lowest = num
        elif (highest == None or num > highest):
            highest = num

    print('\n\nThe lowest number you inputted is:', "{:.1f}".format(lowest))

    print('\nThe highest number you inputted is:', "{:.1f}".format(highest))


def average(nums):
    total = 0

    for num in nums:
        total += num

    return float(float(total) / len(nums))


def printNumAboveBelowEqualAvg(nums):
    avg = average(nums)

    below = 0
    equal = 0
    above = 0

    for num in nums:
        if num < avg:
            below += 1
        elif num == avg:
            equal += 1
        else:
            above += 1

    print('\n\n', "{:.1f}".format(below), 'numbers are below the average')
    print('\n', "{:.1f}".format(equal), 'numbers are equal to the average')
    print('\n', "{:.1f}".format(above), 'numbers are above the average')


def main():
    floats = []

    for i in range(15):
        floats.append(getFloatInput())

    print('\n\nFloats, first to last')

    printElemsFirstToLast(floats)

    print('\n\nFloats, last to first')

    printElemsLastToFirst(floats)

    printNumAboveBelowEqualAvg(floats)

    printHighestAndLowest(floats)


main()
