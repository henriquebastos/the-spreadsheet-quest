

class Viewport(object):
    def __init__(self, top, left, bottom, right):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right

    def __repr__(self):
        return '{}({}, {}, {}, {})'.format(
            self.__class__.__name__,
            self.top, self.left, self.bottom, self.right
        )

    def __str__(self):
        return '(({}, {}), ({}, {}))'.format(
            self.top, self.left, self.bottom, self.right
        )

    def __eq__(self, other):
        return (self.top == other.top and
                self.left == other.left and
                self.bottom == other.bottom and
                self.right == other.right)

    @property
    def rows(self):
        return RowIterator(self)


class RowIterator:
    def __init__(self, viewport):
        self.vp = viewport

    def __len__(self):
        return self.vp.bottom + 1 - self.vp.top

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self._slice(item)
        else:
            return self._index(item)

    def _index(self, item):
        col_indexes = range(self.vp.left, self.vp.right + 1)
        row_index = self.vp.top + item

        return tuple(tuple((row_index, j) for j in col_indexes))

    def _slice(self, item):
        offset = self.vp.top
        start, stop, step = item.indices(len(self))

        slice_ = slice(start + offset, stop + offset, step)

        col_indexes = range(self.vp.left, self.vp.right + 1)
        row_indexes = range(slice_.start, slice_.stop, slice_.step)

        return tuple((tuple((i, j) for j in col_indexes)
                      for i in row_indexes))


if __name__ == '__main__':
    assert Viewport(2, 1, 12, 4)

    v = Viewport(2, 1, 12, 4)
    assert v.top == 2 and v.left == 1 and v.bottom == 12 and v.right == 4

    assert repr(v) == 'Viewport(2, 1, 12, 4)'
    assert str(v) == '((2, 1), (12, 4))'

    assert Viewport(2, 1, 12, 4) == Viewport(2, 1, 12, 4)

    assert Viewport(0, 0, 1, 1).rows[:] == (((0, 0), (0, 1)), ((1, 0), (1, 1)))
    assert Viewport(0, 0, 1, 1).rows[0] == ((0, 0), (0, 1))

    v = Viewport(0, 0, 3, 1)
    assert RowIterator(v)[1] == ((1, 0), (1, 1))
    assert RowIterator(v)[1:-1] == (((1, 0), (1, 1)), ((2, 0), (2, 1)))
