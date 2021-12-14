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
    def from_file(cls, data_file: Path):
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

    def _fold(self, fold_instruction: FoldInstruction):
        direction, location = fold_instruction
        folded_paper_dots = set()

        if direction == "x":
            line_max = self.height + 1
            other_line_max = self.width + 1

            def is_dot(line, *x_coords):
                return any((x, line) in self.dots for x in x_coords)
        else:
            line_max = self.width + 1
            other_line_max = self.height + 1

            def is_dot(line, *y_coords):
                return any((line, y) in self.dots for y in y_coords)

        for line in range(line_max):
            first_half = range(location - 1, -1, -1)
            second_half = range(location + 1, other_line_max)

            for i, (a, b) in enumerate(reversed(list(zip_longest(first_half, second_half)))):
                if is_dot(line, a, b):
                    if direction == "x": p = (i, line)
                    if direction == "y": p = (line, i)
                    folded_paper_dots.add(p)

        return folded_paper_dots

    def fold(self):
        for fold_instruction in self.fold_instructions:
            folded_paper_dots = self._fold(fold_instruction)
            self.dots = folded_paper_dots
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

