from __future__ import annotations
from pprint import pprint
from collections import Counter
from operator import itemgetter
from functools import partial, reduce
from typing import List, Tuple, NamedTuple, Set
from pathlib import Path
from enum import IntEnum

TEST_INPUT_FILE = Path("test_input.txt")
INPUT_FILE = Path("input.txt")


class Coords(NamedTuple):
    i: int
    j: int


class Direction(IntEnum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    BOTTOM = 3

    @property
    def indices(self):
        return Coords(*{
            Direction.LEFT: (0, -1),
            Direction.UP: (-1, 0),
            Direction.RIGHT: (0, 1),
            Direction.BOTTOM: (1, 0),
        }[self.value])


class HeightMap:
    @classmethod
    def from_file(cls, text_file: Path):
        data = []
        for line in text_file.open():
            data.append([int(h) for h in line.rstrip("\n")])

        return cls(data)

    def __init__(self, data: List[List[int]]):
        self._data = data

    @property
    def all_points(self):
        points = set()
        for i in range(len(self._data)):
            for j in range(len(self._data[0])):
                points.add(Coords(i, j))
        return points

    def neighbours(self, p: Coords) -> List[Coords]:
        if p.i == 0 and p.j == 0:  # Upper left corner.
            directions = [Direction.RIGHT, Direction.BOTTOM]
        elif p.i == 0 and p.j == len(self._data[0]) - 1:  # Upper right corner.
            directions = [Direction.LEFT, Direction.BOTTOM]
        elif p.i == len(self._data) - 1 and p.j == 0:  # Bottom left corner.
            directions = [Direction.UP, Direction.RIGHT]
        elif p.i == len(self._data) - 1 and p.j == len(self._data[0]) - 1:  # Bottom right corner.
            directions = [Direction.LEFT, Direction.UP]
        elif p.j == 0:  # Left edge.
            directions = [Direction.UP, Direction.RIGHT, Direction.BOTTOM]
        elif p.j == len(self._data[0]) - 1:  # Right edge.
            directions = [Direction.LEFT, Direction.UP, Direction.BOTTOM]
        elif p.i == 0:  # Upper edge.
            directions = [Direction.LEFT, Direction.RIGHT, Direction.BOTTOM]
        elif p.i == len(self._data) - 1:  # Bottom edge.
            directions = [Direction.LEFT, Direction.UP, Direction.RIGHT]
        else:  # Middle points.
            directions = [Direction.LEFT, Direction.UP, Direction.RIGHT, Direction.BOTTOM]

        return [d.indices for d in directions]

    def partition_basins(self):
        basins = []
        remaining_points = sorted({p for p in self.all_points if self._data[p.i][p.j] != 9}, key=lambda p: (p.i, p.j))
        while len(remaining_points) > 0:
            p = next(iter(remaining_points))
            basin = self.fill_basin({p})
            basins.append(basin)

            for q in basin:
                try:
                    remaining_points.remove(q)
                except ValueError:
                    pass

        return basins

    def fill_basin(self, basin: Set[Coords], processed=None):
        if not processed:
            processed = set()

        neighbours = {Coords(p.i + n.i, p.j + n.j)
                      for p in basin - processed
                      for n in self.neighbours(p)
                      if self._data[p.i + n.i][p.j + n.j] != 9}
                      # and n.i >= 0 and n.j >= 0}

        processed.update(basin)
        if len(neighbours) == 0:
            return basin

        return self.fill_basin(basin | neighbours, processed)


if __name__ == "__main__":
    hmap = HeightMap.from_file(INPUT_FILE)
    # basin_1 = {Coords(0, 0)}
    # print(basin_1)
    # basin_2 = {Coords(0, 5)}
    # b1 = hmap.fill_basin(basin_1)
    # print(len(hmap.all_points - b1))
    # b = hmap.fill_basin(basin_2)
    # print(basin_2)
    # print(basins_lst)
    # print(basins)
    basins = hmap.partition_basins()

    pprint(basins)

    c = Counter(len(b) for b in basins)
    print(c)
    print(sorted(c.keys(), reverse=True))



