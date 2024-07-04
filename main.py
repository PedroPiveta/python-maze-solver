from graphics import Window, Point, Line, Cell
from maze import Maze
def main():
    win = Window(800, 600)

    maze = Maze(10, 10, 5, 5, 75, 75, win)

    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()

    maze.solve()

    # cell1 = Cell(win, 50, 50, 150, 150)
    # cell1.draw()  # Draw cell1
    # 
    # cell2 = Cell(win, 200, 50, 300, 150)
    # cell2.has_left_wall = False
    # cell2.draw()  # Draw cell2 with no left wall
    #
    # cell1.draw_move(cell2)
    # 
    # cell3 = Cell(win, 350, 50, 450, 150)
    # cell3.has_top_wall = False
    # cell3.has_bottom_wall = False
    # cell3.draw()  # Draw cell3 with no top and bottom walls
    # 
    # cell4 = Cell(win, 500, 50, 600, 150)
    # cell4.has_right_wall = False
    # cell4.draw()  # Draw cell4 with no right wall
    # 
    # cell5 = Cell(win, 50, 200, 150, 300)
    # cell5.has_left_wall = False
    # cell5.has_right_wall = False
    # cell5.has_top_wall = False
    # cell5.has_bottom_wall = False
    # cell5.draw()  # Draw cell5 with no walls

    win.wait_for_close()
main()

