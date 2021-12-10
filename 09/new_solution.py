from copy import deepcopy
from collections import Counter
from functools import reduce
import operator
from itertools import product, count
from pathlib import Path
from typing import List, Dict, Set, Any, NamedTuple
from enum import Enum


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

        # Another way of doing it which would make `from_tuple` redundant:
        #    return (Coords(i, j) for (i, j) in product(range(self.num_rows), range(self.num_cols)))
        return map(Coords.from_tuple, product(range(self.num_rows), range(self.num_cols)))

    @property
    def num_rows(self):
        return len(self._data)

    @property
    def num_cols(self):
        return len(self._data[0])

    def get_neighbours(self, p: Coords):
        neighbours = {}

        for d in Direction:
            n = p + d.value

            if (0 <= n.i < self.num_rows) and (0 <= n.j < self.num_cols):
                neighbours[d] = n

        return neighbours

    def find_low_points(self):
        low_points: Dict[Coords, int] = {}

        for p in self:
            if all(self._data[p.i][p.j] < self._data[n.i][n.j] for n in self.get_neighbours(p).values()):
                low_points[p] = self._data[p.i][p.j]

        return low_points

    def calculate_risk_level(self, p: Coords):
        return self._data[p.i][p.j] + 1

    def _fill_basin_on_map(self, basin: Set[Coords], hmap, basin_tag):
        """Marks the basin's points on the given height map.

        This function returns when it has marked all the points
        belonging to `basin` on the height map `hmap` with the
        associated `basin_tag`. Note that marking is done by
        replacing the point's value in `hmap` (in-place) by
        `basin_tag`.

        Because `hmap` is mutated, it can be used for other basins
        in later calls, ultimately marking all the basins on this
        `hmap`.

        The way this function finds all the points belonging to
        the basin, is by recursively adding all the neighbours that
        are not yet part of any basin, and don't have value 9. If no
        such neighbours are left to select, the job is done for this
        basin.
        """

        relevant_neighbours = {
            n
            for p in basin
            for n in self.get_neighbours(p).values()
            if hmap[n.i][n.j] in range(0, 9)}

        for n in basin | relevant_neighbours:
            hmap[n.i][n.j] = basin_tag

        if len(relevant_neighbours) == 0:
            return

        return self._fill_basin_on_map(relevant_neighbours, hmap, basin_tag)

    def fill_basins_on_map(self) -> List[List[Any]]:
        """Mars all basins on the height map.

        Makes a copy of the height map so that it can be mutated
        safely. On this copy, basin after basin is marked recursively.

        Makes use of the insight that each low point corresponds
        to exactly one basin, so those are used as starting points
        for filling.
        """

        hmap_data = deepcopy(self._data)
        low_points = self.find_low_points()

        basin_tag_generator = map(str, count())
        for p in low_points:
            self._fill_basin_on_map({p}, hmap_data, next(basin_tag_generator))

        return hmap_data


if __name__ == "__main__":
    height_map = HeightMap.from_file(INPUT_FILE)

    # Answer 1.
    low_points = height_map.find_low_points()
    risk = sum(height_map.calculate_risk_level(p) for p in low_points)
    print(risk)

    # Answer 2.
    basins = height_map.fill_basins_on_map()

    basin_counts = Counter(val for (i, j) in height_map if (val := basins[i][j]) != 9)
    three_biggest_basin_sizes = sorted(basin_counts.values(), reverse=True)[:3]
    prod = reduce(operator.mul, three_biggest_basin_sizes, 1)
    print(prod)