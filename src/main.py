#---[ Global Imports ]----------------------------------------------------------
from point  import Point
from line   import Line
from cell   import Cell
from window import Window

#---[ Global Imports ]----------------------------------------------------------


def main() -> None:
    window = Window(800, 800)

    cell_list = []

    cell_list.append(Cell(Point(5, 5), Point(10, 10), window))
    cell_list.append(Cell(Point(10, 10), Point(15, 15), window))
    cell_list.append(Cell(Point(15, 15), Point(20, 20), window))

    for cell in cell_list:
        cell.draw()

    window.wait_for_close()
    return


#---[ Entry ]-------------------------------------------------------------------
if __name__ == "__main__":
    main()

#---[ Entry ]-------------------------------------------------------------------

