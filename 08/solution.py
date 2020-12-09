from copy import deepcopy


def parse_boot_code(boot_code_file):
    with open(boot_code_file) as f:
        return [[t[0], int(t[1])]
                for line in f
                if (t := line.strip('\n').split())]


def eval_boot_code(boot_code, line=1, acc=0, cache=None):
    if cache is None:
        cache = set()

    # Return accumulator as soon as a line is recurring.
    if line in cache:
        return line, acc

    cache.add(line)

    try:
        op, arg = boot_code[line]
    except IndexError:
        print(f'terminates')
        return 0, acc

    if op == 'nop':
        line += 1
    elif op == 'acc':
        acc += arg
        line += 1
    elif op == 'jmp':
        line += arg

    return eval_boot_code(boot_code, line, acc, cache)


def replace_nth_instr(boot_code, from_, to, n=0):
    boot_code_copy = deepcopy(boot_code)

    pos = -1
    for i, instr in enumerate(boot_code_copy):
        if instr[0] == from_:
            pos += 1
            if pos == n:
                instr[0] = to
                return boot_code_copy


if __name__ == '__main__':
    boot_code = parse_boot_code('data/boot_code.txt')

    # Get accumulator value just before second execution of line.
    print(eval_boot_code(boot_code))

    # Fix boot code so that it terminates.
    for i in range(len(boot_code)):
        boot_code_copy = replace_nth_instr(boot_code, 'jmp', 'nop', i)
        # boot_code_copy = replace_nth_instr(boot_code, 'nop', 'jmp', i)
        if boot_code_copy:
            status, val = eval_boot_code(boot_code_copy)
            if status == 0:
                print(val)
                break
