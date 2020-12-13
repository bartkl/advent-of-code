from itertools import product


def pause():
    print('...')
    input()


class AdjacentTiles:
    def __init__(self, map_, start):
        self.map = map_
        self.start = start

        self.iterator = zip(*
            [self._get_generator_for_direction(direction)
              for direction in list(product([0, -1, 1], [0, -1, 1]))
              if list(direction) != [0, 0]])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)

    def _get_generator_for_direction(self, direction):
        max_row_idx = len(self.map) - 1
        max_col_idx = len(self.map[0]) - 1

        i = 1
        while True:
            next_row_idx = self.start[0] + i * direction[0]
            next_col_idx = self.start[1] + i * direction[1]
            if ((0 <= next_row_idx <= max_row_idx) and
                (0 <= next_col_idx <= max_col_idx)):
                yield self.map[next_row_idx][next_col_idx]
            else:
                yield 'X'
            i += 1


class SeatLayoutMap:
    def __init__(self, map_file):
        with open(map_file) as f:
            self.map = f.read().splitlines()

    def __iter__(self):
        self.generation = 0
        return self

    def __next__(self):
        next_map = []
        for row_idx in range(len(self.map)):
            next_map_row = ""
            for col_idx in range(len(self.map[row_idx])):
                adjacent_tiles_iter = AdjacentTiles(self.map, [row_idx, col_idx])
                adjacent_tiles = ''.join(next(adjacent_tiles_iter))

                if self.map[row_idx][col_idx] == 'L':
                    if all(t != '#' for t in adjacent_tiles):
                        next_map_row += '#'
                    else:
                        next_map_row += 'L'

                elif self.map[row_idx][col_idx] == '#':
                    adj_occupied_count = adjacent_tiles.count('#')
                    if adj_occupied_count >= 4:
                        next_map_row += 'L'
                    else:
                        next_map_row += '#'

                else:
                    next_map_row += self.map[row_idx][col_idx]  # Or just hardcoded '.'?

            next_map.append(next_map_row)

        if next_map != self.map:
            self.map = next_map
            return self.map
        else:
            raise StopIteration


class SeatLayoutMap2(SeatLayoutMap):
    def __next__(self):
        next_map = []
        for row_idx in range(len(self.map)):
            next_map_row = ""
            for col_idx in range(len(self.map[row_idx])):
                adjacent_tiles_iter = AdjacentTiles(self.map, [row_idx, col_idx])
                adjacent_tiles = ''.join(next(adjacent_tiles_iter))
                del adjacent_tiles_iter

                if self.map[row_idx][col_idx] == 'L':
                    if all(t != '#' for t in adjacent_tiles):
                        next_map_row += '#'
                    else:
                        next_map_row += 'L'

                elif self.map[row_idx][col_idx] == '#':
                    adj_occupied_count = adjacent_tiles.count('#')
                    if adj_occupied_count >= 4:
                        next_map_row += 'L'
                    else:
                        next_map_row += '#'

                else:
                    next_map_row += self.map[row_idx][col_idx]  # Or just hardcoded '.'?

            next_map.append(next_map_row)

        if next_map != self.map:
            self.map = next_map
            return self.map
        else:
            raise StopIteration


if __name__ == '__main__':
    seat_layout_map = SeatLayoutMap('data/map.txt')
    for i, gen in enumerate(seat_layout_map):
        pass
    print(''.join(gen).count('#'))
