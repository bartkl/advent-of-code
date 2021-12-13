from __future__ import annotations
from pathlib import Path
from itertools import zip_longest


TEST_DATA_FILE = Path("test_input.txt")
DATA_FILE = Path("input.txt")


def read_instructions(data_file: Path):
    paper = set()
    folds = []

    for line in map(str.rstrip, data_file.open()):
        if not line:
            continue
        if line.startswith("fold"):
            fold_direction, fold_location = line.split()[2].split("=")
            folds.append((fold_direction, int(fold_location)))
        else:
            paper.add(tuple(map(int, line.split(","))))

    return paper, folds


def fold(paper, fold_instruction):
    paper_width = max(c[0] for c in paper)
    paper_height = max(c[1] for c in paper)

    direction, location = fold_instruction
    folded_paper = set()
    if direction == "x":
        for y in range(paper_height + 1):
            left = range(location - 1, -1, -1)
            right = range(location + 1, paper_width + 1)
            for i, (l, r) in enumerate(reversed(list(zip_longest(left, right)))):
                if (l, y) in paper or (r, y) in paper:
                    folded_paper.add((i, y))
    elif direction == "y":
        for x in range(paper_width + 1):
            top = range(location - 1, -1, -1)
            bottom = range(location + 1, paper_height + 1)
            for i, (t, b) in enumerate(reversed(list(zip_longest(top, bottom)))):
                if (x, t) in paper or (x, b) in paper:
                    folded_paper.add((x, i))
    return folded_paper


def print_paper(paper):
    paper_width = max(c[0] for c in paper)
    paper_height = max(c[1] for c in paper)

    for j in range(paper_height + 1):
        for i in range(paper_width + 1):
            if (i, j) in paper:
                print("#", end='')
            else:
                print(".", end='')
        print()



if __name__ == "__main__":
    paper, fold_instructions = read_instructions(DATA_FILE)

    # Answer 1.
    # for fold_instruction in fold_instructions:
    #     paper = fold(paper, fold_instruction)
    # print(paper)
    # print(len(paper))


    # Answer 2.
    # print_paper(paper)
    for fold_instruction in fold_instructions:

        paper = fold(paper, fold_instruction)
    print_paper(paper)
    # print(len(paper))
