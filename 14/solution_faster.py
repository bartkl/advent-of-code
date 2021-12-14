from timeit import default_timer
from array import array
from collections import Counter
from pathlib import Path


TEST_DATA_FILE = Path("test_input.txt")
DATA_FILE = Path("input.txt")


def read_instructions(data_file: Path):
    tmpl, rules_str = data_file.read_text().split("\n\n")
    rules = dict((from_.strip(), to.strip()) for from_, to in (line.split(" ->") for line in rules_str.splitlines()))

    return array("u", tmpl.strip()), rules


def replace(s: array, rules):
    i = 0
    while True:
        if i == len(s) - 1:
            counts = Counter(s)
            return s, counts

        pair = s[i] + s[i + 1]
        val = rules.get(pair)
        s.insert(i + 1 , val)

        i += 2


if __name__ == "__main__":
    start = default_timer()
    tmpl, rules = read_instructions(TEST_DATA_FILE)
    end = tmpl
    c = None
    for i in range(1):
        end, c = replace(end, rules)
    print(end)
    print(max(c.values()) - min(c.values()))
    print(default_timer() - start)
