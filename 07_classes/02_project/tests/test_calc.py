import sys
import unittest

path = r'C:\Users\paula\PycharmProjects\python-unittest\07_classes\02_project'
sys.path.append(path)

from calculator.calc_math import SimpleMathCalculator


class TestSimpleMathCalculator(unittest.TestCase):

    def test_add(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.add(3, 4), 7)

    def test_sub(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.sub(3, 4), -1)

    def test_mul(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.mul(3, 4), 12)