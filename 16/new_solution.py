from utils import consume, hex_digit_to_bin, HexInt, BinStr, HexStr
from typing import Iterator


DATA = "38006F45291200"




def decode(packet: HexStr):
    packet_bin_str = "".join(map(hex_digit_to_bin, packet))
    print(packet_bin_str)

    return _decode(packet_bin_str)


def _decode(packet: Iterator[BinStr]) -> int:
    version = consume(packet, 3)
    print(version)
    # print("".join(d for d in map(hex_digit_to_bin, iter_digits(packet))))




if __name__ == "__main__":
    decode(DATA)