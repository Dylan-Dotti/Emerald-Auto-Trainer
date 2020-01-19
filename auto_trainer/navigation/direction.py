from enum import Enum


class Direction(Enum):
    up = 'up'
    down = 'down'
    left = 'left'
    right = 'right'

    @staticmethod
    def from_str(dir_str):
        dir_str = dir_str.lower()
        if dir_str.lower() == 'up':
            return Direction.up
        if dir_str.lower() == 'down':
            return Direction.down
        if dir_str.lower() == 'left':
            return Direction.left
        if dir_str.lower() == 'right':
            return Direction.right

    def get_opposite_direction(self):
        if self is Direction.up:
            return Direction.down
        if self is Direction.down:
            return Direction.up
        if self is Direction.left:
            return Direction.right
        if self is Direction.right:
            return Direction.left
