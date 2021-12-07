from collections import deque, Counter
from pathlib import Path
from more_itertools import nth, consume


def read_puzzle_input(text_file: Path):
    return [int(internal_timer) for internal_timer in text_file.read_text().split(",")]


def count_fish_by_internal_timer(state):
    counts = Counter(state)

    return deque(counts.get(internal_timer, 0) for internal_timer in range(9))


def evolve_fish_population_counts(counts):
    yield counts  # Day 0 counts on initialization.
    while True:
        counts.rotate(-1)
        if counts[8] > 0:
            counts[6] += counts[8]

        yield counts


if __name__ == "__main__":
    initial_internal_timers = read_puzzle_input(Path("input.txt"))
    initial_counts = count_fish_by_internal_timer(initial_internal_timers)
    fish_population_counts_evolution = evolve_fish_population_counts(initial_counts)

    # Question 1, for 80 days.
    # total_fish_count_after_80_days = sum(nth(fish_population_counts_evolution, 80))
    # print(total_fish_count_after_80_days)

    # Question 2, for 256 days.
    total_fish_count_after_80_days = sum(nth(fish_population_counts_evolution, 256))
    print(total_fish_count_after_80_days)
