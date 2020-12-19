import copy
from itertools import product
from pprint import pprint


INITIAL_STATE = {
    0: {
        0: dict(enumerate("#.#.##.#")),
        1: dict(enumerate("#.####.#")),
        2: dict(enumerate("...##...")),
        3: dict(enumerate("#####.##")),
        4: dict(enumerate("#....###")),
        5: dict(enumerate("##..##..")),
        6: dict(enumerate("#..####.")),
        7: dict(enumerate("#...#.#.")),
    }
}


# INITIAL_STATE = {
#     0: {
#         0: {0: '.', 1: '#', 2: '.'},
#         1: {0: '.', 1: '.', 2: '#'},
#         2: {0: '#', 1: '#', 2: '#'},
#     }
# }


class PocketDimension:
    def __init__(self, initial_state):
        self.state = initial_state

    def __iter__(self):
        return self

    def _expand_state(self):
        for z, layer in self.state.items():
            row_min_idx = min(layer[0].keys())
            row_max_idx = max(layer[0].keys())

            for row in layer.values():
                # Add new cols for rows in layer.
                # print(max(row.keys()))
                row[row_min_idx - 1] = "."
                row[row_max_idx + 1] = "."

            # Add new rows for layer.
            layer[min(layer.keys()) - 1] = dict.fromkeys(layer[0].keys(), ".")
            layer[max(layer.keys()) + 1] = dict.fromkeys(layer[0].keys(), ".")

        # Add new layers.
        self.state[min(self.state.keys()) - 1] = dict.fromkeys(self.state[0].keys())
        self.state[max(self.state.keys()) + 1] = dict.fromkeys(self.state[0].keys())

        for row_idx in self.state[min(self.state.keys())]:
            self.state[min(self.state.keys())][row_idx] = copy.deepcopy(dict.fromkeys(self.state[0][0].keys(), "."))

        for row_idx in self.state[max(self.state.keys())]:
            self.state[max(self.state.keys())][row_idx] = copy.deepcopy(dict.fromkeys(self.state[0][0].keys(), "."))

    def __next__(self):
        self._expand_state()  # Adds all inactive neighbours.

        next_state = copy.deepcopy(self.state)  # Ensure simultaneous changing.

        for z in self.state:
            for y in self.state[z]:
                for x in self.state[z][y]:
                    neighbours = [self.state.get(z + c, {}).get(y + b, {}).get(x + a, '.')
                                  for (c, b, a) in product((-1, 0, 1), (-1, 0, 1), (-1, 0, 1))
                                  if (c, b, a) != (0, 0, 0)]
                    active_neighbours = [n for n in neighbours if n == '#']
                    if self.state[z][y][x] == '#' and not len(active_neighbours) in [2, 3]:
                        next_state[z][y][x] = '.'
                    elif self.state[z][y][x] == '.' and len(active_neighbours) == 3:
                        next_state[z][y][x] = '#'
                    else:
                        next_state[z][y][x] = self.state[z][y][x]

                    # print(z, y, x)
                    # pprint(self.state[z][y][x])
                    # pprint(active_neighbours)
                    # pprint(next_state[z][y][x])
                    # input()

        self.state = next_state
        return self.state


if __name__ == "__main__":
    pocket_dimension = PocketDimension(INITIAL_STATE)

    val = next(pocket_dimension)
    val = next(pocket_dimension)
    val = next(pocket_dimension)
    val = next(pocket_dimension)
    val = next(pocket_dimension)
    val = next(pocket_dimension)
    print(val)

