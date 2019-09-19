from tkinter import *
from enum import Enum


click_counter = 0
FILLED_TAG = 'filled'


# This will be useful somehow
class Click(Enum):
    ORIGIN = 0,
    DESTINY = 1,
    OBSTACLE = 2


def on_click(event):
    global click_counter, FILLED_TAG

    canvas = event.widget

    if click_counter == 0:
        current_color = '#1b870f'
    elif click_counter == 1:
        current_color = '#a8050a'
    else:
        current_color = '#659df7'

    # If the rect has not been filled yet, fill it with the current color
    if FILLED_TAG not in canvas.gettags(CURRENT):
        # TODO: fix this mess
        tags = list(canvas.gettags(CURRENT))
        tags.append(FILLED_TAG)
        tags = tuple(tags)
        canvas.itemconfig(CURRENT, fill=current_color, tags=tags)
        click_counter += 1


# TODO: Do a better function to have a bigger scene
def draw_scene(canvas, width, height):
    step_x = width//20
    step_y = height//20
    for x in range(0, width, step_x):
        for y in range(0, height, step_y):
            canvas.create_rectangle(x, y, x + step_x, y + step_y, outline='#c9f6ff', fill='#a8eaf7')


def main():
    root = Tk()

    root.title("Pathfinding project")
    window_geometry = {'width': 800, 'height': 600}
    root.geometry(str(window_geometry['width'])+"x"+str(window_geometry['height'])) # convert to string "widthxheight"

    canvas = Canvas(root, width=window_geometry['width'], height=window_geometry['height'])
    draw_scene(canvas, window_geometry['width'], window_geometry['height'])
    canvas.bind("<Button-1>", on_click)

    canvas.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
