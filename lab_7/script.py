from typing import Any, TypeVar
import math
import unittest

# ----- CUSTOM TYPES; JUST FOR FUN -----
MinMax = TypeVar('MinMax', int, None)


# ----- FUNCTIONS -----


def isInt(value: Any) -> bool:
    return isinstance(value, int)


def isMinMax(val: Any) -> bool:
    valid = isInt(val) or val == None
    return valid


def calculateMax(currentMax: MinMax, val: int) -> int:
    if isMinMax(currentMax) == False:
        raise TypeError('currentMax must be of type MinMax')

    if isInt(val) == False:
        raise TypeError('val must be of type int')

    if currentMax == None:
        return val
    else:
        return max(currentMax, val)


def calculateMin(currentMin: MinMax, val: int) -> int:
    if isMinMax(currentMin) == False:
        raise TypeError('currentMin must be of type MinMax')

    if isInt(val) == False:
        raise TypeError('val must be of type int')

    if currentMin == None:
        return val
    else:
        return min(currentMin, val)


def average(total: int, n: int) -> float:
    if isInt(total) == False:
        raise TypeError('Total must be of type int')

    if isInt(n) == False:
        raise TypeError('n must be of type int')

    if n <= 0:
        raise ValueError('n must be >= 0')

    avg = float(total) / float(n)
    return round(avg, 2)


# I am pretty getIntegerInput() could, in theory, "overflow" the callstack,
#  but I am going to make positive assumptions about user input
def getIntegerInput() -> int:
    inputValue = input('Please input an integer:\n')

    try:
        output = int(inputValue)
        return output
    except ValueError:
        print('Inputs must be integers.')
        return getIntegerInput()


def partOne():
    sum = 0
    validInputs = 0
    min = None
    max = None

    negativeInput = False

    while(negativeInput == False):
        integer = getIntegerInput()

        if (integer < 0):
            negativeInput = True
        else:
            sum += integer
            validInputs += 1
            max = calculateMax(max, integer)
            min = calculateMin(min, integer)

    if (validInputs > 0):
        print('The sum of all non-negative integers is: ', sum)
        print('The number of non-negative integers entered is: ', validInputs)
        print(
            'The average of all non-negative integers entered is: ',
            average(sum, validInputs)
        )
        print('The largest non-negative integer entered is: ', max)
        print('The smallest non-negative integer entered is: ', min)
    else:
        print('No valid numbers entered')


# ----- INVOKE METHODS -----
partOne()


# ----- TESTS FOR NON-SIDE-AFFECT FUNCTIONS; RUN 'python3 -m unittest script.py' THEN ENTER -1 -----


class TestIsInt(unittest.TestCase):
    def testReturnsTrueForIntegers(self):
        self.assertTrue(isInt(5))
        self.assertTrue(isInt(2))
        self.assertTrue(isInt(99))

    def testReturnsFalseForNonIntegers(self):
        self.assertFalse(isInt('5'))
        self.assertFalse(isInt(None))
        self.assertFalse(isInt({}))
        self.assertFalse(isInt([]))


class TestCalculateMax(unittest.TestCase):
    def testReturnsTheMax(self):
        self.assertEqual(calculateMax(None, 4), 4)
        self.assertTrue(calculateMax(5, 4), 5)

    def testThrowsTypeErrors(self):
        self.assertRaises(TypeError, calculateMax, '1', 2)
        self.assertRaises(TypeError, calculateMax, None, '3')


class TestCalculateMin(unittest.TestCase):
    def testReturnsTheMax(self):
        self.assertEqual(calculateMin(None, 4), 4)
        self.assertTrue(calculateMin(5, 4), 4)

    def testThrowsTypeErrors(self):
        self.assertRaises(TypeError, calculateMin, '1', 2)
        self.assertRaises(TypeError, calculateMin, None, '3')


class TestAverage(unittest.TestCase):

    def testReturnsAFloat(self):
        self.assertTrue(isinstance(average(2, 1), float))
        self.assertTrue(isinstance(average(5, 2), float))

    def testWorksWithIntegerInputs(self):
        self.assertEqual(average(2, 2), 1.0)
        self.assertEqual(average(5, 2), 2.5)
        self.assertEqual(average(7, 2), 3.5)

    def testOnlyTakesIntegerInputs(self):
        self.assertRaises(TypeError, average, '1', 2)
        self.assertRaises(TypeError, average, 1, '2')
        self.assertRaises(TypeError, average, 1.5, 2)

    def testNMustBeGreaterThanZero(self):
        self.assertRaises(ValueError, average, 1, 0)
        self.assertRaises(ValueError, average, 1, -1)
