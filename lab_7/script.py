import math
import unittest

# ----- FUNCTIONS -----


def average(total: int, n: int) -> float:
    if isinstance(total, int) == False:
        raise TypeError('Total must be of type int')

    if isinstance(n, int) == False:
        raise TypeError('n must be of type int')

    if n <= 0:
        raise ValueError('n must be >= 0')

    avg = float(total) / float(n)
    return round(avg, 2)


# ----- TESTS - ----


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
