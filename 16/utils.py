Digit = str
HexDigit = Digit
HexStr = str
BinStr = str
HexInt = int


def consume(iterable, n):
    # TODO: Better error handling.
    return "".join(next(iterable) for _ in range(n))


def hex_digit_to_bin(digit: HexDigit) -> BinStr:
    return f"{bin(int(digit, base=16))[2:]:0>4}"


def hex_to_bin(hex_num: str) -> str:
    return "".join(map(hex_digit_to_bin, hex_num))
