"""Random walk simulation for a character moving in a 10x10 grid.

The script simulates a single character wandering around inside a
10-by-10 grid. On each step the character chooses one of the four
cardinal directions uniformly at random, while ensuring it stays inside
the grid boundaries. The grid is printed to the console after every
move, providing a simple animation.

Run this file directly to see the character move:

    python random_walk.py

Press ``Ctrl+C`` to stop the simulation early.
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass
from typing import Iterable, Tuple


GRID_WIDTH = 10
GRID_HEIGHT = 10
STEP_DELAY_SECONDS = 0.3


@dataclass(frozen=True)
class Point:
    """Represents a 2D point on the grid."""

    x: int
    y: int

    def move(self, dx: int, dy: int) -> "Point":
        """Return a new point translated by ``(dx, dy)``."""

        return Point(self.x + dx, self.y + dy)


def clamp_position(position: Point) -> Point:
    """Ensure the point stays inside the grid bounds."""

    return Point(
        x=max(0, min(GRID_WIDTH - 1, position.x)),
        y=max(0, min(GRID_HEIGHT - 1, position.y)),
    )


def available_moves() -> Iterable[Tuple[int, int]]:
    """Yield all cardinal-direction moves."""

    yield from ((0, -1), (1, 0), (0, 1), (-1, 0))


def random_walk() -> None:
    """Run the random walk animation until interrupted."""

    position = Point(GRID_WIDTH // 2, GRID_HEIGHT // 2)

    try:
        while True:
            print_board(position)
            dx, dy = random.choice(tuple(available_moves()))
            position = clamp_position(position.move(dx, dy))
            time.sleep(STEP_DELAY_SECONDS)
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")


def print_board(position: Point) -> None:
    """Print the current grid with the character at ``position``."""

    # Clear the screen (ANSI escape sequences work on most terminals).
    print("\033[H\033[J", end="")

    for y in range(GRID_HEIGHT):
        row = []
        for x in range(GRID_WIDTH):
            if position.x == x and position.y == y:
                row.append("@")
            else:
                row.append(".")
        print("".join(row))


if __name__ == "__main__":
    random_walk()
