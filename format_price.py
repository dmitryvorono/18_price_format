def format_price(price):
    if not price:
        return ''
    try:
        float_price = float(price)
    except ValueError:
        return ''
    integer_part = round(float_price)
    fractional_part = float_price - integer_part
    return ''.join([str(integer_part), format_fractional_part(fractional_part)])


def format_fractional_part(fractional_part):
    round_coins = 2
    rounded_fractional_part = round(fractional_part, round_coins)
    if not rounded_fractional_part:
        return ''
    return str(rounded_fractional_part)[1:]


if __name__ == '__main__':
    print(format_price('3245.000000'))
