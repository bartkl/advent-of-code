from collections import UserDict


class RuleTree(UserDict):
    @classmethod
    def from_file(cls, rules_file):
        self = cls()

        with open(rules_file) as f:
            for rule in f:
                rule = rule.strip()

                key, values = rule.split(' contain ')

                self[key] = []
                if values == 'no other bags.':
                    continue
                else:
                    values = values.rstrip('.').split(', ')
                    for value in values:
                        amount, bag = value.split(' ', maxsplit=1)
                        self[key].append((int(amount), bag))
        return self

if __name__ == '__main__':
    ruletree = RuleTree.from_file('data/07/rules.txt')
