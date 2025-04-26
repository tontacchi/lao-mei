#---[ Global Imports ]----------------------------------------------------------
from point  import Point
from line   import Line

from window import Window

#---[ Global Imports ]----------------------------------------------------------


def main() -> None:
    window = Window(800, 800)

    line = Line(Point(50, 50), Point(500, 500))
    window.draw_line(line, "green")
    window.draw_line(line, "red")

    window.wait_for_close()
    return


#---[ Entry ]-------------------------------------------------------------------
if __name__ == "__main__":
    main()

#---[ Entry ]-------------------------------------------------------------------

