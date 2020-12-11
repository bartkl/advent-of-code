import time


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
                if self.map[row_idx][col_idx] == 'L':
                    if row_idx == 0:
                        adjacent_rows = self.map[0:2]
                    elif row_idx == len(self.map) - 1:
                        adjacent_rows = self.map[row_idx-1:row_idx+1]
                    else:
                        adjacent_rows = self.map[row_idx-1:row_idx+2]

                    if col_idx == 0:
                        adjacent_tiles = [row[0:2] for row in adjacent_rows]
                    elif col_idx == len(self.map[0]) - 1:
                        adjacent_tiles = [row[col_idx-1:col_idx+1] for row in adjacent_rows]
                    else:
                        adjacent_tiles = [row[col_idx-1:col_idx+2] for row in adjacent_rows]

                    if all(t != '#' for t in ''.join(adjacent_tiles)):
                        next_map_row += '#'
                    else:
                        next_map_row += 'L'

                elif self.map[row_idx][col_idx] == '#':
                    # TODO: Make DRY.
                    if row_idx == 0:
                        adjacent_rows = self.map[0:2]
                    elif row_idx == len(self.map) - 1:
                        adjacent_rows = self.map[row_idx-1:row_idx+1]
                    else:
                        adjacent_rows = self.map[row_idx-1:row_idx+2]

                    if col_idx == 0:
                        adjacent_tiles = [row[0:2] for row in adjacent_rows]
                    elif col_idx == len(self.map[0]) - 1:
                        adjacent_tiles = [row[col_idx-1:col_idx+1] for row in adjacent_rows]
                    else:
                        adjacent_tiles = [row[col_idx-1:col_idx+2] for row in adjacent_rows]

                    adj_occupied_count = ''.join(adjacent_tiles).count('#') - 1  # -1 for the current tile.

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
    for gen in seat_layout_map:
        pass
    print(''.join(gen).count('#'))
