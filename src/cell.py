from point import Point
from line  import Line
from window import Window

class Cell:
    def __init__(self, upper_left_corner: Point, lower_right_corner: Point, window: Window) -> None:
        # [top, right, bottom, left]
        self.walls = [True] * 4

        self._upper_left_corner  = upper_left_corner
        self._lower_right_corner = lower_right_corner

        self._window: Window = window

        return

    def draw(self, upper_left: Point, lower_right: Point) -> None:
        TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3
        draw_walls = []

        if self.walls[LEFT]:
            x, y1, y2 = upper_left.x, upper_left.y, lower_right.y
            line = Line(Point(x, y1), Point(x, y2))

            draw_walls.append(line)

        if self.walls[TOP]:
            y, x1, x2 = upper_left.y, upper_left.x, lower_right.x
            line = Line(Point(y, x1), Point(y, x2))

            draw_walls.append(line)
        if self.walls[RIGHT]:
            x, y1, y2 = lower_right.x, upper_left.y, lower_right.y
            line = Line(Point(x, y1), Point(x, y2))

            draw_walls.append(line)
        if self.walls[BOTTOM]:
            y, x1, x2 = lower_right.y, upper_left.x, lower_right.x
            line = Line(Point(y, x1), Point(y, x2))

            draw_walls.append(line)

        for line in draw_walls:
            line.draw(self._window.__canvas, "black")

        return

