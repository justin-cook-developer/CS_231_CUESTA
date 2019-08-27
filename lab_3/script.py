a = 2
b = 4.7
c = 3
d = 4.2

answer1 = b + a / c - d
answer2 = (a + b) / c - d
answer3 = d * -b - float(c / a)
answer4 = a - b * (c % int(d))
answer5 = d / a + (b * c)

print("answer1: " + str("{0:.2f}".format(answer1)))
print("answer2: " + str("{0:.2f}".format(answer2)))
print("answer3: " + str("{0:.2f}".format(answer3)))
print("answer4: " + str("{0:.2f}".format(answer4)))
print("answer5: " + str("{0:.2f}".format(answer5)))
