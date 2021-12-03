from collections import Counter
from itertools import repeat
from pathlib import Path


DIAGNOSTIC_REPORT = Path("input.txt")


def read_diagnostic_report(report_file):
    text = DIAGNOSTIC_REPORT.read_text()
    lines = text.splitlines()

    return lines


def get_gamma_rate(bin_numbers: list):
    gamma_digits = []
    for i, lines in enumerate(repeat(bin_numbers, len(bin_numbers[0]))):
        c = Counter(line[i] for line in lines)
        gamma_digits.append(c.most_common()[0][0])

    return int("".join(gamma_digits), 2)


def get_epsilon_rate(bin_numbers: list):
    digits = []
    for i, lines in enumerate(repeat(bin_numbers, len(bin_numbers[0]))):
        c = Counter(line[i] for line in lines)
        digits.append(c.most_common()[1][0])

    return int("".join(digits), 2)


def get_power_consumption(gamma, epsilon):
    return gamma * epsilon


if __name__ == "__main__":
    diagostic_report_lines = read_diagnostic_report(DIAGNOSTIC_REPORT)
    g = get_gamma_rate(diagostic_report_lines)
    e = get_epsilon_rate(diagostic_report_lines)
    power_consumption = get_power_consumption(g, e)

    print(power_consumption)