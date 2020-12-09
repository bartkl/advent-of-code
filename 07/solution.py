from collections import UserDict
import time


def flatten(l):
    return [item for sublist in l for item in sublist]


class RuleTree(UserDict):
    @classmethod
    def from_file(cls, rules_file):
        self = cls()

        with open(rules_file) as f:
            for rule in f:
                rule = rule.strip()

                key, values = rule.split(' contain ')

                self[key] = {}
                if values == 'no other bags.':
                    continue
                else:
                    values = values.rstrip('.').split(', ')
                    for value in values:
                        amount, bag = value.split(' ', maxsplit=1)
                        if (amount := int(amount)) == 1:
                            # Normalize to plural form.
                            bag += 's'
                        self[key][bag] = amount
        return self

    def _suited_bags_for(self, bags):
        if not bags:
            return set()

        containers = set()
        for bag in bags:
            for container_name, container in self.items():
                if bag in container.keys():
                    containers.add(container_name)

        return containers | self._suited_bags_for(containers)

    def suited_bags_for(self, bag):
        suited_bags = self._suited_bags_for({bag})
        return suited_bags


    def _count_bags_inside(self, keys):
        if not keys:
            return 0

        count = 0
        new_keys = []
        for key in keys:
            count += sum(self[key].values())
            new_keys.extend(flatten([[k] * v for k, v in self[key].items()]))

        return count + self._count_bags_inside(new_keys)

    def count_bags_inside(self, bag):
        return self._count_bags_inside({bag})




if __name__ == '__main__':
    ruletree = RuleTree.from_file('data/rules.txt')

    # Amount of containing bags of shiny gold bag.
    suited_bags = ruletree.suited_bags_for('shiny gold bags')
    print(len(suited_bags))

    # Amount of bags inside my single shiny gold bag.
    bags_inside_shiny_gold = ruletree.count_bags_inside('shiny gold bags')
    print(bags_inside_shiny_gold)



