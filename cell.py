from tkinter import Button
import random
import settings


class Cell:
    all = []

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            bg="white",
            width=12,
            height=4
        )
        btn.bind('<Button-1>', self.left_click)
        btn.bind('<Button-3>', self.right_click)
        self.cell_btn_object = btn

    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_count == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

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
        self.cell_btn_object.configure(
            text=f"{self.surrounded_cells_mines_count}",
        )

    def show_mine(self):
        # A logic to interrupt the game and display a message that player lost!
        self.cell_btn_object.config(bg="red")

    def right_click(self, event):
        print("Right click")
        print(event)

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
