from collections import UserDict
import time


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




if __name__ == '__main__':
    ruletree = RuleTree.from_file('data/07/rules.txt')
    suited_bags = ruletree.suited_bags_for('shiny gold bags')

    print(suited_bags)
    print(len(suited_bags))

