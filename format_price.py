def format_price(price):
    if not price:
        return ''
    try:
        float_price = float(price)
    except ValueError:
        return ''
    integer_part = int(round(float_price))
    fractional_part = float_price - integer_part
    return ''.join([format_integer_part(integer_part), format_fractional_part(fractional_part)])


def format_integer_part(integer_part):
    return insert_space_between_symbols(str(integer_part), 3)

def insert_space_between_symbols(s, count_symbols):
    if len(s) <= count_symbols:
        return s
    return ''.join([insert_space_between_symbols(s[:-count_symbols], count_symbols), ' ', s[-count_symbols:]])


def format_fractional_part(fractional_part):
    round_coins = 2
    rounded_fractional_part = round(fractional_part, round_coins)
    if not rounded_fractional_part:
        return ''
    return str(rounded_fractional_part)[1:]


if __name__ == '__main__':
    print(format_price('3245.000000'))
