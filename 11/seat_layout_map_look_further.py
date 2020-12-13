from adjacent_tiles import AdjacentTiles
from seat_layout_map import SeatLayoutMap


class SeatLayoutMapLookFurther(SeatLayoutMap):
    def __next__(self):
        next_map = []
        for row_idx in range(len(self.map)):
            next_map_row = ""
            for col_idx in range(len(self.map[0])):
                # adjacent_tiles_iter = AdjacentTiles(self.map, [row_idx, col_idx])
                adjacent_tiles_iter = AdjacentTiles(self.map, [row_idx, col_idx], stop_after_first_seat=True)

                occupied_seat_count = 0
                for adjacent_tiles in adjacent_tiles_iter:
                    occupied_seat_count += ''.join(adjacent_tiles).count('#')

                    if all(c == 'X' for c in adjacent_tiles):
                        break

                if self.map[row_idx][col_idx] == 'L':
                    if occupied_seat_count == 0:
                        next_map_row += '#'
                    else:
                        next_map_row += 'L'

                elif self.map[row_idx][col_idx] == '#':
                    if occupied_seat_count >= 5:
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
