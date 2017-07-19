import argparse


def format_price(price):
    if not price:
        return ''
    try:
        float_price = float(price)
    except ValueError:
        return ''
    integer_part = int(round(float_price))
    fractional_part = float_price - integer_part
    return ''.join([format_integer_part(integer_part),
                    format_fractional_part(fractional_part)])


def format_integer_part(integer_part):
    count_symbols = 3
    return insert_space_between_symbols(str(integer_part), count_symbols)


def insert_space_between_symbols(string, count_symbols):
    if len(string) <= count_symbols:
        return string
    format_head_string = insert_space_between_symbols(string[:-count_symbols], count_symbols)
    return ''.join([format_head_string, ' ', string[-count_symbols:]])


def format_fractional_part(fractional_part):
    round_coins = 2
    rounded_fractional_part = round(fractional_part, round_coins)
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
