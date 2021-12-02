from pathlib import Path

INPUT = Path("input.txt")

def _parse_instruction_line(line):
    direction, units = line.split(" ")

    return direction, int(units)



def answer_1():
    instructions = map(_parse_instruction_line, INPUT.open())

    h = 0
    d = 0
    for direction, units in instructions:
        if direction == "forward":
            h += units
        elif direction == "up":
            d -= units
        elif direction == "down":
            d += units

    return h * d





def answer_2():
    instructions = map(_parse_instruction_line, INPUT.open())

    h = 0
    d = 0
    a = 0
    for direction, units in instructions:
        if direction == "forward":
            h += units
            d += a * units
        elif direction == "up":
            a -= units
        elif direction == "down":
            a += units

    print(d)
    print(h)
    return h * d


if __name__ == "__main__":
    # print(answer_1())
    print(answer_2())
