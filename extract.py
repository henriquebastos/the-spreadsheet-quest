import sys

from statement import CardStatement


if __name__ == '__main__':
    filename = sys.argv[1]

    stm = CardStatement.from_xls(filename)

    for row in stm:
        print('{3: >6} {2}'.format(*row))
