from itertools import cycle, chain
from pathlib import Path
from typing import Optional, Iterator, Generator, List
from more_itertools import consume, nth


LanternFish = Iterator
LanternFishPopulation = Generator


INPUT_DATA = Path("input.txt")


def lantern_fish(start: Optional[int] = 8) -> LanternFish:
    internal_timer_states = range(6, -1, -1)
    life_cycle = cycle(internal_timer_states)

    if start == 8:
        return chain((8, 7), life_cycle)

    consume(life_cycle, 6 - start)
    return life_cycle


def create_lantern_fish_population(internal_timers: List[int]) -> List[LanternFish]:
    return list(map(lantern_fish, internal_timers))


def lantern_fish_population(initial_population: List[int]) -> LanternFishPopulation:
    population = create_lantern_fish_population(initial_population)
    yield [next(fish) for fish in population]  # Priming.

    while True:
        curr_internal_timers = []
        for i, fish in enumerate(population):
            internal_timer = next(fish)
            if internal_timer == 6:
                population.append(lantern_fish())
            curr_internal_timers.append(internal_timer)

        yield curr_internal_timers


def read_initial_state(text_file: Path) -> List[int]:
    text = text_file.read_text()
    return [int(internal_timer) for internal_timer in text.split(",")]


if __name__ == "__main__":
    initial_state = read_initial_state(INPUT_DATA)
    e = lantern_fish_population(initial_state)
    after_80_days = nth(e, 80)
    print(len(after_80_days))
