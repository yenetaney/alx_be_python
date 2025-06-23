import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def set_up(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
         self.assertEqual(self.calc.addition(6,9),11)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10,9),1)
    def test_divide(self):
         self.assertEqual(self.calc.divide(10,2),5)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()

