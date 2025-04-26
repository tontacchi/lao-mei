from tkinter import Canvas
from point   import Point

class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.__start = start
        self.__end = end

        return

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        line_width = 2

        canvas.create_line(
            self.__start.x,
            self.__start.y,
            self.__end.x,
            self.__end.y,
            fill=fill_color,
            width=line_width
        )

        return

