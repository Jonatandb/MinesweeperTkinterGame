from tkinter import Button


class Cell:
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

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
