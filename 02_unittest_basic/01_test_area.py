import unittest


def area(widht, height):
    """The function returns the area of the rectangle."""

    if not (isinstance(widht, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (widht > 0 and height > 0):
        return ValueError('The width and height must be positive')

    return widht * height

class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 5), 20, 'message')


if __name__ == '__main__':
    unittest.main(verbosity=2)