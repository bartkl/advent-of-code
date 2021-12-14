from timeit import default_timer
from collections import Counter
from functools import reduce
from pathlib import Path


TEST_DATA_FILE = Path("test_input.txt")
DATA_FILE = Path("input.txt")


def pairwise(iterable):
    return zip(iter(iterable), iter(iterable[1:]))


def read_instructions(data_file: Path):
    tmpl, rules_str = data_file.read_text().split("\n\n")
    rules = dict((from_.strip(), to.strip()) for from_, to in (line.split(" ->") for line in rules_str.splitlines()))

    return tmpl.strip(), rules


def replacer(rules):
    def perform_replacement(acc, succ):
        pair_str = "".join(succ)
        repl_val = rules.get(pair_str)

        if repl_val:
            return acc + f"{succ[0]}{repl_val}"
        else:
            return acc + "".join(succ)

    return perform_replacement


if __name__ == "__main__":
    start = default_timer()
    tmpl, rules = read_instructions(DATA_FILE)
    end = tmpl
    R = replacer(rules)
    for _ in range(10):
        end = reduce(R, pairwise(end), "") + end[-1]
    c = Counter(end)
    print(max(c.values()) - min(c.values()))
    print(c)
    # print(tmpl)
    # print(rules)

    print(default_timer() - start)