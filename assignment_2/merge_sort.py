def split(arr):
    middle = len(arr) // 2

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
