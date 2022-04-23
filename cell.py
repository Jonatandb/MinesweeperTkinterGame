from tkinter import Button


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
            text=f"{self.x}, {self.y}",
            width=12,
            height=4
        )
        btn.bind('<Button-1>', self.left_click)
        btn.bind('<Button-3>', self.right_click)
        self.cell_btn_object = btn

    def left_click(self, event):
        print("Left click")
        print(event)

    def right_click(self, event):
        print("Right click")
        print(event)

    @staticmethod
    def randomize_mines():
        pass

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
