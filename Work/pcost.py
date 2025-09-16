#!usr/bin/env python3
# pcost.py

from report import read_portfolio


def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    # total_cost = 0.0
    #
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     for rowno, row in enumerate(rows, start=1):
    #         record = dict(zip(headers, row))
    #         try:
    #             nshares = int(record['shares'])
    #             price = float(record['price'])
    #             total_cost += nshares * price
    #         except ValueError:
    #             print(f'Row {rowno}: Bad row: {row}')
    #
    # return total_cost
    total_cost = 0.0
    portfolio_list = read_portfolio(filename)
    for dic in portfolio_list:
        total_cost += int(dic.shares) * float(dic.price)
    return total_cost


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfile')

    total_cost = portfolio_cost(argv[1])
    print(f'Total cost: {total_cost}')


if __name__ == '__main__':
    import sys

    main(sys.argv)
