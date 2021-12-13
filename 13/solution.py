from __future__ import annotations
from pathlib import Path
from itertools import zip_longest
from typing import Set, List, Tuple


PaperDot = Tuple[int, int]
PaperDots = Set[PaperDot]
FoldInstruction = Tuple[str, int]
FoldInstructions = List[FoldInstruction]


TEST_DATA_FILE = Path("test_input.txt")
DATA_FILE = Path("input.txt")


class Paper:
    @classmethod
    def from_file(cls, data_file: Path) -> Paper:
        instructions = data_file.read_text().split("\n\n")

        paper_dots = {(int(x), int(y)) for x, y in (line.split(",") for line in instructions[0].splitlines())}
        fold_instructions = [(direction, int(location)) for direction, location in (line.split()[-1].split("=") for line in instructions[1].splitlines())]

        return cls(paper_dots, fold_instructions)

    def __init__(self, dots: PaperDots, fold_instructions: FoldInstructions):
        self.dots = dots
        self.fold_instructions = iter(fold_instructions)

    @property
    def width(self):
        return max(c[0] for c in self.dots)

    @property
    def height(self):
        return max(c[1] for c in self.dots)

    def fold(self):
        for fold_instruction in self.fold_instructions:
            direction, location = fold_instruction
            folded_paper = set()

            if direction == "x":
                for y in range(self.height + 1):
                    left = range(location - 1, -1, -1)
                    right = range(location + 1, self.width + 1)
                    for i, (l, r) in enumerate(reversed(list(zip_longest(left, right)))):
                        if (l, y) in self.dots or (r, y) in self.dots:
                            folded_paper.add((i, y))
            elif direction == "y":
                for x in range(self.width + 1):
                    top = range(location - 1, -1, -1)
                    bottom = range(location + 1, self.height + 1)
                    for i, (t, b) in enumerate(reversed(list(zip_longest(top, bottom)))):
                        if (x, t) in self.dots or (x, b) in self.dots:
                            folded_paper.add((x, i))
            self.dots = folded_paper
            yield self.dots


    def print(self):
        for j in range(self.height + 1):
            for i in range(self.width + 1):
                if (i, j) in paper.dots:
                    print("#", end='')
                else:
                    print(".", end='')
            print()


if __name__ == "__main__":
    paper = Paper.from_file(TEST_DATA_FILE)
    fold = paper.fold()
    print(f"Answer to question 1: {len(paper.dots)}.")

    for _ in fold: pass  # Perform all other folds.
    print(f"Answer to question 2 can be read from the following print:\n")
    paper.print()

