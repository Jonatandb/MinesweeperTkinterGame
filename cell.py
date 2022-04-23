import sys
from tkinter import Button, Label
import random
import settings
import ctypes


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    mines_count_label_object = None
    candidates_count = 0

    def __init__(self, x, y, window, is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        self.window = window

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=f"Cells Left: {settings.CELL_COUNT}",
            width=12,
            height=4,
            bg="black",
            fg="white",
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl

    @staticmethod
    def create_mines_count_label(location):
        lbl = Label(
            location,
            text=f"Mines Left: {settings.MINES_COUNT}",
            width=12,
            height=4,
            bg="black",
            fg="white",
            font=("", 30)
        )
        Cell.mines_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_count == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # If there are no more cells left to open then the game is over
            if Cell.cell_count == settings.MINES_COUNT:
                self.window.after(100, self.show_you_win_message)
        # Cancel left and right click events if cell is already open
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def right_click_actions(self, event):
        if not self.is_open:
            print(f"Candidates: {Cell.candidates_count}")

            if self.is_mine_candidate:
                if Cell.candidates_count > 0:
                    Cell.candidates_count -= 1
                    self.is_mine_candidate = False
                    self.cell_btn_object.config(bg="SystemButtonFace")
            else:
                if Cell.candidates_count < settings.MINES_COUNT:
                    Cell.candidates_count += 1
                    self.is_mine_candidate = True
                    self.cell_btn_object.config(bg="yellow")

            # Replace the text of cell count label with the newer count
            if Cell.mines_count_label_object:
                Cell.mines_count_label_object.configure(
                    text=f"Mines Left: {settings.MINES_COUNT - Cell.candidates_count}",
                )
            print(f"    Candidates: {Cell.candidates_count}")

    def get_cell_by_coords(self, x, y):
        # Return a cell object based on the value of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_coords(self.x - 1, self.y - 1),
            self.get_cell_by_coords(self.x - 1, self.y),
            self.get_cell_by_coords(self.x - 1, self.y + 1),
            self.get_cell_by_coords(self.x, self.y - 1),
            self.get_cell_by_coords(self.x, self.y + 1),
            self.get_cell_by_coords(self.x + 1, self.y - 1),
            self.get_cell_by_coords(self.x + 1, self.y),
            self.get_cell_by_coords(self.x + 1, self.y + 1)
        ]
        cells = [
            cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_count(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(
                text=f"{self.surrounded_cells_mines_count}",
            )
            # Replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}"
                )
            # If this was a mine candidate then change the color back to normal
            self.cell_btn_object.config(bg="lightgray")

        # Mark the cell as opened
        self.is_open = True

    def show_mine(self):
        self.cell_btn_object.config(bg="red")
        for cell in Cell.all:
            if cell.is_mine:
                cell.cell_btn_object.config(bg="red")
                cell.cell_btn_object.configure(text="*")
            # Cancel left and right click events on game over
            cell.cell_btn_object.unbind('<Button-1>')
            cell.cell_btn_object.unbind('<Button-3>')
        self.window.after(100, self.show_game_over_message)

    def show_you_win_message(self):
        result = ctypes.windll.user32.MessageBoxW(
            0, "Congratulations! You won the game!", "Game over", 5
        )
        print(result)

    def show_game_over_message(self):
        result = ctypes.windll.user32.MessageBoxW(
            0, "You Lose! :(", "Game Over", 5
        )
        if result == 2:
            sys.exit()

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
            # IDBEHOLDA 😈
            # picked_cell.cell_btn_object.configure(
            #     text="*",
            # )

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
