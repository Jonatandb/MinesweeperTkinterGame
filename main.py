from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()

# Override the settings of the window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.configure(bg='black')
root.title("Minesweeper Game by Jonatandb@gmail.com")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_percentage(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_percentage(25),
    height=utils.height_percentage(75)
)
left_frame.place(x=0, y=utils.height_percentage(25))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_percentage(75),
    height=utils.height_percentage(75)
)
center_frame.place(x=utils.width_percentage(25), y=utils.height_percentage(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        cell = Cell(x, y, root)
        cell.create_btn_object(center_frame)
        cell.cell_btn_object.grid(column=x, row=y)

# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)
Cell.randomize_mines()

# Run the window
root.mainloop()
