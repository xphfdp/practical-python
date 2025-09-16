#!/usr/bin/env python3
# report.py

import fileparse
import stock
import tableformat

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
        portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])

    return [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts ]


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
        row = (dic.name, dic.shares, prices[dic.name], prices[dic.name] - dic.price)
        report.append(row)
    return report


def print_report(reportdata, formatter):
    # header_tuple = ('Name', 'Shares', 'Price', 'Change')
    # header = '%10s %10s %10s %10s' % header_tuple
    # separator = '{:->10s} {:->10s} {:->10s} {:->10s}'.format('-', '-', '-', '-')
    # print(f'{header}\n{separator}')
    # for name, shares, price, change in report:
    #     advanced_price = '$' + str(price)
    #     print(f'{name:>10s} {shares:>10d} {advanced_price:>10s} {change:>10.2f}')
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricesfile, fmt='txt'):
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricesfile)

    report = make_report(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    if len(argv) != 4:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile fmt')
    portfile = argv[1]
    pricefile = argv[2]
    fmt = argv[3]
    portfolio_report(portfile, pricefile, fmt)


if __name__ == '__main__':
    import sys

    main(sys.argv)
