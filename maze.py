from graphics import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self.cells = self._createcells()
     
    def _createcells(self):
        cells = []
        for col in range(self.num_cols):
            colcells = []
            for row in range(self.num_rows):
                cell = self._draw_cell(row, col)
                colcells.append(cell)
            cells.append(colcells)
        return cells

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell = Cell(x1, y1, x2, y2, self._win)
        cell.draw()
        self._animate()
        return cell

    def _break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.cells[0][0].draw()

        self.cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        self.cells[self.num_rows - 1][self.num_cols - 1].draw()
    

    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self.cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self.cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self.cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self.cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self.cells[i][j].draw()
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for row in self.cells:
            for cell in row:
                cell.visited = False
                print(cell.visited)

    def _solve_r(self, i, j):
        self._animate()

        # vist the current cell
        self.cells[i][j].visited = True

        # if we are at the end cell, we are done!
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        # move left if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self.cells[i][j].has_left_wall
            and not self.cells[i - 1][j].visited
        ):
            self.cells[i][j].draw_move(self.cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i - 1][j], True)

        # move right if there is no wall and it hasn't been visited
        if (
            i < self.num_cols - 1
            and not self.cells[i][j].has_right_wall
            and not self.cells[i + 1][j].visited
        ):
            self.cells[i][j].draw_move(self.cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self.cells[i][j].has_top_wall
            and not self.cells[i][j - 1].visited
        ):
            self.cells[i][j].draw_move(self.cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (
            j < self.num_rows - 1
            and not self.cells[i][j].has_bottom_wall
            and not self.cells[i][j + 1].visited
        ):
            self.cells[i][j].draw_move(self.cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False    
    def solve(self):
        return self._solve_r(0, 0)

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
