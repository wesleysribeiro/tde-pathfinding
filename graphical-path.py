from tkinter import *
from pathfinding.core.grid import Grid_
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.best_first import BestFirst
from pathfinding.finder.breadth_first import BreadthFirstFinder
from pathfinding.finder.dijkstra import DijkstraFinder
from enum import Enum


class Window:
    FILLED_TAG = 'filled'  # flag used to check if the rect is already filled
    click_counter = 0
    window_geometry = {'width': 800, 'height': 600}
    submit_button = None
    canvas = None  # This widget's canvas
    current_algorithm = None  # Holds the selected algorithm
    current_matrix = None  # Holds the selected matrix
    stepxm = 0
    stepym = 0
    sizem = 0
    inicio = [0, 0]
    destino = [0, 0]
    matriz = []

    class Color(Enum):
        ORIGIN = "#1b870f",
        DESTINY = "#a8050a",
        OBSTACLE = "#659df7",
        BACKGROUND = "#a8eaf7",
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

        default_algorithm = "Largura"
        self.current_algorithm = StringVar(frame)
        self.current_algorithm.set(default_algorithm)
        select_algorithm = OptionMenu(frame, self.current_algorithm, default_algorithm, "Custo Uniforme", "A*", "Guloso")
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

        xm = event.x // self.stepxm
        ym = event.y // self.stepym
        print('x: '+ str(xm) + '\ty: '+str(ym))
        if self.click_counter == 0:
            current_color = self.Color.ORIGIN.value
            self.inicio = [ym, xm]

        elif self.click_counter == 1:
            current_color = self.Color.DESTINY.value
            self.destino = [ym, xm]
        else:
            current_color = self.Color.OBSTACLE.value
            self.matriz[ym][xm] = 0

        # If the rect has not been filled yet, fill it with the current color
        if self.FILLED_TAG not in canvas.gettags(CURRENT):
            canvas.addtag_withtag(self.FILLED_TAG, CURRENT)
            canvas.itemconfig(CURRENT, fill=current_color)
            self.click_counter += 1

            # Origin and destiny were provided, enable submit button
            if self.click_counter == 2:
                self.enable_submit_button(NORMAL)

    def draw_scene(self, width, height, size):
        self.widthm = width

        step_x = width // size
        step_y = height // size

        self.stepxm = step_x
        self.stepym = step_y
        self.sizem = size
        self.matriz = [[1 for x in range(0, width // step_x)] for y in range(0, width // step_x)]

        row, column = [0, 0] # Used to store the rectangle index in the matrix
        for x in range(0, width, step_x):
            for y in range(0, height, step_y):
                rect = self.canvas.create_rectangle(x, y, x + step_x, y + step_y, outline='#c9f6ff', fill='#a8eaf7')
                self.canvas.addtag_withtag([row, column], rect)
                row += 1
            row = 0
            column += 1

    def draw_path(self, path, tested_nodes):
        for i, j in path:
            k = self.canvas.find_withtag([j, i])
            self.canvas.itemconfig(k, fill="#00C0FF")

        for i, j in tested_nodes:
            item = self.canvas.find_withtag([j, i])
            if self.canvas.itemcget(item, "fill") == self.Color.BACKGROUND.value:
                self.canvas.itemconfig(item, fill=self.Color.TESTED.value)

    def enable_submit_button(self, status):
        self.submit_button.config(state=status)

    # TODO: Call the selected algorithm function, store the generated matrix, call function draw_path to
    # to update the current scene
    def on_submit_clicked(self):
        curr_algorithm = self.current_algorithm.get()

        grid = Grid_(matrix=self.matriz)

        start = grid.node(self.inicio[1], self.inicio[0])
        end = grid.node(self.destino[1], self.destino[0])

        for row in self.matriz:
            print(row)

        if curr_algorithm == "Custo Uniforme":
            finder = DijkstraFinder()

        elif curr_algorithm == "A*":
            finder = AStarFinder()

        elif curr_algorithm == "Guloso":
            finder = BestFirst()
        else:
            finder = BreadthFirstFinder()

        path, runs = finder.find_path(start, end, grid)
        self.draw_path(path[1:-1:], [])


def main():
    root = Tk()
    Window(root, "Pathfinding")
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
