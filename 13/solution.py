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

            for l, r in zip_longest(left, right):
                if (p := (l, y)) in paper:
                    folded_paper.add(p)
                elif (p := (r, y)) in paper:
                    folded_paper.add(p)
        return folded_paper
    elif direction == "y":
        for x in range(paper_width + 1):
            top = range(location - 1, -1, -1)
            bottom = range(location + 1, paper_height + 1)

            for t, b in zip_longest(top, bottom):
                if (p := (x, t)) in paper:
                    folded_paper.add(p)
                elif (p := (x, b)) in paper:
                    folded_paper.add(p)
        return folded_paper



if __name__ == "__main__":
    paper, fold_instructions = read_instructions(DATA_FILE)

    # Answer 1.
    for fold_instruction in fold_instructions:
        paper = fold(paper, fold_instruction)
        break
    print(paper)
    print(len(paper))


    # Answer 2.
    pass