from pathlib import Path
from typing import NamedTuple, List, Iterable, Optional
from itertools import product
from enum import Enum


TEST_DATA_FILE = Path("test_input.txt")
DATA_FILE = Path("input.txt")


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
    LEFT_UP = LEFT + UP
    RIGHT_UP = RIGHT + UP
    RIGHT_BOTTOM = RIGHT + BOTTOM
    LEFT_BOTTOM = LEFT + BOTTOM


class EnergyLevels:
    @classmethod
    def from_file(cls, data_file: Path):
        data = [[int(e) for e in line.rstrip()] for line in data_file.open()]

        return cls(data)

    def __init__(self, data: List[List[int]]):
        self._data = data
        self.num_flashes = 0

    def __iter__(self):
        return map(Coords.from_tuple, product(range(self.num_rows), range(self.num_cols)))

    def _increment(self, coords: Optional[Iterable[Coords]] = None):
        for p in coords or self:
            self._data[p.i][p.j] += 1

    def _increment_all(self):
        self._increment(self)

    def _increment_neighbours_of_flashing(self):
        processed = set()
        while True:
            flashing_found = False
            for p in self:
                if p in processed: continue
                if self._data[p.i][p.j] > 9:
                    flashing_found = True
                    self.num_flashes += 1
                    processed.add(p)
                    self._increment(self.get_neighbours(p).values())
            if not flashing_found:
                return

    def _set_flashing_to_zero(self):
        for (i, j) in product(range(self.num_rows), range(self.num_cols)):
            if self._data[i][j] > 9:
                self._data[i][j] = 0

    def get_neighbours(self, p: Coords):
        neighbours = {}

        for d in Direction:
            n = p + d.value

            if (0 <= n.i < self.num_rows) and (0 <= n.j < self.num_cols):
                neighbours[d] = n

        return neighbours

    @property
    def num_rows(self):
        return len(self._data)

    @property
    def num_cols(self):
        return len(self._data[0])

    def progress_energy_levels(self):
        self._increment_all()
        self._increment_neighbours_of_flashing()
        self._set_flashing_to_zero()


if __name__ == "__main__":
    energy_levels = EnergyLevels.from_file(DATA_FILE)

    # Answer 1.
    for _ in range(100):
        energy_levels.progress_energy_levels()
    print(energy_levels.num_flashes)

    # Answer 2.
    step = 1
    while True:
        energy_levels.progress_energy_levels()
        if all(energy_levels._data[p.i][p.j] == 0 for p in energy_levels):
            break
        step += 1
    print(step)