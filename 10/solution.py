from collections import Counter
from itertools import permutations
from math import prod

import time


def count_arrangements(joltages):
    # Assumes sorted joltages.

    partitioning = []
    last_i = 0
    while last_i < len(joltages):
        p = [j for j in joltages[last_i+1:last_i+5] if j - joltages[last_i] <= 3]
        if not p:
            break
        partitioning.append(p)
        last_i = joltages.index(max(p))

    count = 1
    for i in range(len(partitioning) - 1):
        diff_at_end = partitioning[i+1][0] - partitioning[i][-1]
        size = len(partitioning[i])

        count *= int(2**size - 2**(size - (3 - diff_at_end + 1)))
    return count



if __name__ == '__main__':
    with open('data/joltages.txt') as f:
        joltages = [0] + sorted([int(j.strip()) for j in f])

    joltages.append(max(joltages) + 3)
    print(joltages)

    # 1.
    diffs = []
    for i in range(1, len(joltages)):
        diffs.append(joltages[i] - joltages[i-1])
        prev = joltages[i]

    counts = Counter(diffs)
    print(f'Amount of 1-diffs times 3-diffs: {counts[1] * counts[3]}')

    # 2.
    # print(count_arrangements(joltages))
    print(count_arrangements(joltages))





    # print(joltages)
    # arrs = create_arrangements(joltages, [[0]])
    # print(len(arrs))

    # count = 0
    # for arrangement in permutations(joltages):
    #     if diff_okay(arrangement):
    #         count += 1

    # print(count)


    
    


