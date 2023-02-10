
def area(widht, height):
    """The function returns the area of the rectangle."""

    if not (isinstance(widht, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (widht > 0 and height > 0):
        raise ValueError('The width and height must be positive')

    return widht * height

def perimeter(widht, height):
    """The function returns the perimeter of the rectangle."""

    if not (isinstance(widht, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float.')

    if not (widht > 0 and height > 0):
        raise ValueError('The width and height must be positive')

    return 2 * widht + 2 * height
