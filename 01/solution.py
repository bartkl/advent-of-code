from pathlib import Path

DEPTHS = Path("input.txt")


def answer_1():
    increases_count = 0
    text = list(map(int, DEPTHS.read_text().splitlines()))

    for i in range(1, len(text)):
        if text[i] > text[i-1]:
            increases_count += 1

    print(increases_count)


def answer_2():
    increases_count = 0
    text = list(map(int, DEPTHS.read_text().splitlines()))

    for i in range(1, len(text)):
        try:
            s = text[i] + text[i+1] + text[i+2]
            r = text[i-1] + text[i] + text[i+1]
            if s > r:
                increases_count += 1
        except IndexError:
            print(increases_count)
            return

    print(increases_count)


if __name__ == "__main__":
    answer_1()
    # answer_2()
