from array import array


def numbers(start_list):
    cache = array('l', [])

    for val in start_list:
        cache.insert(0, val)
        yield val

    while True:
        for d, val in enumerate(cache[1:], 1):
            if val == cache[0]:
                cache.insert(0, d)
                yield d
                break
        else:
            cache.insert(0, 0)
            yield 0


numbers_gen = numbers([0,20,7,16,1,18,15])

for i, number in enumerate(numbers_gen, 1):
    if i == 30000000:
        print(f'Number {i} = {number}')
        exit()
