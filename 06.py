if __name__ == '__main__':
    with open('data/06/answers.txt') as f:
        groups_answers = [group for group in f.read().split('\n\n')]

    # Find answers that anyone answered yes to.
    any_yes_per_group = [set(g.replace('\n', '')) for g in groups_answers]
    lens = [len(g) for g in any_yes_per_group]

    print(sum(lens))

    # Find answers that anyone answered yes to.
    lens = []
    for group in groups_answers:
        shared_answers = set(group.replace('\n', ''))

        for person in group.splitlines():
            print(person)
            shared_answers &= set(person)

        lens.append(len(shared_answers))

    print(sum(lens))


