from math import inf, floor, sqrt

# pure functions


def split(arr):
    middle = floor(len(arr) / 2)

    return (arr[0:middle], arr[middle:])


def merge(left, right):
    merged = [0] * (len(left) + len(right))

    i = 0
    j = 0
    k = 0

    while (i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1

        k += 1

    while (i < len(left)):
        merged[k] = left[i]
        k += 1
        i += 1

    while (j < len(right)):
        merged[k] = right[j]
        k += 1
        j += 1

    return merged


def merge_sort(arr):
    if (len(arr) <= 1):
        return arr
    else:
        (left, right) = split(arr)

        return merge(
            merge_sort(left),
            merge_sort(right)
        )


def fahrenheit_to_celsius(fahr):
    return (fahr - 32) * (5 / 9)


# likely unecessary, can index into sorted array
def min_and_max(nums):
    highest = -inf
    lowest = inf

    for num in nums:
        if num > highest:
            highest = num
        elif num < lowest:
            lowest = num

    return (lowest, highest)


def average(nums):
    total = 0.0

    for num in nums:
        total = total + num

    return total / len(nums)


def below_equal_above_avg(nums, avg):
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

    return (below, equal, above)


def standard_deviation(nums, average):
    sum_of_vals_from_mean_squared = 0.0

    for num in nums:
        sum_of_vals_from_mean_squared += (num - average) ** 2

    return sqrt(sum_of_vals_from_mean_squared / (len(nums) - 1))


# side affect functions
def get_num_of_temps():
    base_msg = 'Please enter the number of fahrenheit values you wish to input, between 1 and 35, inclusive: '

    num_temps = int(input(base_msg))

    while (num_temps < 1 or num_temps > 35):
        num_temps = int(input(
            'The value you entered is outside the accepted range. ' + base_msg
        ))

    return num_temps


def get_single_temp():
    base_msg = 'Please enter a fahrenheit temperature between -150.0 and 150.0, inclusive, note values can be floats: '

    temp = float(input(base_msg))

    while(temp < -150.0 or temp > 150.0):
        temp = float(
            input('The value you entered is outside the accepted range. ' + base_msg)
        )

    return temp


def main(
    get_num_of_temps, get_single_temp, merge_sort, fahrenheit_to_celsius,
    average, below_equal_above_avg, standard_deviation
):
    num_temps = get_num_of_temps()

    temps = []

    for k in range(num_temps):
        temps.append(get_single_temp())

    sorted_temps = merge_sort(temps)

    for temp in sorted_temps:
        print('temp f : c', temp, fahrenheit_to_celsius(temp))

    fahr_avg = average(sorted_temps)

    print('averages f : c', fahr_avg, fahrenheit_to_celsius(fahr_avg))

    print(
        'high f : c', sorted_temps[-1],
        fahrenheit_to_celsius(sorted_temps[-1])
    )

    print(
        'low f : c', sorted_temps[0],
        fahrenheit_to_celsius(sorted_temps[0])
    )

    (below, equal, above) = below_equal_above_avg(sorted_temps, fahr_avg)

    print('below', below)
    print('equal', equal)
    print('above', above)

    print('std dev', standard_deviation(sorted_temps, fahr_avg))


main(
    get_num_of_temps, get_single_temp, merge_sort, fahrenheit_to_celsius,
    average, below_equal_above_avg, standard_deviation
)
