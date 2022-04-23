from tkinter import *
import settings

root = Tk()

# Override the settings of the window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.configure(bg='black')
root.title("Minesweeper Game")
root.resizable(False, False)

# Run the window
root.mainloop()
