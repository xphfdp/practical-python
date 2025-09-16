# tableformat.py
import pylab as p


class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TexttableFormatter(TableFormatter):
    """
    Emit a table in plain-text format.
    """

    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format.
    """

    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for r in rowdata:
            print(f'<td>{r}</td>', end='')
        print('</tr>')


class FormatError(Exception):
    pass


def create_formatter(name):
    if not name in ['txt', 'csv', 'html']:
        raise FormatError('Unknown table format %s' % name)
    return TexttableFormatter() if name == 'txt' else CSVTableFormatter() if name == 'csv' else HTMLTableFormatter()


def print_table(portfolio_list, attr_list, tableformat):
    tableformat.headings(attr_list)
    for portfolio in portfolio_list:
        rowdata = [str(getattr(portfolio, attr)) for attr in attr_list]
        tableformat.row(rowdata)
