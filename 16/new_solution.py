from itertools import islice, tee
from utils import hex_digit_to_bin, HexInt, BinStr, HexStr
from typing import Iterator, Callable
from functools import reduce
import operator


# DATA = "38006F45291200"
DATA = "A052E04CFD9DC0249694F0A11EA2044E200E9266766AB004A525F86FFCDF4B25DFC401A20043A11C61838600FC678D51B8C0198910EA1200010B3EEA40246C974EF003331006619C26844200D414859049402D9CDA64BDEF3C4E623331FBCCA3E4DFBBFC79E4004DE96FC3B1EC6DE4298D5A1C8F98E45266745B382040191D0034539682F4E5A0B527FEB018029277C88E0039937D8ACCC6256092004165D36586CC013A008625A2D7394A5B1DE16C0E3004A8035200043220C5B838200EC4B8E315A6CEE6F3C3B9FFB8100994200CC59837108401989D056280803F1EA3C41130047003530004323DC3C860200EC4182F1CA7E452C01744A0A4FF6BBAE6A533BFCD1967A26E20124BE1920A4A6A613315511007A4A32BE9AE6B5CAD19E56BA1430053803341007E24C168A6200D46384318A6AAC8401907003EF2F7D70265EFAE04CCAB3801727C9EC94802AF92F493A8012D9EABB48BA3805D1B65756559231917B93A4B4B46009C91F600481254AF67A845BA56610400414E3090055525E849BE8010397439746400BC255EE5362136F72B4A4A7B721004A510A7370CCB37C2BA0010D3038600BE802937A429BD20C90CCC564EC40144E80213E2B3E2F3D9D6DB0803F2B005A731DC6C524A16B5F1C1D98EE006339009AB401AB0803108A12C2A00043A134228AB2DBDA00801EC061B080180057A88016404DA201206A00638014E0049801EC0309800AC20025B20080C600710058A60070003080006A4F566244012C4B204A83CB234C2244120080E6562446669025CD4802DA9A45F004658527FFEC720906008C996700397319DD7710596674004BE6A161283B09C802B0D00463AC9563C2B969F0E080182972E982F9718200D2E637DB16600341292D6D8A7F496800FD490BCDC68B33976A872E008C5F9DFD566490A14"


OPERATIONS = {
    "000": sum,
    "001": lambda args: reduce(operator.mul, args, 1),
    "010": min,
    "011": max,
    "101": lambda args: 1 if args[0] > args[1] else 0,
    "110": lambda args: 1 if args[0] < args[1] else 0,
    "111": lambda args: 1 if args[0] == args[1] else 0,
}


def consume(iterable, n, default=None):
    return "".join(islice(iterable, n))


class Decoder(Callable):
    def __init__(self):



def decode(packet: HexStr):
    packet_bin_str = "".join(map(hex_digit_to_bin, packet))
    packet_iter = iter(packet_bin_str)

    def _decode(packet: Iterator) -> int:
        version = consume(packet, 3)
        type_id = consume(packet, 3)

        if type_id == "100":
            number = ""
            while True:
                prefix = next(packet)
                number += consume(packet, 4)

                if prefix == "0":
                    break

            print(int(number, 2))
            return int(number, base=2)

        else:
            length_type_id = next(packet)
            operation = OPERATIONS[type_id]

            if length_type_id == "0":
                subpackets_length = int(consume(packet, 15), 2)
                subpackets = iter(consume(packet, subpackets_length))

                operands = []
                while True:
                    try:
                        val = _decode(subpackets)
                        operands.append(val)
                    except StopIteration:
                        return operation(operands)

            elif length_type_id == "1":
                operands = []
                num_subpackets = int(consume(packet, 11), 2)
                for i in range(num_subpackets):
                    try:
                        operands.append(_decode(packet))
                    except RuntimeError:
                        return operation(operands)
                return operation(operands)

    return _decode(packet_iter)




if __name__ == "__main__":
    v = decode(DATA)
    print(v)