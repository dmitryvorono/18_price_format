import argparse


def format_price(price):
    if not is_correct_price(price):
        return ''
    integer_part, fractional_part = price.split('.')
    float_fractional_part = float(''.join(['0.', fractional_part])) 
    return ''.join([format_integer_part(integer_part),
                    format_fractional_part(float_fractional_part)])


def is_correct_price(price):
    try:
        float_price = float(price)
    except:
        return False
    return True


def format_integer_part(integer_part):
    count_symbols = 3
    reverse = integer_part[::-1]
    divided_reverse = divide_string(reverse, count_symbols)
    return ' '.join(divided_reverse)[::-1]


def divide_string(string, count_symbols):
    divided_string = []
    for i in range(0, len(string), count_symbols):
        divided_string.append(string[i:i+count_symbols])
    return divided_string


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
