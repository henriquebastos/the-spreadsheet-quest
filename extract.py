import sys

from statement import CardStatement


if __name__ == '__main__':
    filename = sys.argv[1]

    stm = CardStatement.from_xls(filename)

    print(str(stm))
