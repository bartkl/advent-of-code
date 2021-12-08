from operator import attrgetter, itemgetter
from collections import Counter
import string
from pathlib import Path
from enum import IntEnum
from typing import Set


_uppercase_a_to_g = " ".join(string.ascii_uppercase[:7])
Segment = IntEnum("Segment", _uppercase_a_to_g)
Signal = IntEnum("Signal", _uppercase_a_to_g)

DIGITS__SEGMENTS = {
    0: {Segment.A, Segment.B, Segment.C, Segment.E, Segment.F, Segment.G},
    1: {Segment.C, Segment.F},
    2: {Segment.A, Segment.C, Segment.D, Segment.E, Segment.G},
    3: {Segment.A, Segment.C, Segment.D, Segment.F, Segment.G},
    4: {Segment.B, Segment.C, Segment.D, Segment.F},
    5: {Segment.A, Segment.B, Segment.D, Segment.F, Segment.G},
    6: {Segment.A, Segment.B, Segment.D, Segment.E, Segment.F, Segment.G},
    7: {Segment.A, Segment.C, Segment.F},
    8: {Segment.A, Segment.B, Segment.C, Segment.D, Segment.E, Segment.F, Segment.G},
    9: {Segment.A, Segment.B, Segment.C, Segment.D, Segment.F, Segment.G},
}


def read_signal_notes(text_file: Path):
    with text_file.open() as f:
        for line in f:
            signal_patterns, digit_output_values = line.rstrip("\n").split(" | ")
            yield signal_patterns.split(" "), digit_output_values.split(" ")


def decode_signals(signal_patterns, digit_output_values):
    signal_pattern__digit = {}

    for pattern in signal_patterns:
        signal_count = len(pattern)
        for digit, segments in DIGITS__SEGMENTS.items():
            if digit in [1, 4, 7, 8] and signal_count == len(segments):
                signal_pattern__digit["".join(sorted(pattern))] = digit
        # possible_digits = [digit for digit, segments in DIGITS__SEGMENTS.items() if len(pattern) == len(segments)]
        # for d in possible_digits:
        #     segments = DIGITS__SEGMENTS[d]
        #     for s in segments:
        #         possibilities[s].update(segments)
        #
        # for k, in possibilities:
        #     possibilities[k] = SEGMENT_COUNT__DIGITS[len(pattern)]

    print(signal_pattern__digit)
    for pattern in signal_patterns:
        signal_count = len(pattern)
        for digit, segments in DIGITS__SEGMENTS.items():
            if digit in [0, 6, 9] and signal_count == len(segments):
                key_1 = next(filter(lambda i: i[1] == 1, signal_pattern__digit.items()))[0]
                if not set(key_1).issubset(set(pattern)):
                    signal_pattern__digit["".join(sorted(pattern))] = 6
                else:
                    key_4 = next(filter(lambda i: i[1] == 4, signal_pattern__digit.items()))[0]
                    if set(key_4).issubset(set(pattern)):
                        signal_pattern__digit["".join(sorted(pattern))] = 9
                    else:
                        signal_pattern__digit["".join(sorted(pattern))] = 0
            if digit in [2, 3, 5] and signal_count == len(segments):
                key_1 = next(filter(lambda i: i[1] == 1, signal_pattern__digit.items()))[0]
                if set(key_1).issubset(set(pattern)):
                    signal_pattern__digit["".join(sorted(pattern))] = 3
                else:
                    key_4 = next(filter(lambda i: i[1] == 4, signal_pattern__digit.items()))[0]
                    key_4_and_not_key_1 = "".join(sorted(list(set(key_4) - set(key_1))))
                    if set(key_4_and_not_key_1).issubset(set(pattern)):
                        signal_pattern__digit["".join(sorted(pattern))] = 5
                    else:
                        signal_pattern__digit["".join(sorted(pattern))] = 2

    print("End")
    print(signal_pattern__digit)

    decoded_digits = []
    for d in digit_output_values:
        d = "".join(sorted(d))
        decoded_d = signal_pattern__digit[d]
        decoded_digits.append(decoded_d)

    print("Je moeder")
    print(decoded_digits)

    return int("".join(map(str,decoded_digits)))

    # print(mapping)
    # x = ["".join(sorted(d)) for d in digit_output_values]
    # print(x)
    # c = Counter(x)
    # s = sum(1 for pattern, count in c.items() if pattern in mapping.values())
    # return s
    # print(itemgetter(mapping.values())(c))







if __name__ == "__main__":
    input_file = Path("input.txt")
    signal_notes = read_signal_notes(input_file)

    S = []
    for signal_patterns, digit_output_values in signal_notes:
        S.append(decode_signals(signal_patterns, digit_output_values))
        # for d in digit_output_values:
        #     if len(d) in [2,3,4,7]:
        #         S += 1
    print("Je moeder222222222")
    print(sum(S))



