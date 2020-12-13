from seat_layout_map import SeatLayoutMap
from seat_layout_map_look_further import SeatLayoutMapLookFurther


if __name__ == '__main__':
    # 1.
    print(f"Checking adjacent seats...")
    seat_layout_map = SeatLayoutMap('data/map.txt')
    for i, map_generation in enumerate(seat_layout_map, 1):
        if i > 1:
            print('evolved')
        print(f'\tgeneration {i}... ', end='')
    print('stable')
    print()

    print(f"Amount of occupied seats: {''.join(map_generation).count('#')}")
    print()

    # 2.
    print(f"Now, looking around until the first seat is seen in every direction...")
    seat_layout_map_look_further = SeatLayoutMapLookFurther('data/map.txt')
    for i, map_generation in enumerate(seat_layout_map_look_further):
        if i > 1:
            print('evolved')
        print(f'\tgeneration {i}... ', end='')
    print('stable')

    print(f"Amount of occupied seats: {''.join(map_generation).count('#')}")
