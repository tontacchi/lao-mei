#---[ Global Imports ]----------------------------------------------------------
from point  import Point
from line   import Line
from cell   import Cell
from window import Window

#---[ Global Imports ]----------------------------------------------------------


def main() -> None:
    window = Window(800, 800)

    cell_list = []

    temp1 = Cell(Point(100, 100), Point(150, 150), window)
    temp1.walls = [False, False, False, False]
    cell_list.append(temp1)

    temp2 = Cell(Point(100, 50), Point(150, 100), window)
    temp2.walls = [True, True, False, True]
    cell_list.append(temp2)

    temp3 = Cell(Point(50, 100), Point(100, 150), window)
    temp3.walls = [True, False, True, True]
    cell_list.append(temp3)

    temp4 = Cell(Point(100, 150), Point(150, 200), window)
    temp4.walls = [False, True, True, True]
    cell_list.append(temp4)

    temp5 = Cell(Point(150, 100), Point(200, 150), window)
    temp5.walls = [True, True, True, False]
    cell_list.append(temp5)

    for cell in cell_list:
        cell.draw()

    temp1.draw_move(temp2)
    temp1.draw_move(temp3)
    temp1.draw_move(temp4)
    temp1.draw_move(temp5)

    window.wait_for_close()
    return

'''
    side = 25
    origin = Point(50, 50)
    
    NUM_ROWS, NUM_COLS = 3, 5
    for row in range(NUM_ROWS):
        start = Point(origin.x, origin.y)
        start.y = origin.y + side * row

        for col in range(NUM_COLS):
            left  = Point(start.x, start.y)
            right = Point(start.x + side, start.y + side)
            cell_list.append(Cell(left, right, window))
            start.x += side
'''

#---[ Entry ]-------------------------------------------------------------------
if __name__ == "__main__":
    main()

#---[ Entry ]-------------------------------------------------------------------

