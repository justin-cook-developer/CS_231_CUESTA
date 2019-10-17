# Justin Cook / justin_cook3@my.cuesta.edu
# CIS 231 / Scovil
# Assignment 2

from math import inf, floor, sqrt


# pure functions
def selectionSort(list):
    for i in range(len(list) - 1):
        minIndex = i

        for j in range(i + 1, len(list)):
            if list[j] < list[minIndex]:
                minIndex = j

        temp = list[minIndex]
        list[minIndex] = list[i]
        list[i] = temp


def fahrenheit_to_celsius(fahr):
    return (fahr - 32) * (5 / 9)


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
    if (len(nums) == 1):
        return 0

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


# main program: tie all of the pieces together
def main(
    get_num_of_temps, get_single_temp, selectionSort, fahrenheit_to_celsius,
    average, below_equal_above_avg, standard_deviation
):
    num_temps = get_num_of_temps()

    temps = []

    for k in range(num_temps):
        temps.append(get_single_temp())

    selectionSort(temps)

    header = 'CIS 231 - Assignment 2 - Justin Cook'
    print(header.rjust(len(header) + 20), '\n')

    print('{:>30} {:>10}'.format('FAHR', 'CELS'))
    print('\n{:>30} {:>10}'.format('====', '===='))

    for temp in temps:
        print('{:>30} {:>10}'.format(
            "{:.1f}".format(temp),
            "{:.1f}".format(fahrenheit_to_celsius(temp)
                            )))

    print('{:>30} {:>10}'.format('====', '===='))

    fahr_avg = average(temps)

    print('\nAverage: {:>21} {:>10}'.format(
        "{:.1f}".format(fahr_avg),
        "{:.1f}".format(fahrenheit_to_celsius(fahr_avg))
    ))

    print('\nHigh: {:>24} {:>10}'.format(
        "{:.1f}".format(temps[-1]),
        "{:.1f}".format(fahrenheit_to_celsius(temps[-1]))
    ))

    print('\nLow: {:>25} {:>10}'.format(
        "{:.1f}".format(temps[0]),
        "{:.1f}".format(fahrenheit_to_celsius(temps[0]))
    ))

    (below, equal, above) = below_equal_above_avg(temps, fahr_avg)

    print('\nAbove Average: {:>13}'.format(above))
    print('Equal to Average: {:>10}'.format(equal))
    print('Below to Average: {:>10}'.format(below))

    print('\nStandard Deviation: {:>10}'.format(
        "{:.1f}".format(standard_deviation(temps, fahr_avg)
                        )))


main(
    get_num_of_temps, get_single_temp, selectionSort, fahrenheit_to_celsius,
    average, below_equal_above_avg, standard_deviation
)
