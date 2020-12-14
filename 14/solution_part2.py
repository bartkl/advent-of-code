MASK = 'X' * 36
MEM = {}


def address_generator(address):
    x_count = address.count('X')
    x_gen = (f'{n:b}'.zfill(x_count) for n in range(2**x_count))

    for xs in x_gen:
        new_address = address
        for c in xs:
            new_address = new_address.replace('X', c, 1)
        yield new_address


def apply_mask(address):
    bin_val = f'{int(address):036b}'
    generating_val = "".join([t[0] if t[0] in ['X', '1'] else t[1] for t in zip(MASK, bin_val)])
    return generating_val


def parse_instruction(line):
    obj, value = line.strip().split(' = ')
    return obj, value


if __name__ == '__main__':
    with open('data/program.txt') as f:
        for instruction in f:
            obj, val = parse_instruction(instruction)
            if obj == 'mask':
                MASK = val

            elif obj.startswith('mem'):
                address = int(obj[3:].lstrip('[').rstrip(']'))
                new_address = apply_mask(address)
                if 'X' not in new_address:
                    MEM[int(new_address, 2)] = int(val)
                else:
                    address_gen = address_generator(new_address)
                    for address in address_gen:
                        MEM[int(address, 2)] = int(val)

    s = sum(MEM.values())

    print(s)
