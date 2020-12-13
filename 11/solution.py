from seat_layout_map import SeatLayoutMap
from seat_layout_map_look_further import SeatLayoutMapLookFurther


if __name__ == '__main__':
    # 1.
    # seat_layout_map = SeatLayoutMap('data/map.txt')
    # for i, gen in enumerate(seat_layout_map):
    #     pass
    #
    # print(''.join(gen).count('#'))
    # print(seat_layout_map.generation)

    # 2.
    seat_layout_map2 = SeatLayoutMapLookFurther('data/map.txt')
    for i, gen2 in enumerate(seat_layout_map2):
        print(i)
    print(''.join(gen2).count('#'))
