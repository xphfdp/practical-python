import csv


def parse_csv(file, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    """
    Parse a CSV file into a list of records
    """
    if select is not None and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(file, delimiter=delimiter)

    if has_headers:
        # Read the file headers
        headers = next(rows)
    else:
        headers = None

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
    for rowno, row in enumerate(rows):
        try:
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        except ValueError as e:
            if not silence_errors:
                print(f'Row {rowno + 1}: Could\'t convert {row}')
                print(f'Row {rowno + 1}: {e}')
            else:
                pass
    return records
