from itertools import chain

import xlrd


class Spreadsheet:
    def __init__(self, sheet, viewport):
        self.sheet = sheet
        self.vp = viewport

    @classmethod
    def from_xls(cls, filename, viewport):
        book = xlrd.open_workbook(filename, formatting_info=True)
        sheet = book.sheet_by_index(0)

        return cls(sheet, viewport)

    @property
    def headers(self):
        return [self.sheet.cell_value(i, j) for i, j in self.vp.rows[0]]

    @property
    def data(self):
        return [[self.sheet.cell_value(i, j) for i, j in indexes]
                for indexes in self.vp.rows[1:]]

    def __iter__(self):
        return chain([self.headers], self.data)
