from timeit import default_timer
from array import array
from itertools import chain

from pathlib import Path
from typing import List, Optional


TEST_DATA_FILE = Path("test_input.txt")
DATA_FILE = Path("input.txt")


def read_data_file(data_file: Path):
    cave_connections = {}
    for line in data_file.open():
        a, b = line.rstrip().split("-")
        cave_connections.setdefault(a, []).append(b)
        cave_connections.setdefault(b, []).append(a)

    caves = set(chain(*cave_connections.values(), cave_connections.keys()))
    caves_int = {0: "start", **{(10 + i) if v.isupper() else i: v for i, v in enumerate((c for c in caves if c not in ["start", "end"]), 1)}, 12: "end"}
    print(caves_int)
    cave_connections_int = {caves_int.index(k): [caves_int.index(_v) for _v in v] for k, v in cave_connections.items()}
    print(cave_connections_int)

    return caves_int, cave_connections_int


def build_all_paths(connections, paths: Optional[List[List[str]]] = None, twice_allowed_cave = None):
    if paths is None:
        paths = [[0]]

    if all(p[-1] == "end" for p in paths):
        return paths

    i = 0
    while True:
        try:
            path = paths[i]
        except IndexError:
            return build_all_paths(connections, paths, twice_allowed_cave)

        last_cave = path[-1]
        if last_cave == 1:
            i += 1
            continue

        continuations = array("b")
        for next_cave in connections[last_cave]:
            if next_cave.islower():
                if next_cave == twice_allowed_cave and path.count(next_cave) == 2:
                    continue
                elif next_cave != twice_allowed_cave and next_cave in path:
                    continue
            continuations.append(path + [next_cave])

        paths[i:i + 1] = continuations
        i += len(continuations)



if __name__ == "__main__":
    start = default_timer()
    # connections = read_data_file(TEST_DATA_FILE)
    caves_int, caves_connections = read_data_file(DATA_FILE)
    # print(c)

    small_caves = set(c for c in chain(*caves_connections.values(), caves_connections.keys()) if c.islower() and c not in (0, 1))
    # {'gt', 'zf', 'so', 'ly', 'ui', 'bt'}

    print(small_caves)
    paths = []
    for twice_allowed_cave in small_caves:
        for path in build_all_paths(caves_connections, twice_allowed_cave=twice_allowed_cave):
            if path not in paths:
                paths.append(path)
    # print(paths)
    print(len(paths))
    print(default_timer() - start)