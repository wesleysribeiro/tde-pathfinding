from tkinter import *

click_counter = 0


def on_click(event):
    global click_counter

    canvas = event.widget

    if click_counter == 0:
        current_color = 'red'
    elif click_counter == 1:
        current_color = 'green'
    else:
        current_color = 'black'

    if 'filled' not in canvas.gettags(CURRENT):
        # This just looks awful, let's get rid of it
        tags = list(canvas.gettags(CURRENT))
        tags.append("filled")
        tags = tuple(tags)
        canvas.itemconfig(CURRENT, fill=current_color, tags=tags)
        click_counter += 1

def main():
    root = Tk()

    root.title("Pathfinding project")
    root.geometry("800x600")
    print(root.winfo_geometry())

    canvas = Canvas(root, width=800, height=600)

    for x in range(0, 800, 20):
        for y in range(0, 600, 15):
            canvas.create_rectangle(x, y, x + 20, y + 15, fill='white')

    canvas.bind("<Button-1>", on_click)

    canvas.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
