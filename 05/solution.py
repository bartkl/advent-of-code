from itertools import chain


def get_seat_id(seat) -> int:
    mapping = str.maketrans('FBLR', '0101')
    bin_str = seat.translate(mapping)

    return int(bin_str, 2)


if __name__ == '__main__':
    with open('data/boarding_passes.txt') as f:
        seat_ids = {get_seat_id(seat.strip()) for seat in f}

    ### Get max boarding pass ID.
    print(f"Highest seat ID in list: {max(seat_ids)}.")

    ### Determine your seat ID.
    missing_seat_ids = set(range(2**10)) - seat_ids

    # All seats are booked, so neighbouring seats with IDs +/- 1 must be in
    # the list, and thus lack in the missing seats list.
    for seat_id in missing_seat_ids:
        if not {seat_id - 1, seat_id + 1} & missing_seat_ids:
            print(f"My seat is the one with ID: {seat_id}.")
