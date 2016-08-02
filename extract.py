import sys
from itertools import chain

import xlrd


def extract(filename):
    book = xlrd.open_workbook(filename, formatting_info=True)
    sheet = book.sheet_by_index(0)

    FIRST_ROW = 2
    FIRST_COL = 1
    LAST_ROW = 12
    LAST_COL = 4

    headers = []
    for j in range(FIRST_COL, LAST_COL + 1):
        value = sheet.cell_value(FIRST_ROW, j)
        headers.append(value)

    data = []
    for i in range(FIRST_ROW + 1, LAST_ROW + 1):
        row = []
        for j in range(FIRST_COL, LAST_COL + 1):
            value = sheet.cell_value(i, j)
            row.append(value)

        data.append(row)

    return headers, data


if __name__ == '__main__':
    filename = sys.argv[1]

    headers, data = extract(filename)

    for row in chain([headers], data):
        print('{3: >6} {2}'.format(*row))
