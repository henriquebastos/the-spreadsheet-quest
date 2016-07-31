from spreadsheet import Spreadsheet
from viewport import Viewport


class CardStatement(Spreadsheet):
    viewport = Viewport(2, 1, 12, 4)

    def __str__(self):
        return '\n'.join('{3: >6} {2}'.format(*row) for row in self)
