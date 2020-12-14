import time


MASK = 'X' * 36
MEM = {}


def apply_mask(val):
    bin_val = f'{int(val):036b}'
    new_val = "".join([t[0] if t[0] in ['0', '1'] else t[1] for t in zip(MASK, bin_val)])
    # print(f'old val: {bin_val}')
    # print(f'mask   : {MASK}')
    # print(f'new val: {new_val}')
    return new_val


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
                new_val = apply_mask(val)
                MEM[address] = int(new_val, 2)

    s = sum(MEM.values())

    print(s)
