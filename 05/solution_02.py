from pathlib import Path


LINES = Path("input.txt")


def read_lines(data_file: Path):
    line_segments = []
    for line in data_file.open():
        p1, p2 = [tuple(map(int, p.split(","))) for p in line.split(" -> ")]
        line_segments.append((p1, p2))

    return line_segments


def count_line_covering(line_segments):
    points_covered = []
    for line in line_segments:
        p1, p2 = line
        if p1[0] == p2[0]:
            q = min(p1[1], p2[1])
            d = abs(p2[1] - p1[1])
            points_covered.extend([(p1[0], q + e) for e in range(d + 1)])
        elif p1[1] == p2[1]:
            q = min(p1[0], p2[0])
            d = abs(p2[0] - p1[0])
            points_covered.extend([(q + e, p1[1]) for e in range(d + 1)])
        # elif (d0 := abs(p2[0] - p1[0])) == (d1 := abs(p2[1] - p1[1])):
        else:
            if p2[0] >= p1[0]:
                p = p1
                q = p2
            else:
                p = p2
                q = p1

            d = abs(q[1] - p[1])
            if q[1] >= p[1]:
                r = [(p[0] + e, p[1] + e) for e in range(d + 1)]
                points_covered.extend(r)
            else:
                r = [(p[0] + e, p[1] - e) for e in range(d + 1)]
                points_covered.extend(r)

    return points_covered


def count_covered_segments(lines):
    counter = {}
    for p in lines:
        if p in counter:
            counter[p] += 1
        else:
            counter[p] = 1

    return counter


if __name__ == "__main__":
    lines = read_lines(LINES)
    print(lines)
    covered = count_line_covering(lines)
    print(covered)

    print(len(covered))
    print(len(set(covered)))

    c = count_covered_segments(covered)
    s = len([v for v in c.values() if v > 1])
    print(s)
