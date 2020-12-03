from math import prod


MAP_FILE = 'data/03/map.txt'


def count_trees(slope):
    current_pos = [0, 0]
    tree_count = 0

    with open(MAP_FILE) as map_:
        row_length = len(map_.readline().strip())  # Skips first line deliberately.

        while True:
            for _ in range(slope[1]):
                row = map_.readline().strip()
                current_pos[1] += 1

                if not row:
                    return tree_count
            
            current_pos[0] = (current_pos[0] + slope[0]) % row_length

            if row[current_pos[0]] == '#':
                tree_count += 1

    return tree_count


if __name__ == '__main__':
    tree_counts = {str(slope): count_trees(slope)
                   for slope in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))}

    print(f'Tree counts per slope:\n{tree_counts}')
    print()
    print(f'Product of tree counts:\n{prod(tree_counts.values())}')
