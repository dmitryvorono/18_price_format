# Price Formatter

The most frequent question when developing the website is printing on page goods price. For example, database return string like `3245.000000`. You need to format it to more descriptive view `3 245`.

# Requirements

- Python3.6
- Virtualenv(optional)

# How to install

1. Python 3.6 should be already installed
2. Clone or download this repository
4. For testing run:
 
```bash
$ python3.6 -m unittest tests.py 
```

# How to launch

The script have two interface:

1. Programm - import module in your application and use function `format_price(price)`
2. Command line interface. For example, there was format string `2547.280000`:

```bash
python3.6 format_price.py 2547.2800000
```

The result is `2 547.28`

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
