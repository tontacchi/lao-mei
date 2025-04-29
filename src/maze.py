import time
import random

from   point  import Point
from   cell   import Cell
from   window import Window

from   frame  import Frame

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
        # return self._solve_r(0, 0)
        print("solving")
        self._solve_dfs_iterative()
        print("solved!")

        return True

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

    def _draw_cell(self, row: int, col: int, animate=False) -> None:
        cell = self._cells[row][col]
        cell.draw()

        if animate:
            self._animate()

        return

    def _animate(self, animate: bool=True) -> None:
        SLEEP_MILLISECONDS = 2.5

        if not animate:
            SLEEP_MILLISECONDS = 0

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

    def _solve_dfs_iterative(self) -> None:
        '''
        Solves the maze using a stack Stack.

        Precondition:
        - the maze is solveable.

        Postcondition:
        - all cells are set to visited
        - the maze is "solved"

        Side-Effects:
        - renders lines between visited cells of the maze
            - the final path is colored red
        '''
        neighbors = self._get_neighbors(0, 0)
        random.shuffle(neighbors)
        next_neighbor_index = 0

        call_stack = [[0, 0, neighbors, next_neighbor_index]]

        while call_stack:
            self._animate()
            row, col, neighbors, next_neighbor_index = call_stack[-1]

            if next_neighbor_index >= len(neighbors):
                print(f"visited all neighbors of ({row}, {col})")
                call_stack.pop()

                if call_stack:
                    prev_row, prev_col, _, _ = call_stack[-1]
                    cell, prev_cell = self._cells[row][col], self._cells[prev_row][prev_col]

                    cell.draw_move(prev_cell, undo=True)
                    
                continue

            next_row, next_col = neighbors[next_neighbor_index]

            # neighbor index incremented for next time
            call_stack[-1][3] += 1

            neighbor = self._cells[next_row][next_col]
            if neighbor.visited == False:
                neighbor.visited = True

                cell = self._cells[row][col]
                cell.draw_move(neighbor)

                if (next_row, next_col) == (self._num_rows-1, self._num_cols-1):
                    break

                neighbor_of_neighbors = self._get_neighbors(next_row, next_col)
                random.shuffle(neighbor_of_neighbors)
                call_stack.append([next_row, next_col, neighbor_of_neighbors, 0])
            else:
                print(f"revisited ({next_row}, {next_col}). skipping rest")

        return

    def _get_neighbors(self, row: int, col: int) -> list:
        cell = self._cells[row][col]
        neighbors = []

        if 0 < row and cell.walls[0] == False and self._cells[row-1][col].visited == False:
            neighbors.append((row-1, col))
        if 0 < col and cell.walls[3] == False and self._cells[row][col-1].visited == False:
            neighbors.append((row, col-1))
        if row < self._num_rows-1 and cell.walls[2] == False and self._cells[row+1][col].visited == False:
            neighbors.append((row+1, col))
        if col < self._num_cols-1 and cell.walls[1] == False and self._cells[row][col+1].visited == False:
            neighbors.append((row, col+1))
        
        return neighbors

