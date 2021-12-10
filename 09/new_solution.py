from copy import deepcopy
from collections import Counter
from functools import reduce
import operator
from itertools import product, count
from pathlib import Path
from typing import List, Dict, Tuple, Set, Any
from enum import Enum


Coords = Tuple[int, int]


class Direction(Enum):
    LEFT = (0, -1)
    UP = (-1, 0)
    RIGHT = (0, 1)
    BOTTOM = (1, 0)


TEST_INPUT_FILE = Path("test_input.txt")
INPUT_FILE = Path("input.txt")


class HeightMap:
    @classmethod
    def from_file(cls, text_file: Path):
        data = []
        for line in text_file.open():
            data.append([int(h) for h in line.rstrip("\n")])

        return cls(data)

    def __init__(self, data: List[List[int]]):
        self._data = data

    def __iter__(self):
        """Creates an iterator that yields the indices of the data."""

        return product(range(self.num_rows), range(self.num_cols))

    @property
    def num_rows(self):
        return len(self._data)

    @property
    def num_cols(self):
        return len(self._data[0])

    def get_neighbours(self, i, j):
        neighbours = {}
        for direction in Direction:
            di, dj = direction.value
            ni = i + di
            nj = j + dj

            if (0 <= ni < self.num_rows) and (0 <= nj < self.num_cols):
                neighbours[direction] = (ni, nj)

        return neighbours

    def find_low_points(self):
        low_points: Dict[Coords, int] = {}

        for (i, j) in self:
            if all(self._data[i][j] < self._data[k][l] for k, l in self.get_neighbours(i, j).values()):
                low_points[(i, j)] = self._data[i][j]

        return low_points

    def calculate_risk_level(self, i, j):
        return self._data[i][j] + 1

    def _fill_basin_on_map(self, basin: Set[Coords], hmap_data, basin_tag):
        """Draws out the basins points on the given copy of the height map.

        The height map `hmap_data` is mutated recursively until there's no
        neighbours left to add.
        """

        relevant_neighbours = {
            (ni, nj)
            for (i, j) in basin
            for (ni, nj) in self.get_neighbours(i, j).values()
            if hmap_data[ni][nj] in range(0, 9)}

        for (ni, nj) in basin | relevant_neighbours:
            hmap_data[ni][nj] = basin_tag

        if len(relevant_neighbours) == 0:
            return basin

        return self._fill_basin_on_map(relevant_neighbours, hmap_data, basin_tag)

    def fill_basins_on_map(self) -> List[List[Any]]:
        hmap_data = deepcopy(self._data)
        low_points = self.find_low_points()

        basin_tag_generator = map(str, count())
        for (i, j) in low_points:
            self._fill_basin_on_map({(i, j)}, hmap_data, next(basin_tag_generator))

        return hmap_data


if __name__ == "__main__":
    height_map = HeightMap.from_file(INPUT_FILE)

    # Answer 1.
    low_points = height_map.find_low_points()
    risk = sum(height_map.calculate_risk_level(i, j) for (i, j) in low_points)
    print(risk)

    # Answer 2.
    basins = height_map.fill_basins_on_map()

    basin_counts = Counter(val for (i, j) in height_map if (val := basins[i][j]) != 9)
    three_biggest_basin_sizes = sorted(basin_counts.values(), reverse=True)[:3]
    prod = reduce(operator.mul, three_biggest_basin_sizes, 1)
    print(prod)