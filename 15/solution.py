from __future__ import annotations
from pathlib import Path
from functools import lru_cache
from utils import time_performance, pairwise
from typing import NamedTuple, List, Set
from enum import Enum
from itertools import product, permutations


TEST_DATA_FILE = Path("test_input.txt")
DATA_FILE = Path("input.txt")
TEST_SMALL_DATA_FILE = Path("test_input_small.txt")


class Coords(NamedTuple):
    i: int
    j: int

    @classmethod
    def from_tuple(cls, t):  # NOTE: You cannot override `__new__`, so I do it this way.
        return cls(t[0], t[1])

    def __add__(self, other):
        return Coords(self[0] + other[0], self[1] + other[1])


class Direction(Enum):
    LEFT = Coords(0, -1)
    UP = Coords(-1, 0)
    RIGHT = Coords(0, 1)
    BOTTOM = Coords(1, 0)


class RiskMap:
    @classmethod
    def from_file(cls, data_file: Path):
        with data_file.open() as f:
            stripped_line_iter = map(str.strip, f)
            data = [[int(e) for e in line] for line in stripped_line_iter]

        return cls(data)

    def __init__(self, data: List[List[int]]):
        self._data = data

    @lru_cache()
    def get_neighbours(self, p: Coords) -> Set[Coords]:
        neighbours = set()

        for d in Direction:
            n = p + d.value

            if (0 <= n.i < self.num_rows) and (0 <= n.j < self.num_cols):
                neighbours.add(n)

        return neighbours

    @property
    def num_rows(self):
        return len(self._data)

    @property
    def num_cols(self):
        return len(self._data[0])

    # def determine_paths(self):
    #     bottom_right_point = Coords(self.num_rows - 1, self.num_cols - 1)
    #     all_points = map(Coords.from_tuple, product(range(self.num_rows + 1), range(self.num_cols + 1)))

    def determine_paths(self, remaining_points, paths=None):
        if paths is None:
            paths = [[Coords(0, 0)]]

        bottom_right_point = Coords(self.num_rows - 1, self.num_cols - 1)

        if all((self.get_neighbours(path[-1]) - set(path) == set() or path[-1] == bottom_right_point) for path in paths):
            return paths

        i = 0
        while True:
            try:
                path = paths[i]
            except IndexError:
                return self.determine_paths(paths)

            neighbours = [n for n in self.get_neighbours(path[-1]) if n not in path]

            if not neighbours or path[-1] == bottom_right_point:
                i += 1
                continue

            path_continuations = [path + [n] for n in neighbours]
            paths[i:i + 1] = path_continuations
            i += len(path_continuations)






    # def determine_paths(self, paths=None):
    #     if paths is None:
    #         paths = [[Coords(0, 0)]]
    #
    #     bottom_right_point = Coords(self.num_rows - 1, self.num_cols - 1)
    #
    #     if all((self.get_neighbours(path[-1]) - set(path) == set() or path[-1] == bottom_right_point) for path in paths):
    #         return paths
    #
    #     i = 0
    #     while True:
    #         try:
    #             path = paths[i]
    #         except IndexError:
    #             return self.determine_paths(paths)
    #
    #         neighbours = [n for n in self.get_neighbours(path[-1]) if n not in path]
    #
    #         if not neighbours or path[-1] == bottom_right_point:
    #             i += 1
    #             continue
    #
    #         path_continuations = [path + [n] for n in neighbours]
    #         paths[i:i + 1] = path_continuations
    #         i += len(path_continuations)


@time_performance
def main():
    # risk_map = RiskMap.from_file(TEST_DATA_FILE)
    risk_map = RiskMap.from_file(TEST_SMALL_DATA_FILE)
    paths = risk_map.determine_paths()
    # pprint(paths)

    # for path in paths:
    #     s = sum(risk_map._data[p.i][p.j] for p in path)
    #     print(s)



if __name__ == "__main__":
    main()

