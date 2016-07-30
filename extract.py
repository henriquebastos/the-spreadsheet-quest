import sys

from spreadsheet import Spreadsheet


if __name__ == '__main__':
    filename = sys.argv[1]

    sheet = Spreadsheet(filename)

    for row in sheet:
        print('{3: >6} {2}'.format(*row))
