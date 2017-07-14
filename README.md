# Price Formatter

The most frequent question when developing the website is printing on page goods price. For example, database return string like `3245.000000`. You need to format it to more descriptive view `3 245`.

# Requirements

- Python3.6
- Virtualenv(optional)

# How to install

1. Python 3.6 should be already installed
2. Clone or download this repository
3. Add permission on executive `format_price.py`
4. For testing run:
 
```bash
$ python3.6 -m unittest tests.py 
```

# How to launch

The script have two interface:

1. Programm - import module in your application and use function `format_price(price)`
2. Command line interface (do not forgot add permissions on exec). For example, there was format string `2547.280000`:

```bash
./format_price.py 2547.2800000
```

The result is `2 547.28`

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)


# Price Formatter

Одна из частых задач при разработке сайта - вывод на странице цен товара. Например, из базы данных приходит строка вида `3245.000000`. Нужно привести её к более наглядному виду `3 245`.

# Требования к окружению

- Python3.6
- Virtualenv(опционально)

# Как установить

1. Python3.6 должен быть установлен
2. Склонировать или загрузить архивом данный репозиторий
3. Выдать права на исполнение файлу `format_price.py`
4. Для проверки работоспособности скрипта запустите тесты:

```bash
$ python3.6 -m unittest tests.py 
```

# Как запустить

Программа имеет два интерфейса:

1. Программный - импортируйте скрипт в ваше приложение и используйте функцию `format_price(price)` 
2. Интерфейс командной строки (не забудьте выдать права на исполнение). В качестве примера ниже произведено форматирование строки `2547.280000`:

```bash
./format_price.py 2547.2800000
```

Полученный результат: `2 547.28`
