from collections import Counter


def read_joltages(filepath):
    with open(filepath) as f:
        adapters = sorted([int(j.strip()) for j in f])
        return [0] + adapters + [adapters[-1] + 3]


def get_diffs(joltages):
    return [joltages[i] - joltages[i-1] for i in range(1, len(joltages))]


def count_arrangements(joltages):
    """Counts all possible arrangements of adapters.

    Method:
        The joltages are partitioned into classes based on the
    property of being no more than distance three from each other,
    starting from the left. Then, based on the size of the class
    and what joltage follows it immediately (in the next class),
    the amount of possible arrangement of that class are calculated.
      The rough idea behind those calculations is: start out with
    the power set, i.e. all possible arragements of the class, where
    order doesn't matter, and subtract all impossibilities. Based on
    the adjacent class to the right, either 0, 1 or 2 elements can be
    left out, leaving the rest of those elements to generate class
    arrangements which are invalid (a sub power set). These you
    subtract, leaving you with the valid amount of arrangements of the
    class. It was tricky getting this formula generalized!
      From there, you simply imagine a decision tree where you choose
    a valid element from each of the classes which results in an
    arrangement. The multiplication of all the possibilities ends up
    being the result.

    Args:
        joltages: A sorted list of joltages (int).

    Returns:
        Amount of possible joltages arrangements.
    """

    partitioning = []
    i = 0  # Keeps track partitions, not elements.
    while i < len(joltages) - 1:
        p = [j for j in joltages[i+1:i+5] if j - joltages[i] <= 3]
        partitioning.append(p)
        i = joltages.index(max(p))

    count = 1
    for i in range(len(partitioning) - 1):
        diff_at_end = partitioning[i+1][0] - partitioning[i][-1]
        size = len(partitioning[i])

        count *= int(2**size - 2**(size - (3 - diff_at_end + 1)))
    return count


if __name__ == '__main__':
    joltages = read_joltages('data/joltages.txt')

    # 1.
    diffs = get_diffs(joltages)
    diff_counts = Counter(diffs)
    print(f'Amount of 1-diffs times 3-diffs: {diff_counts[1] * diff_counts[3]}')

    # 2.
    print(f'Amount of arrangements: {count_arrangements(joltages)}')
