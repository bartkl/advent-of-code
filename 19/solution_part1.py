from pathlib import Path


SAMPLE_RULES = (
    '0: 4 1 5\n'
    '1: 2 3 | 3 2\n'
    '2: 4 4 | 5 5\n'
    '3: 4 5 | 5 4\n'
    '4: "a"\n'
    '5: "b"\n'
).splitlines()


RECEIVED_MESSAGES = Path('data/received_messages.txt').read_text().split('\n\n')
RULES = RECEIVED_MESSAGES[0].splitlines()
MESSAGES = RECEIVED_MESSAGES[1].splitlines()

VALIDATORS = {}


class ValidationError(Exception):
    pass


def create_primitive_rule_fn(letter):
    def rule_fn(txt):
        if not txt or txt[0] != letter:
            raise ValidationError

        return txt[1:]

    return rule_fn


def create_compound_rule_fn(validators, refs):
    def rule_fn(txt):
        if not txt:
            raise ValidationError

        for ref in refs:
            txt = validators[ref](txt)
        return txt

    return rule_fn


def create_composed_rule_fn(validators, ref_groups):
    def rule_fn(txt):
        if not txt:
            raise ValidationError

        for refs in ref_groups[:-1]:
            try:
                return create_compound_rule_fn(validators, refs)(txt)
            except ValidationError:
                continue

        # The last one has to work.
        return create_compound_rule_fn(validators, ref_groups[-1])(txt)

    return rule_fn


def create_validators(rules):
    for rule_line in rules:
        rule_nr, rule_body = rule_line.strip().split(': ')

        # Primitive.
        if (letter := rule_body.strip('"')).isalpha():
            VALIDATORS[rule_nr] = create_primitive_rule_fn(letter)

        # Composed.
        elif '|' in rule_body:
            rule_ref_groups = [group.split(' ') for group in rule_body.split(' | ')]
            VALIDATORS[rule_nr] = create_composed_rule_fn(VALIDATORS, rule_ref_groups)

        # Compound.
        else:
            refs = rule_body.split(' ')
            VALIDATORS[rule_nr] = create_compound_rule_fn(VALIDATORS, refs)


create_validators(SAMPLE_RULES)
VALIDATORS['0']('aaaabbb')

create_validators(RULES)
count = 0
for msg in MESSAGES:
    try:
        txt = VALIDATORS['0'](msg)
        if not txt:
            count += 1
    except ValidationError:
        pass

print(count)

