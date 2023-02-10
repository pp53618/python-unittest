def calc_tax(amount, tax_rate, age):
    """The function returns the amount of icome tax."""

    if not isinstance(amount, (int, float)):
        raise TypeError('The amount value must be int or float type.')
    if not amount >= 0:
        raise ValueError('The amount value must be positive.')

    if not isinstance(tax_rate, float):
        raise TypeError('The tax_rate must be float type.')
    if not 0 < tax_rate < 1:
        raise ValueError('The tax_rate must be beetwen 0 and 1.')

    if not isinstance(age, int):
        raise TypeError('The age value must be int')
    if not age > 0:
        raise ValueError('The age value must be positive.')

    if age <= 18:
        return int(min(amount * tax_rate, 5000))
    elif age <= 65:
        return int(amount * tax_rate)
    else:
        return int(min(amount * tax_rate, 8000))
