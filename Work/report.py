# report.py
#
# Exercise 2.4
import csv
from pprint import pprint


# 购进股票
def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            record = dict(zip(header, row))
            try:
                stock = {
                    'name': record['name'],
                    'shares': int(record['shares']),
                    'price': float(record['price'])
                }
                portfolio.append(stock)
            except ValueError:
                print(f'Bad row: {row}')
    return portfolio


# 卖出股票
def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # header = next(rows)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices


# 计算收益
def calculate(portfolio_file, prices_file):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    gain = 0.0
    loss = 0.0
    for dic in portfolio:
        gain += prices[dic['name']] * dic['shares']
        loss += dic['price'] * dic['shares']
    return gain - loss


# 输出最终数据
def make_report(portfolio, prices):
    report = []
    for dic in portfolio:
        row = (dic['name'], dic['shares'], prices[dic['name']], prices[dic['name']] - dic['price'])
        report.append(row)
    return report


portfolio = read_portfolio('Data/portfolio.csv')
pprint(portfolio)
prices = read_prices('Data/prices.csv')
pprint(prices)
total = calculate("Data/portfolio.csv", "Data/prices.csv")
print(total)
header_tuple = ('Name', 'Shares', 'Price', 'Change')
header = '%10s %10s %10s %10s' % header_tuple
separator = '{:->10s} {:->10s} {:->10s} {:->10s}'.format('-', '-', '-', '-')
print(f'{header}\n{separator}')
for name, shares, price, change in make_report(portfolio, prices):
    advanced_price = '$' + str(price)
    print(f'{name:>10s} {shares:>10d} {advanced_price:>10s} {change:>10.2f}')
