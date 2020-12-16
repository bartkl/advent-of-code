from itertools import chain
from pathlib import Path


def transpose(l):
    r = []
    for i in range(len(l[0])):
        r.append([s[i] for s in l])
    return r


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


def ticket_is_valid(ticket, rules):
    invalid_values = get_invalid_values_from_ticket(ticket, rules)
    return not invalid_values


def get_field_position_options(tickets, rules):
    cols = transpose(tickets)
    options = dict.fromkeys(range(len(cols)))

    for j in options:
        options[j] = set(rules.keys())  # Using `fromkeys` you get many references to one set.

    for i, col in enumerate(cols):
        for val in col:
            for field, value_range in rules.items():
                if val not in value_range:
                    options[i].discard(field)

    return options


def determine_positions(options):
    result = [None] * len(options)

    while None in result:
        for col_idx in options.keys():
            if len(options[col_idx]) == 1:
                val = next(iter(options[col_idx]))
                result[col_idx] = val
                for opts2 in options.values():
                    opts2.discard(val)

    return result





if __name__ == '__main__':
    # Part 1.
    tickets_info = Path('data/tickets_info.txt').read_text()
    # tickets_info = Path('data/test_data.txt').read_text()
    rules_info, own_ticket, nearby_tickets = tickets_info.split('\n\n')

    rules = parse_rules(rules_info)
    invalids = []
    for ticket in map(parse_ticket, nearby_tickets.splitlines()[1:]):
        invalids.extend(get_invalid_values_from_ticket(ticket, rules))

    print(sum(invalids))

    # Part 2.
    valid_tickets = [ticket for ticket in map(parse_ticket, nearby_tickets.splitlines()[1:])
                     if ticket_is_valid(ticket, rules)]


    options = get_field_position_options(valid_tickets, rules)
    positions = determine_positions(options)

    own_ticket = parse_ticket(own_ticket.splitlines()[1])
    p = 1
    for i, field in enumerate(positions):
        if field.startswith('departure'):
            print(i, field)
            p *= own_ticket[i]

    print(p)
