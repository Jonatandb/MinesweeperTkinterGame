from tkinter import *
import settings
import utils

root = Tk()

# Override the settings of the window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.configure(bg='black')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red',  # Change later to black
    width=settings.WIDTH,
    height=utils.height_percentage(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='blue',  # Change later to black
    width=utils.width_percentage(25),
    height=utils.height_percentage(75)
)
left_frame.place(x=0, y=utils.height_percentage(25))


# Run the window
root.mainloop()
