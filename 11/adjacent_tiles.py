from itertools import zip_longest, product


class AdjacentTiles:
    def __init__(self, map_, start, stop_after_first_seat=False, done_char='X'):
        self.map = map_
        self.start = start
        self.stop_after_first_seat = stop_after_first_seat

        self.iterator = zip_longest(*[
            self._get_generator_for_direction(direction)
            for direction in list(product([0, -1, 1], [0, -1, 1]))
            if list(direction) != [0, 0]], fillvalue=done_char)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)

    def _get_generator_for_direction(self, direction):
        i = 1
        while True:
            next_row_idx = self.start[0] + i * direction[0]
            next_col_idx = self.start[1] + i * direction[1]

            # Using `IndexError` does not work: negative indices wrap around.
            if ((0 <= next_row_idx <= len(self.map) - 1) and
                    (0 <= next_col_idx <= len(self.map[0]) - 1)):
                val = self.map[next_row_idx][next_col_idx]
                yield val

                if self.stop_after_first_seat and val in ['L', '#']:
                    # Yield the stop char first, then exhaust.
                    return
                else:
                    i += 1
            else:
                return
