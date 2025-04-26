from tkinter import Tk, BOTH, Canvas

from line    import Line

class Window():
    def __init__(self, width: int, height: int) -> None:
        # instance variables / fields
        self.__root = Tk()
        self.__canvas = Canvas(master=self.__root, width=width, height=height)
        self.__running = False

        # styles
        self.__root.title("Sample Window")
        self.__canvas.pack(fill=BOTH, expand=True)

        # close behavior
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        return
    
    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

        return

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.__canvas, fill_color=fill_color)

        return

    def wait_for_close(self) -> None:
        self.__running = True

        while self.__running:
            self.redraw()

        return
    
    def close(self) -> None:
        self.__running = False

        return
