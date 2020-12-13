from __future__ import annotations

import math
from typing import NamedTuple, Optional, Tuple
from enum import IntEnum


def rotate(origin, point, angle):
    a = math.radians(angle)
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(a) * (px - ox) - math.sin(a) * (py - oy)
    qy = oy + math.sin(a) * (px - ox) + math.cos(a) * (py - oy)

    return int(qx), int(qy)


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


class DifferentShip:
    def __init__(self):
        self._position = Position(0, 0)
        self._waypoint = Position(1, 10)

    @property
    def waypoint(self):
        """Relative to ship's position."""

        return self._waypoint

    @waypoint.setter
    def waypoint(self, value: Position):
        self._waypoint = value

    def update_waypoint(self, value: Tuple[int, int]):
        self._waypoint = Position(self._waypoint.vertical + value[0],
                                  self._waypoint.horizontal + value[1])

    @property
    def waypoint_abs(self):
        return Position(self._position[0] + self._waypoint[0],
                        self._position[1] + self._waypoint[1])

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value: Position):
        self._position = value

    def update_position(self, value: Tuple[int, int]):
        self._position = Position(self._position.vertical + value[0],
                                  self._position.horizontal + value[1])

    def rotate_waypoint(self, value: int):
        new_waypoint_abs = rotate(self.position, self.waypoint_abs, value)
        self.waypoint= Position(new_waypoint_abs[0] - self.position[0],
                                new_waypoint_abs[1] - self.position[1])

    def move(self, units: int):
        for _ in range(units):
            self.position = self.waypoint_abs

    def do(self, instruction):
        command = instruction[0]
        value = int(instruction[1:])

        if command == 'E':
            self.update_waypoint(Position(0, value))
        elif command == 'W':
            self.update_waypoint(Position(0, -value))
        if command == 'N':
            self.update_waypoint(Position(value, 0))
        elif command == 'S':
            self.update_waypoint(Position(-value, 0))
        elif command == 'R':
            self.rotate_waypoint(value)
        elif command == 'L':
            self.rotate_waypoint(-value)
        elif command == 'F':
            self.move(value)


if __name__ == '__main__':
    # 1.
    ship = Ship()

    with open('data/instructions.txt') as instructions:
        for instruction in instructions:
            ship.do(instruction)

    print(f'Manhattan distance: {sum(abs(coord) for coord in ship.position)}')

    # 2.
    ship = DifferentShip()

    with open('data/instructions.txt') as instructions:
        for instruction in instructions:
            ship.do(instruction)

    print(f'Manhattan distance: {sum(abs(coord) for coord in ship.position)}')
