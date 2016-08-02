from itertools import chain

import xlrd
from viewport import Viewport


class Spreadsheet:
    viewport = Viewport(0, 0, 1, 1)

    def __init__(self, sheet, viewport=None):
        self.sheet = sheet

        if viewport:
            self.viewport = viewport

    @classmethod
    def from_xls(cls, filename, viewport=None):
        book = xlrd.open_workbook(filename, formatting_info=True)
        sheet = book.sheet_by_index(0)

        return cls(sheet, viewport)

    @property
    def headers(self):
        return [self.sheet.cell_value(i, j) for i, j in self.viewport.rows[0]]

    @property
    def data(self):
        return [[self.sheet.cell_value(i, j) for i, j in indexes]
                for indexes in self.viewport.rows[1:]]

    def __iter__(self):
        return chain([self.headers], self.data)
