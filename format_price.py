import argparse


def format_price(price):
    if not is_correct_price(price):
        return ''
    parts = price.split('.')
    integer_part = parts[0]
    fractional_part = parts[1] if len(parts) > 1 else '0'
    float_fractional_part = float(''.join(['0.', fractional_part]))
    return ''.join([format_integer_part(integer_part),
                    format_fractional_part(float_fractional_part)])


def is_correct_price(price):
    try:
        float(price)
    except TypeError:
        return False
    except ValueError:
        return False
    return True


def format_integer_part(integer_part):
    count_symbols = 3
    reverse = integer_part[::-1]
    divided_reverse = divide_string(reverse, count_symbols)
    return ' '.join(divided_reverse)[::-1]


def divide_string(string, count_symbols):
    return [string[index:index+count_symbols]
            for index in range(0, len(string), count_symbols)]


def format_fractional_part(fractional_part):
    ndigits = 2
    rounded_fractional_part = round(fractional_part, ndigits)
    if not rounded_fractional_part:
        return ''
    return str(rounded_fractional_part)[1:]


def create_args_parser():
    parser = argparse.ArgumentParser(description='This script format input price')
    parser.add_argument('price', type=str, help='Price string')
    return parser


if __name__ == '__main__':
    parser = create_args_parser()
    args = parser.parse_args()
    print(format_price(args.price))
