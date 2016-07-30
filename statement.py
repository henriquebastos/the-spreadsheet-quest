from spreadsheet import Spreadsheet
from viewport import Viewport


class CardStatement(Spreadsheet):
    viewport = Viewport(2, 1, 12, 4)

    def __str__(self):
        out = []
        for row in self:
            out.append('{3: >6} {2}'.format(*row))
        return '\n'.join(out)
