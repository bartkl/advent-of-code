from collections import Counter
from pathlib import Path
from more_itertools import nth

INPUT = Path("input.txt")


def read_initial_state(text_file):
    text = text_file.read_text()
    return Counter(int(internal_timer) for internal_timer in text.split(","))


def decrement_counter_keys(c):
    for key in sorted(c.keys()):
        c[key - 1] = c.pop(key)


def evolve(population):
    while True:
        decrement_counter_keys(population)
        if -1 in population.keys():
            population.update({6: population[-1]})
            population.update({8: population[-1]})
            del population[-1]

        yield population


if __name__ == "__main__":
    init_state = read_initial_state(INPUT)
    e = evolve(init_state)
    x = nth(e, 255)
    print(sum(x.values()))
