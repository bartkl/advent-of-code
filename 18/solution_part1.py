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
                # args.append(sub_expr)
                args.append(evaluate(sub_expr))
                sub_expr = ''
        if parens_opened > parens_closed:
            # if parens_opened == 1 and t == '(':
            #     continue
            sub_expr += t
            continue

        if t.isdigit():
            if args and args[-1] in ['+', '*']:
                args.append(t)
            else:
                if args:
                    args[-1] += t
                else:
                    args.append(t)

        elif t in ['+', '*']:
            args.append(t)

    val = int(args.pop(0))
    while args:
        op = {"+": operator.add, "*": operator.mul}[args.pop(0)]
        n = int(args.pop(0))

        val = op(val, n)

    return val




if __name__ == "__main__":
    with open("data/homework.txt") as f:
        expressions_sum = sum(evaluate(expression.replace(' ', '').strip())
                              for expression in f)
    print(expressions_sum)

    # with open("data/homework.txt") as f:
    #     expressions = [evaluate(expression.replace(' ', '').strip())
    #                   for expression in f]
    # print(expressions[-1])

    # expr = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
    # print(evaluate(expr))