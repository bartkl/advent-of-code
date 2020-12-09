from math import prod


MAP_FILE = 'data/map.txt'


def count_trees(slope):
    x_pos, y_pos = 0, 0
    tree_count = 0

    with open(MAP_FILE) as map_:
        row_length = len(map_.readline().strip())  # This also makes you start
                                                   # on the first row.
        while (y_pos := y_pos + 1) and (row := map_.readline().strip()):

            # This moves you to the correct row with respect to the slope.
            if not y_pos % slope[1] == 0:
                continue

            # Wrap around over the x-axis indefinitely.
            x_pos = (x_pos + slope[0]) % row_length

            if row[x_pos] == '#':
                print(f'Tree at position: {x_pos, y_pos}')
                tree_count += 1

    return tree_count


if __name__ == '__main__':
    tree_counts = {f'({x}, {y})': count_trees((x, y))
                   for (x, y) in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))}

    print(f'Tree counts per slope:\n{tree_counts}')
    print()
    print(f'Product of tree counts:\n{prod(tree_counts.values())}')
