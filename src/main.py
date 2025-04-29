#---[ Global Imports ]----------------------------------------------------------
from point  import Point
from line   import Line
from cell   import Cell
from maze   import Maze
from window import Window

#---[ Global Imports ]----------------------------------------------------------


def main() -> None:
    window = Window(800, 800)

    corner = Point(50, 50)
    maze_dimensions = (30, 30)
    cell_dimensions = (10, 10)

    maze = Maze(
        corner,
        *maze_dimensions,
        *cell_dimensions,
        window,
        seed=None
    )
    maze.solve()

    window.wait_for_close()
    return

#---[ Entry ]-------------------------------------------------------------------
if __name__ == "__main__":
    main()

#---[ Entry ]-------------------------------------------------------------------

