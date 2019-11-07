def divmod(tupl):
    return (
        int(tupl[0] / tupl[1]),
        tupl[0] % tupl[1]
    )


print(divmod((7, 3)))


def includes(tupls, tupl):
    for tup in tupls:
        if tup == tupl:
            return True

    return False


myTup = (1, 2)
tups = [myTup, (2, 3)]

print(includes(tups, myTup))


def highsAndHighest(listOfDicts):
    highs = []
    highest = None

    if len(listOfDicts):
        highest = listOfDicts[0]["high"]

    for dic in listOfDicts:
        high = dic["high"]

        highs.append(high)

        if high > highest:
            highest = high

    return (highs, highest)


print(highsAndHighest(
  [{ "high": 3 }, { "high": 4 }, { "high": 8 }]
))


def printEvens():
  for n in range(2, 101, 2):
    print(n)


printEvens()
