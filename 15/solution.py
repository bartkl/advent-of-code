def numbers(start_list):
    cache = {}

    for i, val in enumerate(start_list, 1):
        cache[val] = i
        yield val
    del cache[val]
    i += 1

    while True:
        prev_val = val
        try:
            val = (i - 1) - cache[val]
        except KeyError:
            val = 0
        finally:
            cache[prev_val] = i - 1
            # print(cache)
            # input()
        yield val
        i += 1


numbers_gen = numbers([0, 20, 7, 16, 1, 18, 15])

for i, number in enumerate(numbers_gen, 1):
    if i == 30000000:
        print(f'Number {i} = {number}')
        exit()
