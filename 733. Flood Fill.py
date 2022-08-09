from time import sleep
from threading import Thread

MA = [[1,1,1],[1,1,0],[1,0,1]]

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        global MA
        if image[sr][sc] == color:
            return image

        from collections import deque
        nodedeque = deque([[sr,sc]])
        startingColor = image[sr][sc]
        image[sr][sc] = color

        while nodedeque:

            cur = nodedeque.popleft()
            if cur[0] > 0:
                if image[cur[0] - 1][cur[1]] == startingColor:
                    nodedeque.append([cur[0] - 1, cur[1]])
                    image[cur[0] - 1][cur[1]] = color

            if cur[0] < len(image)-1:
                if image[cur[0] + 1][cur[1]]== startingColor:
                    nodedeque.append([cur[0] + 1, cur[1]])
                    image[cur[0] + 1][cur[1]] = color

            if cur[1] > 0:
                if image[cur[0]][cur[1] - 1]== startingColor:
                    nodedeque.append([cur[0], cur[1] - 1])
                    image[cur[0]][cur[1] - 1] = color

            if cur[1] < len(image[0])-1:
                if image[cur[0]][cur[1] + 1]== startingColor:
                    nodedeque.append([cur[0], cur[1] + 1])
                    image[cur[0]][cur[1] + 1] = color

            MA = image
            sleep(1)

        return image



def task():
    sl = Solution()
    sl.floodFill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)

t1 = Thread(target=task)
t1.start()





import tkinter as tk
from tkinter import ttk

class Maze:
    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix
        self.root = tk.Tk()
        self.colors = {
            0: "lightblue",
            1: "red",
            2: "green",
            3: "blue"
        }
        self.setup()
        self.show()

    def setup(self):
        self.root.title('Maze Visu')
        self.root.resizable(0, 0)


    def show(self):

        for idx_row, row in enumerate(self.matrix):
            for idx_col, col in enumerate(self.matrix[idx_row]):
                tk.Label(text=f"({idx_row},{idx_col})", bg=self.colors[col], width=7, height=4).grid(column=idx_col, row=idx_row)
    

        # keep the window displaying
        self.root.after(100, self.update)
        self.root.mainloop()

    def update(self):
        updated_matrix = MA

        for idx_row, row in enumerate(updated_matrix):
            for idx_col, col in enumerate(updated_matrix[idx_row]):
                tk.Label(text=f"({idx_row},{idx_col})", bg=self.colors[col], width=7, height=4).grid(column=idx_col, row=idx_row)


        # update the window displaying
        self.root.after(100, self.update)
        self.root.update()


mz = Maze([[1,1,1,0],[1,1,0,0],[1,0,1,0]])