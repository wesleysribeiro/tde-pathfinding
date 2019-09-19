from tkinter import *
from enum import Enum


class Window:
    FILLED_TAG = 'filled' # flag used to check if the rect is already filled
    rect_matrix = [[]] # TODO: Matrix to be passed to the algorithm
    click_counter = 0
    window_geometry = {'width': 800, 'height': 600}
    submit_button = None
    canvas = None # This widget's canvas
    current_algorithm = None # Holds the selected algorithm
    current_matrix = None # Holds the selected matrix

    def __init__(self, parent, title):
        self.parent = parent
        parent.title(title)

        width = self.window_geometry['width']
        height = self.window_geometry['height']

        # Converting to a string with pattern = "heightxwidth"
        # Adds some extra room in the height for the buttons/frame
        parent.geometry(f"{width}x{height + 150}")

        self.canvas = Canvas(parent, width=width, height=height)
        self.draw_scene(width, height)
        self.canvas.bind("<Button-1>", self.on_scene_clicked)

        frame = Frame(parent, bg='#dff5f1', height=200, width=width)
        self.canvas.pack()
        default_matrix = "10x10"
        self.current_matrix = StringVar(frame)
        self.current_matrix.set(default_matrix)
        select_matrix = OptionMenu(frame, self.current_matrix, default_matrix, "20x20", "30x30")
        select_matrix.grid(row=0, column=0, padx=20)

        default_algorithm = "A*"
        self.current_algorithm = StringVar(frame)
        self.current_algorithm.set(default_algorithm)
        select_algorithm = OptionMenu(frame, self.current_algorithm, default_algorithm, "Dijkstra", "Three", "Four")
        select_algorithm.grid(row=0, column=1, padx=20)
        self.submit_button = Button(frame, text='Submit', state=DISABLED, command=self.on_submit_clicked)
        self.submit_button.grid(row=0, column=2, padx=20)
        frame.pack()

    # This will be useful somehow, someday, hopefully
    class Click(Enum):
        ORIGIN = 0,
        DESTINY = 1,
        OBSTACLE = 2

    def on_scene_clicked(self, event):
        canvas = event.widget

        if self.click_counter == 0:
            current_color = '#1b870f'
        elif self.click_counter == 1:
            current_color = '#a8050a'
        else:
            current_color = '#659df7'

        # If the rect has not been filled yet, fill it with the current color
        if self.FILLED_TAG not in canvas.gettags(CURRENT):
            # TODO: fix this mess, find a better way to do this, if there is one
            tags = list(canvas.gettags(CURRENT))
            tags.append(self.FILLED_TAG)
            tags = tuple(tags)
            canvas.itemconfig(CURRENT, fill=current_color, tags=tags)
            self.click_counter += 1

            # Origin and destiny were provided, enable submit button
            if self.click_counter == 2:
                self.enable_submit_button()

    # TODO: Make a better function to have a bigger scene (10x10 matrix, 20x20, 30x30 and on)
    def draw_scene(self, width, height):
        step_x = width//20
        step_y = height//20

        for x in range(0, width, step_x):
            for y in range(0, height, step_y):
                self.canvas.create_rectangle(x, y, x + step_x, y + step_y, outline='#c9f6ff', fill='#a8eaf7')

    # TODO: Implement this function
    # Draws the given matrix in the screen
    # def draw_path(matrix):

    def enable_submit_button(self):
        self.submit_button.config(state=NORMAL)

    # TODO: Call the selected algorithm function, store the generated matrix, call function draw_path to
    # to update the current scene
    def on_submit_clicked(self):
        print(f"Submited: {self.current_matrix.get()} with matrix {self.current_algorithm.get()}")


def main():
    root = Tk()
    window = Window(root, "Pathfinding")
    root.mainloop()


if __name__ == "__main__":
    main()
