import math
import unittest

# ----- FUNCTIONS -----


def isInt(value: int) -> bool:
    return isinstance(value, int)


def average(total: int, n: int) -> float:
    if isInt(total) == False:
        raise TypeError('Total must be of type int')

    if isInt(n) == False:
        raise TypeError('n must be of type int')

    if n <= 0:
        raise ValueError('n must be >= 0')

    avg = float(total) / float(n)
    return round(avg, 2)


# ----- TESTS - ----

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
