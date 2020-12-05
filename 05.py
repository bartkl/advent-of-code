from itertools import chain


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
    with open('data/05/boarding_passes.txt') as f:
        seats = {Seat(specifier.strip()) for specifier in f}

    # Get max boarding pass ID.
    max_seat_id = max(s.id for s in seats)
    print(f"Highest seat ID in list: {max_seat_id}.")

    # Determine your seat ID.
    all_seat_ids = set(range(2**10))
    missing_seat_ids = (
        all_seat_ids
        - {s.id for s in seats}  # Taken seats.
        - {s_id for s_id in chain(range(2**3),
                                  range(2**10 - 8, 2**10))}  # Lacking first and last rows.
    )

    # The seats with IDs +1 and -1 will be in the list, so
    # in the missing seats list they will not occur.
    for seat_id in missing_seat_ids:
        if not {seat_id - 1, seat_id + 1} & missing_seat_ids:
            print(f"My seat is the one with ID: {seat_id}.")
            exit()
