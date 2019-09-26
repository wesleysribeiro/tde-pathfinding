from tkinter import *
from enum import Enum


class Window:
    FILLED_TAG = 'filled'  # flag used to check if the rect is already filled
    click_counter = 0
    window_geometry = {'width': 800, 'height': 600}
    submit_button = None
    canvas = None  # This widget's canvas
    current_algorithm = None  # Holds the selected algorithm
    current_matrix = None  # Holds the selected matrix

    class Color(Enum):
        ORIGIN = "#1b870f",
        DESTINY = "#a8050a",
        OBSTACLE = "#659df7",
        TESTED = "grey"

    def __init__(self, parent, title):
        self.parent = parent
        parent.title(title)

        width = self.window_geometry['width']
        height = self.window_geometry['height']

        # Converting to a string with pattern = "heightxwidth"
        # Adds some extra room in the height for the buttons/frame
        frame_height = 50
        parent.geometry(f"{width}x{height + frame_height}")

        self.canvas = Canvas(parent, width=width, height=height)
        self.draw_scene(width, height, 10)
        self.canvas.bind("<Button-1>", self.on_scene_clicked)

        frame = Frame(parent, height=frame_height, width=width)
        self.canvas.pack()
        default_matrix = "10x10"
        self.current_matrix = StringVar(frame)
        self.current_matrix.set(default_matrix)
        select_matrix = OptionMenu(frame, self.current_matrix, default_matrix,
                                   "20x20", "30x30", "40x40", "50x50", "60x60", command=self.on_matrix_changed)
        select_matrix.grid(row=0, column=0, padx=20)

        default_algorithm = "A*"
        self.current_algorithm = StringVar(frame)
        self.current_algorithm.set(default_algorithm)
        select_algorithm = OptionMenu(frame, self.current_algorithm, default_algorithm, "Dijkstra", "Algo3", "Algo4")
        select_algorithm.grid(row=0, column=1, padx=20)

        self.submit_button = Button(frame, text='Submit', state=DISABLED, command=self.on_submit_clicked)
        self.submit_button.grid(row=0, column=2, padx=20)

        frame.pack()

    def on_matrix_changed(self, event):
        matrix_size = self.current_matrix.get().split('x')[0]
        self.canvas.delete(ALL)
        self.draw_scene(self.window_geometry['width'], self.window_geometry['height'], int(matrix_size))
        self.click_counter = 0
        self.enable_submit_button(DISABLED)

    def on_scene_clicked(self, event):
        canvas = event.widget

        if self.click_counter == 0:
            current_color = self.Color.ORIGIN.value
        elif self.click_counter == 1:
            current_color = self.Color.DESTINY.value
        else:
            current_color = self.Color.OBSTACLE.value

        # If the rect has not been filled yet, fill it with the current color
        if self.FILLED_TAG not in canvas.gettags(CURRENT):
            canvas.addtag_withtag(self.FILLED_TAG, CURRENT)
            canvas.itemconfig(CURRENT, fill=current_color)
            self.click_counter += 1

            # Origin and destiny were provided, enable submit button
            if self.click_counter == 2:
                self.enable_submit_button(NORMAL)

    def draw_scene(self, width, height, size):
        step_x = width // size
        step_y = height // size

        row, column = [0, 0] # Used to store the rectangle index in the matrix
        for x in range(0, width, step_x):
            for y in range(0, height, step_y):
                rect = self.canvas.create_rectangle(x, y, x + step_x, y + step_y, outline='#c9f6ff', fill='#a8eaf7')
                self.canvas.addtag_withtag([row, column], rect)
                row += 1
            row = 0
            column += 1

    # TODO: Implement this function
    # Draws the given matrix in the screen
    # def draw_path(matrix):

    def enable_submit_button(self, status):
        self.submit_button.config(state=status)

    # TODO: Call the selected algorithm function, store the generated matrix, call function draw_path to
    # to update the current scene
    def on_submit_clicked(self):
        print(f"Submited: {self.current_matrix.get()} with matrix {self.current_algorithm.get()}")


def main():
    root = Tk()
    Window(root, "Pathfinding")
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()