from array import array


def numbers(start_list):
    cache = []
    for i, val in enumerate(start_list, 1):
        cache.append(val)
        yield val

    while True:
        for d, val in enumerate(cache[-2::-1], 1):
            if val == cache[-1]:
                cache.append(d)
                yield d
                break
        else:
            cache.append(0)
            yield cache[-1]

        i += 1


numbers_gen = numbers([0,20,7,16,1,18,15])

for i, number in enumerate(numbers_gen, 1):
    print(f'Number {i} = {number}')
    if i == 2020:
        exit()
