import tkinter as tk
from tkinter import ttk

class Maze:
    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix
        self.window = tk.Tk()
        self.colors = {
            0: "lightblue",
            1: "red",
            2: "green",
            3: "blue"
        }
        self.setup()
        self.show()

    def setup(self):
        self.window.title('Maze Visu')
        self.window.resizable(0, 0)


    def show(self):

        for idx_row, row in enumerate(self.matrix):
            for idx_col, col in enumerate(self.matrix[idx_row]):
                tk.Label(text=f"({idx_row},{idx_col})", bg=self.colors[col], width=7, height=4).grid(column=idx_col, row=idx_row)
    

        # keep the window displaying
        self.window.mainloop()

    def update(self, updated_matrix):

        for idx_row, row in enumerate(updated_matrix):
            for idx_col, col in enumerate(updated_matrix[idx_row]):
                tk.Label(text=f"({idx_row},{idx_col})", bg=self.colors[col], width=7, height=4).grid(column=idx_col, row=idx_row)


        # update the window displaying
        self.window.update()


mz = Maze([[1,1,1,0],[1,1,0,0],[1,0,1,0]])

mz.update([[3,1,1,0],[3,1,0,0],[1,0,1,0]])