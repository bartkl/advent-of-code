from pathlib import Path


RECEIVED_MESSAGES = Path('data/received_messages_patched.txt').read_text().split('\n\n')
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


def validate(txt, start_at_rule='0'):
    txt = VALIDATORS[start_at_rule](txt)

    # Unmatched chars left: invalid.
    return bool(not txt)


if __name__ == "__main__":
    create_validators(RULES)

    count = 0
    for msg in MESSAGES:
        try:
            valid = validate(msg)
            if valid:
                count += 1
        except ValidationError:
            pass

    print(count)

