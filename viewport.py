

class Viewport(object):
    def __init__(self, top, left, bottom, right):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right


if __name__ == '__main__':
    assert Viewport(2, 1, 12, 4)

    v = Viewport(2, 1, 12, 4)
    assert v.top == 2 and v.left == 1 and v.bottom == 12 and v.right == 4
