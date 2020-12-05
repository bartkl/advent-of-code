BOARDING_PASSES_FILE = 'data/05/boarding_passes.txt'


def get_row_and_col(pass_id):
    row_chars = pass_id[:7]
    col_chars = pass_id[7:]

    row_range = list(range(128))
    for row_char in row_chars:
        if row_char == 'F':
            row_range = row_range[0:len(row_range)//2]
        elif row_char == 'B':
            row_range = row_range[len(row_range)//2:]
    row = row_range[0]

    col_range = list(range(8))
    for col_char in col_chars:
        if col_char == 'L':
            col_range = col_range[0:len(col_range)//2]
        elif col_char == 'R':
            col_range = col_range[len(col_range)//2:]
    col = col_range[0]

    return row, col


if __name__ == '__main__':
    with open(BOARDING_PASSES_FILE) as f:
        seats = []
        for seat_spec in f:
            seats.append(get_row_and_col(seat_spec))

    ids = [8*row + col for row, col in seats]

    print(max(ids))

