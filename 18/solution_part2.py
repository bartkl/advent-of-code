import operator
from pprint import pprint


def evaluate(expr: str) -> int:
    args = []

    parens_opened = 0
    parens_closed = 0
    sub_expr = ''

    for t in expr:
        if t == '(':
            parens_opened += 1
            if parens_opened - parens_closed == 1:
                continue
        if t == ')':
            parens_closed += 1
            if parens_opened == parens_closed:
                args.append(evaluate(sub_expr))
                sub_expr = ''
        if parens_opened > parens_closed:
            sub_expr += t
            continue

        if t.isdigit():
            if args and args[-1] in ['+', '*']:
                args.append(int(t))
            else:
                if args:
                    args[-1] += int(t)
                else:
                    args.append(int(t))

        elif t in ['+', '*']:
            args.append(t)

    while len(args) != 1:
        try:
            op_idx = args.index('+')
            # print(args)
            args[op_idx - 1 : op_idx + 2] = [args[op_idx - 1] + args[op_idx + 1]]
            # print(args)
            # input()
            continue
        except ValueError:
            pass

        try:
            op_idx = args.index('*')
            # print(op_idx)
            # print(args)
            args[op_idx - 1 : op_idx + 2] = [args[op_idx - 1] * args[op_idx + 1]]
            # print(args)
            # input()
        except ValueError:
            break  # Shouldn't happen.

    return args[0]




if __name__ == "__main__":
    with open("data/homework.txt") as f:
        expressions_sum = sum(evaluate(expression.replace(' ', '').strip())
                              for expression in f)
    print(expressions_sum)

    # with open("data/homework.txt") as f:
    #     expressions = [evaluate(expression.replace(' ', '').strip())
    #                   for expression in f]
    # print(expressions[-1])

    expr = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
    print(evaluate(expr))