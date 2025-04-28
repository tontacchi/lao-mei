import time
import random

from   point  import Point
from   cell   import Cell
from   window import Window

class Maze:
    def __init__(
        self,
        corner: Point,
        num_rows: int,
        num_cols: int,
        cell_width: int,
        cell_height: int,
        window: Window,
        seed: int | None=None
    ) -> None:
        self._corner = corner
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._window = window

        if not seed:
            random.seed(seed)

        self._cells: list[list[Cell]] = []
        self._create_cells()
        self._break_entrance_and_exit()

        self._break_walls_r(0, 0)
        self._reset_cells_visited()

        return

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _create_cells(self) -> None:
        # fills cell matrix
        for row in range(self._num_rows):
            self._cells.append([])

            start = Point(self._corner.x, self._corner.y)
            start.y = self._corner.y + self._cell_height * row

            for col in range(self._num_cols):
                left = Point(start.x, start.y)
                right = Point(start.x + self._cell_width, start.y + self._cell_height)

                self._cells[row].append(Cell(left, right, self._window))

                start.x += self._cell_width

        # renders cells to canvas
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                self._draw_cell(row, col)

        return

    def _draw_cell(self, row: int, col: int) -> None:
        cell = self._cells[row][col]
        cell.draw()

        self._animate()

        return

    def _animate(self) -> None:
        SLEEP_MILLISECONDS = 2.5

        self._window.redraw()
        time.sleep(SLEEP_MILLISECONDS / 100)

        return

    def _break_entrance_and_exit(self) -> None:
        first, last = self._cells[0][0], self._cells[self._num_rows-1][self._num_cols-1]
        TOP, BOTTOM = 0, 2

        first.walls[TOP] = False
        self._draw_cell(0, 0)

        last.walls[BOTTOM] = False
        self._draw_cell(self._num_rows-1, self._num_cols-1)

        return

    def _break_walls_r(self, row: int, col: int) -> None:
        start = self._cells[row][col]
        start.visited= True

        moves = []
        
        if row > 0 and not self._cells[row-1][col].visited:
            moves.append((row-1, col))
        if col > 0 and not self._cells[row][col-1].visited:
            moves.append((row, col-1))
        if row < self._num_rows-1 and not self._cells[row+1][col].visited:
            moves.append((row+1, col))
        if col < self._num_cols-1 and not self._cells[row][col+1].visited:
            moves.append((row, col+1))

        random.shuffle(moves)
        while moves:
            i, j = moves.pop(0)

            next = self._cells[i][j]

            if i < row and not next.visited:
                start.walls[0] = False
            elif j < col and not next.visited:
                start.walls[3] = False
            elif i > row and not next.visited:
                start.walls[2] = False
            elif j > col and not next.visited:
                start.walls[1] = False

            self._break_walls_r(i, j)
            self._draw_cell(row, col)


        return

    def _reset_cells_visited(self) -> None:
        for row in self._cells:
            for cell in row:
                cell.visited = False
                print(cell.visited)

        return

    def _solve_r(self, row: int, col: int) -> bool:
        self._animate()
        start = self._cells[row][col]
        start.visited = True

        if (row, col) == (self._num_rows-1, self._num_cols-1):
            return True

        not_blocked = start.walls[0] == False and row > 0 and not self._cells[row-1][col].visited
        if not_blocked:
            start.draw_move(self._cells[row-1][col])

            res = self._solve_r(row-1, col)
            if res:
                return True
            start.draw_move(self._cells[row-1][col], undo=True)

        not_blocked = start.walls[3] == False and col > 0 and not self._cells[row][col-1].visited
        if not_blocked:
            start.draw_move(self._cells[row][col-1])

            res = self._solve_r(row, col-1)
            if res:
                return True
            start.draw_move(self._cells[row][col-1], undo=True)

        not_blocked = start.walls[2] == False and row < self._num_rows-1 and not self._cells[row+1][col].visited
        if not_blocked:
            start.draw_move(self._cells[row+1][col])

            res = self._solve_r(row+1, col)
            if res:
                return True
            start.draw_move(self._cells[row+1][col], undo=True)

        not_blocked = start.walls[1] == False and col < self._num_cols-1 and not self._cells[row][col+1].visited
        if not_blocked:
            start.draw_move(self._cells[row][col+1])

            res = self._solve_r(row, col+1)
            if res:
                return True
            start.draw_move(self._cells[row][col+1], undo=True)

        return False

