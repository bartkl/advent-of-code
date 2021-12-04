from pathlib import Path


BINGO_DATA = Path("input.txt")


def read_bingo_data(data_file: Path):
    data = data_file.read_text().split("\n\n")

    drawn = [int(d) for d in data[0].split(",")]
    boards = [[[int(d) for d in board_line.split()] for board_line in board.splitlines()] for board in data[1:]]

    return drawn, boards


def _check_for_winner_in_rows(board):
    for row in board:
        if all(n is None for n in row):
            return True
    return False


def _check_for_winner_in_cols(board):
    for i in range(5):
        if all(board[j][i] == board[j+1][i] for j in range(4)):
            return True
    return False


def check_for_winner(boards):
    for board in boards:
        if _check_for_winner_in_rows(board):
            return board
        elif _check_for_winner_in_cols(board):
            return board



def calculate_score(board, last_draw):
    unmarked_sum = sum(n for row in board for n in row if n is not None)

    return last_draw * unmarked_sum


def mark_boards(boards, draw):
    for board in boards:
        for row in board:
            for i in range(len(row)):
                if row[i] == draw:
                    row[i] = None


if __name__ == "__main__":
    numbers_drawn, bingo_boards = read_bingo_data(BINGO_DATA)
    for draw in numbers_drawn:
        mark_boards(bingo_boards, draw)
        winning_board = check_for_winner(bingo_boards)

        if winning_board:
            print(bingo_boards)
            score = calculate_score(winning_board, draw)
            print(score)
            break



