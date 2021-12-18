from itertools import product

from data import TEST_TARGET_AREA, TARGET_AREA, Coords


def move_x(start_pos, start_v):
    pos = start_pos
    v = start_v

    while True:
        pos += v
        yield pos
        if v > 0:
            v -= 1


def move_y(start_pos, start_v):
    pos = start_pos
    v = start_v

    while True:
        pos += v
        yield pos
        v -= 1


def check_x_in_target_area(x_init):
    x_mover = move_x(0, x_init)
    while True:
        pos = next(x_mover)
        if TEST_TARGET_AREA.left <= pos <= TEST_TARGET_AREA.right:
            return True
        if pos > TEST_TARGET_AREA.right:
            return False


def check_y_in_target_area(y_init):
    y_mover = move_y(0, y_init)
    while True:
        pos = next(y_mover)
        if TEST_TARGET_AREA.bottom <= pos <= TEST_TARGET_AREA.top:
            return True
        if pos < TEST_TARGET_AREA.bottom:
            return False


def main():
    x_inits_on_target = []
    for x_init in range(20, 239):
        if check_x_in_target_area(x_init):
            x_inits_on_target.append(x_init)

    print(x_inits_on_target)

    y_inits_on_target = []
    for y_init in range(-94, 68):
        if check_y_in_target_area(y_init):
            y_inits_on_target.append(y_init)

    print(y_inits_on_target)

    print(len(list(product(x_inits_on_target, y_inits_on_target))))


if __name__ == "__main__":
    main()