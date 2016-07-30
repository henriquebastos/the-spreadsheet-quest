import sys
from itertools import chain

import xlrd


def extract(filename):
    book = xlrd.open_workbook(filename, formatting_info=True)
    sheet = book.sheet_by_index(0)

    headers = []
    j = 0
    while True:
        value = sheet.cell_value(2, 1 + j)

        if not value:
            break

        headers.append(value)
        j += 1

    data = []
    i = 0
    while True:
        row = []
        j = 0
        while True:
            value = sheet.cell_value(3 + i, 1 + j)

            if not value:
                break

            row.append(value)
            j += 1

        if not row:
            break

        data.append(row)
        i += 1

    return headers, data


if __name__ == '__main__':
    filename = sys.argv[1]

    headers, data = extract(filename)

    for row in chain([headers], data):
        print('{3: >6} {2}'.format(*row))
