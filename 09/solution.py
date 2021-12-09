from pathlib import Path
from typing import List
from itertools import zip_longest, product


TEST_INPUT_FILE = Path("test_input.txt")
INPUT_FILE = Path("input.txt")


# def _get_generator_for_direction(self, direction):
#     i = 1
#     while True:
#         next_row_idx = self.start[0] + i * direction[0]
#         next_col_idx = self.start[1] + i * direction[1]
#
#         # Using `IndexError` does not work: negative indices wrap around.
#         if ((0 <= next_row_idx <= len(self.map) - 1) and
#                 (0 <= next_col_idx <= len(self.map[0]) - 1)):
#             val = self.map[next_row_idx][next_col_idx]
#             yield val
#
#             if self.stop_after_first_seat and val in ['L', '#']:
#                 # Yield the stop char first, then exhaust.
#                 return
#             else:
#                 i += 1
#         else:
#             return


def read_height_map(text_file: Path):
    height_map = []
    for line in text_file.open():
        height_map.append([int(h) for h in line.rstrip("\n")])

    return height_map


def determine_low_points(height_map: List[List[int]]):
    S = []
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            if i == 0 and j == 0:  # Upper left corner: R,D
                if height_map[i][j] < height_map[i][j + 1] and height_map[i][j] < height_map[i + 1][j]:
                    S.append(height_map[i][j])
            elif i == 0 and j == len(height_map[0]) - 1:  # Upper right corner: L,D
                if height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i + 1][j]:
                    S.append(height_map[i][j])
            elif i == len(height_map) - 1 and j == 0:  # Bottom left corner: R,U
                if height_map[i][j] < height_map[i][j + 1] and height_map[i][j] < height_map[i - 1][j]:
                    S.append(height_map[i][j])
            elif i == len(height_map) - 1 and j == len(height_map[0]) - 1:  # Bottom right corner: L,U
                if height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i - 1][j]:
                    S.append(height_map[i][j])
            elif j == 0:  # Left edge: R,U,D
                if height_map[i][j] < height_map[i][j + 1] and height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i + 1][j]:
                    S.append(height_map[i][j])
            elif j == len(height_map[0]) - 1:  # Right edge: L,U,D
                if height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i - 1][j] and height_map[i][j] < height_map[i + 1][j]:
                    S.append(height_map[i][j])
            elif i == 0:  # Upper edge: L,R,D
                if height_map[i][j] < height_map[i][j + 1] and height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i + 1][j]:
                    S.append(height_map[i][j])
            elif i == len(height_map) - 1:  # Bottom edge: L,R,U
                if height_map[i][j] < height_map[i][j + 1] and height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i - 1][j]:
                    S.append(height_map[i][j])
            else:  # Middle points.
                if height_map[i][j] < height_map[i][j + 1] and height_map[i][j] < height_map[i][j - 1] and height_map[i][j] < height_map[i + 1][j] and height_map[i][j] < height_map[i - 1][j]:
                    S.append(height_map[i][j])
    print(S)
    print(sum(1 + d for d in S))







if __name__ == "__main__":
    m = read_height_map(INPUT_FILE)
    determine_low_points(m)
