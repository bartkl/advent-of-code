from __future__ import annotations

from typing import NamedTuple, Optional, Tuple
from enum import IntEnum


def pause():
    print('... ', end='')
    input()


class Position(NamedTuple):
    vertical: int
    horizontal: int


class Orientation(IntEnum):
    EAST = 0
    NORTH = 90
    WEST = 180
    SOUTH = 270


class Ship:
    def __init__(self,
                 position: Optional[Position] = None,
                 orientation: Optional[Orientation] = None):
        self._position = position or Position(0, 0)
        self._orientation = orientation or Orientation.EAST

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value: Orientation):
        self._orientation = Orientation(value % 360)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value: Position):
        self._position = value

    def update_position(self, value: Tuple[int, int]):
        self._position = Position(self._position.vertical + value[0],
                                  self._position.horizontal + value[1])

    def turn(self, value: Orientation):
        self.orientation = Orientation((self._orientation + value) % 360)

    def move(self, units: int, direction: Optional[Orientation] = None):
        if direction is None:
            direction = self.orientation

        if direction == Orientation.EAST:
            self.update_position((0, units))
        if direction == Orientation.NORTH:
            self.update_position((units, 0))
        if direction == Orientation.WEST:
            self.update_position((0, -units))
        if direction == Orientation.SOUTH:
            self.update_position((-units, 0))

    def do(self, instruction):
        command = instruction[0]
        value = int(instruction[1:])

        print(self.position)
        print(self.orientation)

        if command == 'E':
            self.move(value, Orientation.EAST)
        elif command == 'W':
            self.move(value, Orientation.WEST)
        if command == 'N':
            self.move(value, Orientation.NORTH)
        elif command == 'S':
            self.move(value, Orientation.SOUTH)
        elif command == 'R':
            self.turn(Orientation(-value % 360))
        elif command == 'L':
            self.turn(Orientation(value % 360))
        elif command == 'F':
            self.move(value)


if __name__ == '__main__':
    ship = Ship()

    with open('data/instructions.txt') as instructions:
        for instruction in instructions:
            ship.do(instruction)

        print(ship.position)