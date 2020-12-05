from itertools import chain


BOARDING_PASSES_FILE = 'data/05/boarding_passes.txt'


def read_boarding_passes(passes_file):
    with open(passes_file) as f:
        seats = {Seat(specifier.strip()) for specifier in f}

    return seats


class Seat(str):
    @property
    def id(self) -> int:
        mapping = str.maketrans('FBLR', '0101')
        bin_str = self.translate(mapping)

        return int(bin_str, 2)

    @property
    def row(self) -> int:
        return int(self.id / 2**3)

    @property
    def col(self) -> int:
        return int(self.id % 2**4)


if __name__ == '__main__':
    seats = read_boarding_passes(BOARDING_PASSES_FILE)

    # Get max boarding pass ID.
    max_seat_id = max(s.id for s in seats)
    print(max_seat_id)

    # Determine your seat ID.
    all_seat_ids = set(range(2**10))
    missing_seat_ids = (
        all_seat_ids
        - {s.id for s in seats}
        - {s_id for s_id in chain(range(2**3),
                                  range(2**10 - 8, 2**10))}
    )

    # The seats with IDs +1 and -1 will be in the list, so
    # in the missing seats list they will _not_ occur.
    for seat_id in missing_seat_ids:
        if not {seat_id - 1, seat_id + 1} & missing_seat_ids:
            print(seat_id)
            exit()
