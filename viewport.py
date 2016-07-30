

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


if __name__ == '__main__':
    assert Viewport(2, 1, 12, 4)

    v = Viewport(2, 1, 12, 4)
    assert v.top == 2 and v.left == 1 and v.bottom == 12 and v.right == 4

    assert repr(v) == 'Viewport(2, 1, 12, 4)'
    assert str(v) == '((2, 1), (12, 4))'

    assert Viewport(2, 1, 12, 4) == Viewport(2, 1, 12, 4)
