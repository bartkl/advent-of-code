from typing import Iterable, Optional

Digit = str
HexDigit = Digit
HexStr = str
BinStr = str
HexInt = int


def consume(iterable: Iterable[str], n: Optional[int] = 1) -> str:
    return "".join(next(iter(iterable)) for _ in range(n))


def hex_digit_to_bin(digit: HexDigit) -> BinStr:
    return f"{bin(int(digit, base=16))[2:]:0>4}"

