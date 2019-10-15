from math import inf


def split(arr):
  middle = math.floor(len(arr) / 2)

  return (arr[0:middle], arr[middle:])


def merge(left, right):
  merged = [0] * (len(left) + len(right))

  i = 0
  j = 0
  k = 0

  while (i < len(left) and j < len(right)):
    if (left[i] <= right[j]):
      merged[k] = left[i]
      k += 1
      i += 1
    else:
      merged[k] = right[j]
      k += 1
      j += 1

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


def highest_and_lowest(nums):
  if (len(nums) == 0):
        return None

    highest = -inf
    lowest = inf

    for num in nums:
      if num > highest:
        highest = num
      elif num < lowest:
        lowest = num


    return (lowest, highest)


def average(nums):
    if (len(nums) == 0):
        return None

    total = 0.0

    for num in nums:
        total = total + num

    return total / len(nums)


def below_equal_above_avg(nums, avg):
    if (len(nums) == 0):
        return None

    if avg == None:
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

    return (below, equal, above)
