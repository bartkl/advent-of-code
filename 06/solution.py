from pathlib import Path
from more_itertools import nth

INPUT = Path("input.txt")


def read_initial_state(text_file):
    text = text_file.read_text()
    return [int(internal_timer) for internal_timer in text.split(",")]


def evolve(population):
    yield population

    while True:
        newly_borns = 0
        for i, fish in enumerate(population):
            if fish == 0:
                population[i] = 6
                newly_borns += 1
            else:
                population[i] -= 1

        population.extend([8] * newly_borns)
        yield population


if __name__ == "__main__":
    init_state = read_initial_state(INPUT)
    print(init_state)
    e = evolve(init_state)
    _80th = nth(e, 256)
    print(len(_80th))
