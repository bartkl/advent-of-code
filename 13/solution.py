from functools import reduce
from math import prod


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def part_1():
    with open('data/notes.txt') as f:
        earliest_timestamp = int(f.readline().strip())
        schedule = [int(s) for s in f.readline().strip().split(',') if s != 'x']

    t = 1
    while True:
        for b in schedule:
            if t % b == 0:
                if t > earliest_timestamp:
                    print(b, t - earliest_timestamp)
                    return
        t += 1


def part_2():
    with open('data/notes.txt') as f:
        f.readline()
        schedule = [int(s) if s != 'x' else None for s in f.readline().strip().split(',')]
        # schedule = [7, 13, None, None, 59, None, 31, 19]

    k = 100908173562
    # k = 1
    # t = 1
    # enumerated_schedule = [(0, 7), (1, 13), (4, 59), (6, 31), (7, 19)]
    enumerated_schedule = [(0, 23), (13, 41), (23, 449), (41, 13), (42, 19), (52, 29), (60, 37), (71, 17)]  # Removed (54, 991): by definition true
    while True:
        t = 991*k - 54
        # t = 59*k - 4

        skip = False
        # for i, b in enumerate(schedule):
        for i, b in enumerated_schedule:
            # if b is None:
            #     continue
            if (t + i) % b != 0:
                skip = True
                break
        if skip:
            k += 1
            continue
        else:
            print(t)
            print(k)
            return


if __name__ == '__main__':
    # 1.
    # part_1()

    # 2.
    # start = time.time()
    # part_2()
    # print(f'Took: {time.time() - start:.6f}')
    enumerated_schedule = [(0, 23), (13, 41), (23, 449), (41, 13), (42, 19), (52, 29), (60, 37), (71, 17)]  # Removed (54, 991): by definition true

    n = [23, 41, 449, 13, 19, 29, 991, 37, 17]
    a = [0, -13, -23, -41, -42, -52, -54, -60, -71]
    N = prod(n)
    print(N)
    print(chinese_remainder(n, a))
