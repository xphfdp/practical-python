#!/usr/bin/env python3
# report.py

import fileparse


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    # portfolio = []
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     header = next(rows)
    #     for row in rows:
    #         record = dict(zip(header, row))
    #         try:
    #             stock = {
    #                 'name': record['name'],
    #                 'shares': int(record['shares']),
    #                 'price': float(record['price'])
    #             }
    #             portfolio.append(stock)
    #         except ValueError:
    #             print(f'Bad row: {row}')
    # return portfolio
    with open(filename) as lines:
        return fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])


def read_prices(filename):
    """
    Read prices from a CSV file of name, price data
    """
    # prices = {}
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     # header = next(rows)
    #     for row in rows:
    #         try:
    #             prices[row[0]] = float(row[1])
    #         except IndexError:
    #             pass
    #
    # return prices
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def calculate(portfolio_file, prices_file):
    """
    Calculate some data
    """
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    gain = 0.0
    loss = 0.0
    for dic in portfolio:
        gain += prices[dic['name']] * dic['shares']
        loss += dic['price'] * dic['shares']
    return gain - loss


def make_report(portfolio, prices):
    report = []
    for dic in portfolio:
        row = (dic['name'], dic['shares'], prices[dic['name']], prices[dic['name']] - dic['price'])
        report.append(row)
    return report


def print_report(report):
    header_tuple = ('Name', 'Shares', 'Price', 'Change')
    header = '%10s %10s %10s %10s' % header_tuple
    separator = '{:->10s} {:->10s} {:->10s} {:->10s}'.format('-', '-', '-', '-')
    print(f'{header}\n{separator}')
    for name, shares, price, change in report:
        advanced_price = '$' + str(price)
        print(f'{name:>10s} {shares:>10d} {advanced_price:>10s} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    report = make_report(read_portfolio(portfolio_filename), read_prices(prices_filename))
    print_report(report)


def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
    portfile = argv[1]
    pricefile = argv[2]
    portfolio_report(portfile, pricefile)


if __name__ == '__main__':
    import sys

    main(sys.argv)
