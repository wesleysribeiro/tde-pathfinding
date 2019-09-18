from tkinter import *
from enum import Enum


click_counter = 0


# This will be useful somehow
class Click(Enum):
    ORIGIN = 0,
    DESTINY = 1,
    OBSTACLE = 2


def on_click(event):
    global click_counter

    canvas = event.widget

    if click_counter == 0:
        current_color = '#1b870f'
    elif click_counter == 1:
        current_color = '#a8050a'
    else:
        current_color = '#659df7'

    if 'filled' not in canvas.gettags(CURRENT):
        # TODO: fix this mess
        tags = list(canvas.gettags(CURRENT))
        tags.append("filled")
        tags = tuple(tags)
        canvas.itemconfig(CURRENT, fill=current_color, tags=tags)
        click_counter += 1


def main():
    root = Tk()

    root.title("Pathfinding project")
    root.geometry("800x600")

    canvas = Canvas(root, width=800, height=600)

    # TODO: Make this more generic
    for x in range(0, 800, 40):
        for y in range(0, 600, 20):
            canvas.create_rectangle(x, y, x + 40, y + 20, outline='#c9f6ff', fill='#a8eaf7')

    canvas.bind("<Button-1>", on_click)

    canvas.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
