import itertools


EXPENSES_FILE = 'data/01/expenses.txt'


def read_expenses(expenses_filepath):
    with open(expenses_filepath) as expenses_fp:
        return [int(expense)
                for line in expenses_fp
                if (expense := line.strip())]


if __name__ == '__main__':
    expenses = read_expenses(EXPENSES_FILE)

    #  Get product of pairs with sum 2020.
    pairs = itertools.combinations(expenses, 2)

    for p, q in pairs:
        if p + q == 2020:
            print(p * q)


    # Get product of triples with sum 2020.
    triples = itertools.combinations(expenses, 3)

    for p, q, r in triples:
        if p + q  + r== 2020:
            print(p * q * r)
