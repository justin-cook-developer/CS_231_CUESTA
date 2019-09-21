# Justin Cook / justin_cook3@my.cuesta.edu
# CIS 231 / Scovil
# Assignment 1
# Due: 9 / 20 / 19


def oneDecPlace(floatVar):
    return "{:.1f}".format(floatVar)


def getFahrenheit():
    return float(input('Please enter a float for the temperature, in fahrenheit: '))


def fahrenheitToCels(f):
    return float((f - 32) * (5 / 9))


def averageOf5(num1, num2, num3, num4, num5):
    return float((num1 + num2 + num3 + num4 + num5) / float(5))


def main():
    fahrenheit1 = getFahrenheit()
    fahrenheit2 = getFahrenheit()
    fahrenheit3 = getFahrenheit()
    fahrenheit4 = getFahrenheit()
    fahrenheit5 = getFahrenheit()

    print(
        '\nThe fahrenheit temperatures you entered are:',
        oneDecPlace(fahrenheit1), ',', oneDecPlace(fahrenheit2),
        ',', oneDecPlace(fahrenheit3), ',', oneDecPlace(fahrenheit4),
        ',', oneDecPlace(fahrenheit5)
    )

    print(
        '\nThe average of all the fahrenheit temperatures is:',
        oneDecPlace(averageOf5(
            fahrenheit1, fahrenheit2,
            fahrenheit3, fahrenheit4, fahrenheit5
        ))
    )

    celsius1 = fahrenheitToCels(fahrenheit1)
    celsius2 = fahrenheitToCels(fahrenheit2)
    celsius3 = fahrenheitToCels(fahrenheit3)
    celsius4 = fahrenheitToCels(fahrenheit4)
    celsius5 = fahrenheitToCels(fahrenheit5)

    print(
        '\nThe fahrenheit temperatures converted to celsius are:',
        oneDecPlace(celsius1), ',', oneDecPlace(celsius2), ',',
        oneDecPlace(celsius3), ',', oneDecPlace(celsius4),
        ',', oneDecPlace(celsius5)
    )

    print(
        '\nThe average of all the celsius temperatures is:',
        oneDecPlace(
            averageOf5(celsius1, celsius2, celsius3, celsius4, celsius5)
        )
    )



main()
