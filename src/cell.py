from __future__ import annotations

from point import Point
from line  import Line
from window import Window


class Cell:
    def __init__(self, upper_left_corner: Point, lower_right_corner: Point, window: Window) -> None:
        # [top, right, bottom, left]
        self.walls = [True] * 4

        self._upper_left  = upper_left_corner
        self._lower_right = lower_right_corner

        self._window: Window = window

        return

    def draw(self) -> None:
        TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3
        draw_walls = []

        if self.walls[LEFT]:
            x, y1, y2 = self._upper_left.x, self._upper_left.y, self._lower_right.y
            line = Line(Point(x, y1), Point(x, y2))

            draw_walls.append(line)

        if self.walls[TOP]:
            y, x1, x2 = self._upper_left.y, self._upper_left.x, self._lower_right.x
            line = Line(Point(x1, y), Point(x2, y))

            draw_walls.append(line)
        if self.walls[RIGHT]:
            x, y1, y2 = self._lower_right.x, self._upper_left.y, self._lower_right.y
            line = Line(Point(x, y1), Point(x, y2))

            draw_walls.append(line)
        if self.walls[BOTTOM]:
            y, x1, x2 = self._lower_right.y, self._upper_left.x, self._lower_right.x
            line = Line(Point(x1, y), Point(x2, y))

            draw_walls.append(line)

        for line in draw_walls:
            self._window.draw_line(line, "black")

        return

    def draw_move(self, dest_cell: Cell, undo: bool=False):
        src_x = (self._upper_left.x + self._lower_right.x) // 2
        src_y = (self._upper_left.y + self._lower_right.y) // 2

        dest_x = (dest_cell._upper_left.x + dest_cell._lower_right.x) // 2
        dest_y = (dest_cell._upper_left.y + dest_cell._lower_right.y) // 2

        line = Line(Point(src_x, src_y), Point(dest_x, dest_y))       

        if not undo:
            self._window.draw_line(line, "red")
        else:
            self._window.draw_line(line, "gray")

        return

