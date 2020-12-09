import itertools
import time


def read_data(numbers_file):
    with open(numbers_file) as f:
        return [int(n.strip()) for n in f]


if __name__ == '__main__':
    data = read_data('data/09/numbers.txt')

    # Get first number that's not a sum of any pair in the previous 25 numbers.
    for i in range(25, len(data)):
        if all(a + b != data[i] for a, b in itertools.combinations(data[i-25:i], 2)):
            invalid_num = data[i]
            print(f'Invalid number: {invalid_num}')
            break


    # Find the weakness in your XMAS-encrypted list of numbers.
    for contiguous_set_size in range(2, len(data) + 1):
        for i in range(len(data)):
            contiguous_set = data[i:contiguous_set_size]
            if sum(contiguous_set) == invalid_num:
                print(f'Min and max numbers in contiguous set that sum up to invalid number: {max(contiguous_set) + min(contiguous_set)}')

