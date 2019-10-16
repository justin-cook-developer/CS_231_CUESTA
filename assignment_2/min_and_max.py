def min_and_max(nums):
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
