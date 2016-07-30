import sys
from itertools import chain

import xlrd
from viewport import Viewport


class Spreadsheet:
    def __init__(self, filename):
        book = xlrd.open_workbook(filename, formatting_info=True)
        sheet = book.sheet_by_index(0)

        self.sheet = sheet
        self.vp = Viewport(2, 1, 12, 4)

    @property
    def headers(self):
        return [self.sheet.cell_value(i, j) for i, j in self.vp.rows[0]]

    @property
    def data(self):
        return [[self.sheet.cell_value(i, j) for i, j in indexes]
                for indexes in self.vp.rows[1:]]

    def __iter__(self):
        return chain([self.headers], self.data)


if __name__ == '__main__':
    filename = sys.argv[1]

    sheet = Spreadsheet(filename)

    for row in sheet:
        print('{3: >6} {2}'.format(*row))
