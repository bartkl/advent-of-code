PASSWORDS_FILE = 'data/02/passwords.txt'


def is_valid_password(rule, *, policy_variant):
    policy, password = rule.split(': ')

    char_bounds, char = policy.split(' ')
    char_min, char_max = map(int, char_bounds.split('-'))

    if policy_variant == 'old':
        return int(char_min) <= password.count(char) <= int(char_max)

    elif policy_variant == 'new':
        return (
            bool(password[char_min - 1] == char) ^
            bool(password[char_max - 1] == char))



if __name__ == '__main__':
    # According to the policy at the shopkeepers' old job.
    valid_password_count = 0

    with open(PASSWORDS_FILE) as f:
        for rule in f:
            if is_valid_password(rule, policy_variant='old'):
                valid_password_count += 1

    print(valid_password_count)

    # And according to the new job.
    valid_password_count = 0

    with open(PASSWORDS_FILE) as f:
        for rule in f:
            if is_valid_password(rule, policy_variant='new'):
                valid_password_count += 1

    print(valid_password_count)
