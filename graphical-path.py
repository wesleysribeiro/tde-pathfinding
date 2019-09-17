from tkinter import *
from tkinter import ttk


def callback(self):
    self.configure(bg="red")
    # button


def draw_scene(root, buttons):
    for row in range(0, 10):
        for col in range(0, 10):
            button = Button(root, text="Button" + str(row*10 + col))
            button.config(command=lambda: callback(button))
            button.grid(row=row, column=col)


def main():
    root = Tk()
    root.title("Pathfinding project")
    root.geometry("800x600")

    draw_scene(root)

    # button = Button(root, text="Testing")
    # button.pack()
    # button.bind("<Button-3>", callback)

    root.mainloop()

if __name__ == "__main__":
    main()
