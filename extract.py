import sys

from spreadsheet import Spreadsheet
from viewport import Viewport


if __name__ == '__main__':
    filename = sys.argv[1]

    sheet = Spreadsheet.from_xls(filename, Viewport(2, 1, 12, 4))

    for row in sheet:
        print('{3: >6} {2}'.format(*row))
