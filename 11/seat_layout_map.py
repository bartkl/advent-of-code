from adjacent_tiles import AdjacentTiles


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
                    next_map_row += '.'

            next_map.append(next_map_row)

        if next_map != self.map:
            self.map = next_map
            self.generation += 1

            return self.map

        else:
            raise StopIteration
