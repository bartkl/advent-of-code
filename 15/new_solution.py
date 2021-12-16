from __future__ import annotations

import pickletools
from pathlib import Path
from functools import lru_cache
from utils import time_performance, pairwise
from typing import NamedTuple, List, Set, Generator
from enum import Enum
from itertools import product, permutations


# def cached_per_path(fn):
#     visited_points: Set[Coords] = set()
#
#     return lru_cache()


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

    def distance_to(self, other):
        return bool(abs(self.i - other.i) <= 1) ^ bool(abs(self.j - other.j) <= 1)


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

    # @cached_per_path
    # @once({})
    # @cached_for_path
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

    # @once([])
    # def paths_generator(self, start_point: Coords, end_point: Coords) -> Generator[List[Coords], None, None]:
    #     """Generates all paths between `start_point` and `end_point`.
    #     """
    #
    #     if start_point == end_point:
    #         yield []
    #         return
    #
    #     for neighbour in self.get_neighbours(start_point):
    #         middle_paths = self.paths_generator(neighbour, end_point)
    #         for middle_path in middle_paths:
    #             yield [start_point] + middle_path + [end_point]

    def paths_generator(self, start_point: Coords, end_point: Coords) -> Generator[List[Coords], None, None]:
        def is_neighbour(p: Coords, q: Coords) -> bool:
            different_points = p != q
            non_diagonal_neighbour = bool(abs(p.i - q.i) == 1) ^ bool(abs(p.j - q.j) == 1)

            return different_points and non_diagonal_neighbour

        all_points = map(Coords.from_tuple, product(range(self.num_rows - 1), range(self.num_cols - 1)))

        for permutation in permutations(all_points):
            if any(not is_neighbour(p, q) for p, q in pairwise(permutation)):
                continue
            yield permutation




@time_performance
def main():
    risk_map = RiskMap.from_file(TEST_DATA_FILE)
    # risk_map.get_neighbours.has_run = False
    # print(risk_map.get_neighbours.has_run)
    # print(risk_map.get_neighbours(Coords(0, 0)))
    # print(risk_map.get_neighbours.has_run)
    # risk_map.get_neighbours.has_run = False
    # risk_map = RiskMap.from_file(TEST_SMALL_DATA_FILE)
    # paths = risk_map.paths_generator(Coords(1, 1), Coords(2, 2))
    paths = risk_map.paths_generator(Coords(0, 0), Coords(9, 9))
    print(next(paths))
    print(next(paths))
    # print(next(paths))
    # pprint(paths)

    # for path in paths:
    #     s = sum(risk_map._data[p.i][p.j] for p in path) - 1
    #     if s < 60:
    #         print(s)



if __name__ == "__main__":
    main()

