from itertools import chain
from pathlib import Path


def range_incl(start, end):
    return range(start, end + 1)


def parse_rules(rules_info):
    rules = {}

    for rule_info in rules_info.splitlines():
        field, ranges = rule_info.split(': ')
        ranges = list(chain(*(range_incl(*map(int, r.split('-')))
                              for r in ranges.split(' or '))))
        rules[field] = ranges

    return rules


def parse_ticket(ticket_info):
    return list(map(int, ticket_info.split(',')))


def get_invalid_values_from_ticket(ticket, rules):
    invalids = []
    for value in ticket:
        for value_range in rules.values():
            if value in value_range:
                break
        else:
            invalids.append(value)

    return invalids


if __name__ == '__main__':
    # Part 1.
    tickets_info = Path('data/tickets_info.txt').read_text()
    rules_info, own_ticket, nearby_tickets = tickets_info.split('\n\n')

    rules = parse_rules(rules_info)
    invalids = []
    for ticket in map(parse_ticket, nearby_tickets.splitlines()[1:]):
        invalids.extend(get_invalid_values_from_ticket(ticket, rules))

    print(sum(invalids))
