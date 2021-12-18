from typing import NamedTuple


class Coords(NamedTuple):
    x: int
    y: int

    @classmethod
    def from_tuple(cls, t):
        return cls(t[0], t[1])

    def __add__(self, other):
        return Coords(self[0] + other[0], self[1] + other[1])

    def distance_to(self, other):
        return bool(abs(self.x - other.x) <= 1) ^ bool(abs(self.y - other.y) <= 1)


class Square(NamedTuple):
    top_left: Coords
    top_right: Coords
    bottom_right: Coords
    bottom_left: Coords

    @property
    def left(self):
        return self.top_left.x

    @property
    def top(self):
        return self.top_right.y

    @property
    def right(self):
        return self.bottom_right.x

    @property
    def bottom(self):
        return self.bottom_left.y



TEST_TARGET_AREA = Square(
    top_left=Coords(20, -5), top_right=Coords(30, -5), bottom_right=Coords(30, -10), bottom_left=Coords(20, -10)
)

TARGET_AREA = Square(
    top_left=Coords(195, -67), top_right=Coords(238, -67), bottom_right=Coords(238, -93), bottom_left=Coords(195, -93)
)