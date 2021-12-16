from typing import Iterable, Optional

Digit = str
HexDigit = Digit
HexStr = str
BinStr = str
HexInt = int


def consume(iterable, n, default=None):
    return "".join(islice(iterable, n))


def hex_digit_to_bin(digit: HexDigit) -> BinStr:
    return f"{bin(int(digit, base=16))[2:]:0>4}"

