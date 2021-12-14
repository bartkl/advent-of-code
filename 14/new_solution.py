import math
from collections import Counter
from operator import itemgetter
from pathlib import Path
from utils import time_performance, pairwise


TEST_DATA_FILE = Path("test_input.txt")
DATA_FILE = Path("input.txt")


class PolymerFormula:
    def __init__(self, data_file: Path):
        with data_file.open() as f:
            stripped_line_iter = map(str.strip, f)

            template = next(stripped_line_iter)
            next(stripped_line_iter)  # Skip empty line.
            rules = dict((pair, element) for pair, element in (line.split(" -> ") for line in stripped_line_iter))

        self.template = template
        self.rules = rules

        self._init_pair_counts()

    def _init_pair_counts(self):
        template_pairs = ["".join(pair) for pair in pairwise(self.template)]

        self._pair_counts = Counter(dict.fromkeys(self.rules.keys(), 0))
        self._pair_counts.update(template_pairs)

    def _progress_one_step(self):
        changes = Counter(dict.fromkeys(self._pair_counts, 0))

        for pair in self._pair_counts:
            if self._pair_counts[pair] == 0:
                continue

            new_element = self.rules[pair]
            new_pairs = [pair[0] + new_element, new_element + pair[1]]
            changes.update(dict.fromkeys(new_pairs, self._pair_counts[pair]))

            self._pair_counts[pair] = 0

        self._pair_counts.update(changes)

    def progress(self, *, steps=1):
        for _ in range(steps):
            self._progress_one_step()

    @property
    def element_counts(self):
        double_counts = Counter(dict.fromkeys(set(el for pair in self._pair_counts.keys() for el in pair), 0))

        for pair, count in self._pair_counts.items():
            double_counts[pair[0]] += count
            double_counts[pair[1]] += count

        counts = {el: math.ceil(count / 2) for el, count in double_counts.items()}
        return counts


@time_performance
def main():
    polymer_formula = PolymerFormula(TEST_DATA_FILE)

    polymer_formula.progress(steps=10)

    element_counts = polymer_formula.element_counts
    most_common_element = max(element_counts.items(), key=itemgetter(1))
    least_common_element = min(element_counts.items(), key=itemgetter(1))

    print(f"Most common element: {most_common_element[0]} with count {most_common_element[1]}.")
    print(f"Least common element: {least_common_element[0]} with count {least_common_element[1]}.")


if __name__ == "__main__":
    main()
