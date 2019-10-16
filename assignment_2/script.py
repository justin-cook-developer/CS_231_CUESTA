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
