from pathlib import Path


TEST_DATA_FILE = Path("test_input.txt")
DATA_FILE = Path("input.txt")


def read_data(data_file: Path):
    return data_file.read_text().splitlines()


PARENS = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">",
}

CORRUPT_SCORING = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

INCOMPLETE_SCORING = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

def parse_line(line: str):
    open_chars = []
    for char in line:
        if char in PARENS.keys():
            open_chars.append(char)
        elif char in PARENS.values():
            if char != PARENS[open_chars[-1]]:
                return char
            else:
                open_chars.pop()


def handle_incomplete_line(line: str):
    open_chars = []
    for char in line:
        if char in PARENS.keys():
            open_chars.append(char)
        elif char in PARENS.values():
            open_chars.pop()

    score = 0
    for char in open_chars[::-1]:
        score *= 5
        score += INCOMPLETE_SCORING[PARENS[char]]

    return score


if __name__ == "__main__":
    lines = read_data(DATA_FILE)
    corrupt_score = 0
    incomplete_score = []

    for i, line in enumerate(lines):
        result = parse_line(line)
        if result is not None:
            # print(result)
            # Corrupt.
            corrupt_score += CORRUPT_SCORING[result]
        else:
            # Incomplete.
            _score = handle_incomplete_line(line)
            incomplete_score.append(_score)
    print(sorted(incomplete_score)[int(len(incomplete_score) / 2)])


