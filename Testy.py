import unittest
from app import from_roman



class MyTestCase(unittest.TestCase):

    def test01(self):
        self.assertEqual(from_roman('X'),10)

    def test01(self):
        self.assertIsNone(from_roman(1))

    def test02(self):
        self.assertIsNone(from_roman('H'), roman_numerals)

    def test03(self):
        self.assertIsNone(from_roman('X'))

    def test04(self):
        self.assertRaises(TypeError, from_roman(1))
    def test05(self):
        self.assertRaises(Exception, from_roman('a'))
if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()



