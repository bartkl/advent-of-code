from copy import deepcopy
from pathlib import Path
from typing import List, Optional


TEST_DATA_FILE = Path("test_input.txt")
DATA_FILE = Path("input.txt")


class AlreadyVisitedError(Exception):
    pass


class Cave:
    def __init__(self, name: str):
        self.name: str = name
        self._num_visited = 0

    def __repr__(self):
        return f"<Cave(name={self.name})>"

    def __hash__(self):
        return int.from_bytes(self.name.encode("ascii"), "big")

    def __eq__(self, other):
        return self.name == other.name

    @property
    def visited(self):
        return self._num_visited == 0

    @property
    def num_visited(self):
        return self._num_visited

    def is_small(self):
        return self.name.islower()

    def is_big(self):
        return not self.is_small()

    @num_visited.setter
    def num_visited(self, value):
        if self.is_small() and self._num_visited > 0:
            raise AlreadyVisitedError()

        self._num_visited = value

    def add_connected_path(self):
        pass


def read_data_file(data_file: Path):
    cave_connections = {}
    for line in data_file.open():
        a, b = line.rstrip().split("-")
        cave_connections.setdefault(a, []).append(b)
        cave_connections.setdefault(b, []).append(a)
    return cave_connections


# def build_all_paths(connections, paths: Optional[List[List[str]]] = None):
#     if paths is None:
#         paths = [["start"]]
#
#     i = 0
#     while True:
#         try:
#             path = paths[i]
#         except IndexError:
#             break
#
#         if all(p[-1] == "end" for p in paths):
#             return
#
#         last_cave = path[-1]
#         if last_cave == "end":
#             continue
#
#         continuations = []
#         for next_cave in connections[last_cave]:
#             if next_cave.islower() and next_cave in path:
#                 continue
#             continuations.append(path + [next_cave])
#
#         paths[i:i + 1] = continuations
#         i += len(continuations)
#
#     return build_all_paths(connections, paths)

def build_all_paths(connections, paths: Optional[List[List[str]]] = None):
    if paths is None:
        paths = [["start"]]

    if all(p[-1] == "end" for p in paths):
        return paths

    i = 0
    while True:
        try:
            path = paths[i]
        except IndexError:
            return build_all_paths(connections, paths)

        last_cave = path[-1]
        if last_cave == "end":
            i += 1
            continue

        continuations = []
        for next_cave in connections[last_cave]:
            if next_cave.islower() and next_cave in path:
                continue
            continuations.append(path + [next_cave])

        paths[i:i + 1] = continuations
        i += len(continuations)



if __name__ == "__main__":
    c = read_data_file(DATA_FILE)
    print(c)

    p = build_all_paths(c)
    print(p)
    print(len(p))