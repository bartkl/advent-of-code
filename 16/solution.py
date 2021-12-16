import operator
from functools import reduce
from itertools import islice, tee, takewhile

S = 0
CONSUMED = ""

OPERATIONS = {
            "000": sum,
            "001": lambda args: reduce(operator.mul, args, 1),
            "010": min,
            "011": max,
            "101": lambda args: 1 if args[0] > args[1] else 0,
            "110": lambda args: 1 if args[0] < args[1] else 0,
            "111": lambda args: 1 if args[0] == args[1] else 0,
        }

# DATA = "D2FE28"
# DATA = "620080001611562C8802118E34"
# DATA = "A0016C880162017C3686B18A3D4780"
# DATA = "C0015000016115A2E0802F182340"
# DATA = "38006F45291200"
# DATA = "EE00D40C823060"

# Version sums.
# DATA = "A0016C880162017C3686B18A3D4780"


# DATA = "C200B40A82"  # sum: 3
# DATA = "04005AC33890"  # prd: BROKEN
# DATA = "880086C3E88112"  # min: 7
# DATA = "CE00C43D881120"  # max: 9
# DATA = "D8005AC2A8F0"  # lt: 1
# DATA = "F600BC2D8F"  # gt: 0
# DATA = "9C005AC2F8F0"  # eq: 0
# DATA = "9C0141080250320F1802104A08"  # complicated: 1

# My puzzle input.
DATA = "A052E04CFD9DC0249694F0A11EA2044E200E9266766AB004A525F86FFCDF4B25DFC401A20043A11C61838600FC678D51B8C0198910EA1200010B3EEA40246C974EF003331006619C26844200D414859049402D9CDA64BDEF3C4E623331FBCCA3E4DFBBFC79E4004DE96FC3B1EC6DE4298D5A1C8F98E45266745B382040191D0034539682F4E5A0B527FEB018029277C88E0039937D8ACCC6256092004165D36586CC013A008625A2D7394A5B1DE16C0E3004A8035200043220C5B838200EC4B8E315A6CEE6F3C3B9FFB8100994200CC59837108401989D056280803F1EA3C41130047003530004323DC3C860200EC4182F1CA7E452C01744A0A4FF6BBAE6A533BFCD1967A26E20124BE1920A4A6A613315511007A4A32BE9AE6B5CAD19E56BA1430053803341007E24C168A6200D46384318A6AAC8401907003EF2F7D70265EFAE04CCAB3801727C9EC94802AF92F493A8012D9EABB48BA3805D1B65756559231917B93A4B4B46009C91F600481254AF67A845BA56610400414E3090055525E849BE8010397439746400BC255EE5362136F72B4A4A7B721004A510A7370CCB37C2BA0010D3038600BE802937A429BD20C90CCC564EC40144E80213E2B3E2F3D9D6DB0803F2B005A731DC6C524A16B5F1C1D98EE006339009AB401AB0803108A12C2A00043A134228AB2DBDA00801EC061B080180057A88016404DA201206A00638014E0049801EC0309800AC20025B20080C600710058A60070003080006A4F566244012C4B204A83CB234C2244120080E6562446669025CD4802DA9A45F004658527FFEC720906008C996700397319DD7710596674004BE6A161283B09C802B0D00463AC9563C2B969F0E080182972E982F9718200D2E637DB16600341292D6D8A7F496800FD490BCDC68B33976A872E008C5F9DFD566490A14"


def show(bits_iter):
    original, copy = tee(bits_iter)
    print("".join(list(copy)))
    return original


def hex_to_bin(h):
    return _pad(bin(int(h, base=16))[2:])


def _pad(bits):
    l = len(bits)
    if l % 4 == 0:
        return bits
    else:
        ceiling = int((l / 4) + 1) * 4
        return "0" * (ceiling - l) + bits


def consume(bits_iter, n):
    return "".join(next(bits_iter) for _ in range(n))


def parse_bits_packet():
    global BITS

    version = consume(BITS, 3)
    type_id = consume(BITS, 3)

    # Answer 1.
    global S
    S += int(version, 2)
    # print(S)

    if type_id == "100":
        number = ""
        while True:
            prefix = next(BITS)
            number += consume(BITS, 4)

            if prefix == "0":
                break

        return int(number, base=2)

    else:
        operation = OPERATIONS[type_id]

        length_type_id = next(BITS)
        if length_type_id == "0":
            subpackets_length = int(consume(BITS, 15), 2)
            consumed_before = len(CONSUMED)

            operands = []
            processed_len = 0

            while processed_len < subpackets_length:
                # BITS, bits_copy = tee(BITS)
                # if all(d == "0" for d in list(bits_copy)):
                #     break
                # try:
                n = parse_bits_packet()
                operands.append(n)
                # except RuntimeError:
                    # if type_id == "110":
                    #     print(operands)
                processed_len += (len(CONSUMED) - consumed_before)
            return operation(operands)

        elif length_type_id == "1":
            operands = []
            num_subpackets = int(consume(BITS, 11), 2)
            for i in range(num_subpackets):
                try:
                    operands.append(parse_bits_packet())
                except RuntimeError:
                    return operation(operands)
            return operation(operands)


def iter_with_cursor(iterator):
    global CONSUMED

    for result in iterator:
        CONSUMED += result
        yield result


if __name__ == "__main__":
    bits = hex_to_bin(DATA)
    # print(bits)
    BITS = iter_with_cursor(iter(bits))
    packet = parse_bits_packet()
    print(packet)
    print(S)