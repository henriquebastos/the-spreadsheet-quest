import sys
from itertools import chain

import xlrd
from viewport import Viewport


def extract(filename):
    book = xlrd.open_workbook(filename, formatting_info=True)
    sheet = book.sheet_by_index(0)

    vp = Viewport(2, 1, 12, 4)

    headers = []
    for i, j in vp.rows[0]:
        value = sheet.cell_value(i, j)
        headers.append(value)

    data = []
    for indexes in vp.rows[1:]:
        row = []
        for i, j in indexes:
            value = sheet.cell_value(i, j)
            row.append(value)

        data.append(row)

    return headers, data


if __name__ == '__main__':
    filename = sys.argv[1]

    headers, data = extract(filename)

    for row in chain([headers], data):
        print('{3: >6} {2}'.format(*row))
