from collections import Counter
from pathlib import Path


DIAGNOSTIC_REPORT = Path("input.txt")


def read_diagnostic_report(report_file):
    text = DIAGNOSTIC_REPORT.read_text()
    lines = text.splitlines()

    return lines


def get_oxygen_generator_rating(bin_numbers):
    digit_count = len(bin_numbers[0])
    relevant_bin_numbers = [*bin_numbers]
    for i in range(digit_count):
        digits = [b[i] for b in relevant_bin_numbers]
        c = Counter(digits)
        if c.most_common()[0][1] == c.most_common()[1][1]:
            most_common = "1"
        else:
            most_common = c.most_common()[0][0]
        relevant_bin_numbers = list(filter(lambda e: e[i] == most_common, relevant_bin_numbers))
        if len(relevant_bin_numbers) == 1:
            return int(relevant_bin_numbers[0], 2)


def get_co2_scrubber_rating(bin_numbers):
    digit_count = len(bin_numbers[0])
    relevant_bin_numbers = [*bin_numbers]
    for i in range(digit_count):
        digits = [b[i] for b in relevant_bin_numbers]
        c = Counter(digits)
        if c.most_common()[0][1] == c.most_common()[1][1]:
            least_common = "0"
        else:
            least_common = c.most_common()[1][0]
        relevant_bin_numbers = list(filter(lambda e: e[i] == least_common, relevant_bin_numbers))
        if len(relevant_bin_numbers) == 1:
            return int(relevant_bin_numbers[0], 2)


def get_life_support_rating(oxygen_generator_rating, co2_scrubber_rating):
    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == "__main__":
    diagostic_report_lines = read_diagnostic_report(DIAGNOSTIC_REPORT)
    o = get_oxygen_generator_rating(diagostic_report_lines)
    print(o)
    c = get_co2_scrubber_rating(diagostic_report_lines)
    print(c)
    life_support_rating = get_life_support_rating(o, c)

    print(life_support_rating)
