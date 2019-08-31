# Justin Cook / justin_cook3@my.cuesta.edu
# CIS 231 / Scovil
# Lab 5


def isOdd(integer):
    isEven = integer % 2 == 0
    msg = None

    if (isEven):
        msg = str(integer) + ' is even!'
    else:
        msg = str(integer) + ' is odd!'

    print(msg)


def minutesToClosestHour(minutes):
    pastHalfHour = minutes > 30

    if (pastHalfHour):
        minutesToLog = 60 - minutes
        print(minutesToLog, 'before the hour')
    else:
        print(minutes, 'minutes after the hour')


def comapreNums(x, y):
    output = 'x: ' + str(x) + ', y: ' + str(y)

    if (x > y):
        output += ', x > y'
    elif (x < y):
        output += ', x < y'
    else:
        output += ', x == y'

    print(output)


def main():
    x = int(input('Input an x value\n'))

    isOdd(x)
    minutesToClosestHour(x)

    y = int(input('Input a y value\n'))
    comapreNums(x, y)


main()
