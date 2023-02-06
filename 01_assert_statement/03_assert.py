widht = int(input('Enter the widht of the rectangle: '))
assert widht > 0, 'The widht value must be positive.'
height = int(input('Enter the height of the rectangle: '))
assert height > 0, 'The height value must be positive.'

area = widht * height
print(f'Area: {area}')