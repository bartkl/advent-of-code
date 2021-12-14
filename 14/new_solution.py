from collections import Counter
from pathlib import Path
from timeit import default_timer


TEST_DATA_FILE = Path("test_input.txt")
DATA_FILE = Path("input.txt")


def pairwise(iterable):
    return zip(iter(iterable), iter(iterable[1:]))


def read_instructions(data_file: Path):
    polymer_template, rules_str = data_file.read_text().split("\n\n")
    rules = dict((from_.strip(), to.strip()) for from_, to in (line.split(" ->") for line in rules_str.splitlines()))

    return polymer_template.strip(), rules


def progress(counts, rules):
    changes = dict.fromkeys(counts, 0)
    for pair in counts:
        if counts[pair] == 0:
            continue

        new_element = rules[pair]
        new_pairs = (pair[0] + new_element, new_element + pair[1])

        for p in new_pairs:
            changes[p] += counts[pair]

        counts[pair] = 0
    counts.update(changes)


def count_elements(pair_counts):
    counts = Counter(dict.fromkeys(set(el for pair in pair_counts.keys() for el in pair), 0))
    for pair, count in pair_counts.items():
        counts[pair[0]] += count
        counts[pair[1]] += count
    return counts



if __name__ == "__main__":
    start = default_timer()
    template, rules = read_instructions(DATA_FILE)
    init_pairs = [pair[0] + pair[1] for pair in pairwise(template)]
    c = Counter(dict.fromkeys(rules.keys(), 0))
    c.update(init_pairs)
    # print(c)
    for _ in range(40):
        progress(c, rules)
    print(c)
    d = count_elements(c)
    print(max(d.values()))
    print(min(d.values()))
    # print(c)
    print(default_timer() - start)




    # x = progress(x, rules)
