# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    ans = 0
    rows = csv.reader(open(filename))
    header = next(rows)
    for row in rows:
        try:
            ans += int(row[1]) * float(row[2])
        except ValueError:
            print('missing value')
    return ans

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)
