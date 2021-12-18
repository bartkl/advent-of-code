from itertools import product

from data import TEST_TARGET_AREA, TARGET_AREA, Coords


def mover_gen(start_pos: Coords, start_v: Coords):
    pos = start_pos
    v = start_v

    while True:
        pos += v
        yield pos
        if v.x > 0:
            v = Coords(v.x - 1, v.y)
        v = Coords(v.x, v.y - 1)


def in_target_area(pos: Coords):
    return (TARGET_AREA.left <= pos.x <= TARGET_AREA.right) and\
           (TARGET_AREA.bottom <= pos.y <= TARGET_AREA.top)


def main():
    init_velocities_on_target = []
    # for v in product(range(6, 31), range(-10, 10)):
    for v in product(range(20, 239), range(-94, 94)):
        mover = mover_gen(Coords(0, 0), Coords.from_tuple(v))
        for p in mover:
            if in_target_area(p):
                init_velocities_on_target.append(v)
                break

            if p.x > TARGET_AREA.right or p.y < TARGET_AREA.bottom:
                break

    print(init_velocities_on_target)
    print(len(init_velocities_on_target))


if __name__ == "__main__":
    main()
