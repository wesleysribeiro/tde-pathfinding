from tkinter import *


def paint_rect(event):
    print("Paint rect event triggered")
    # item = event.widget.find_closest(event.x, event.y)[0]
    event.widget.itemconfigure(CURRENT, fill='blue')


def fill_scene(canvas):
    for x in range(30, 830, 30):
        for y in range(20, 620, 20):
            rect = canvas.create_rectangle(x, y, x + 20, y + 15)
            canvas.tag_bind(rect, '<Button-1>', paint_rect)


root = Tk()
root.title("Pathfinding")
root.geometry("1000x700")

w = Canvas(root, width=1000, height=700)
w.pack()
fill_scene(w)

# def main():
    # global w

root.mainloop()


# if __name__ == "__main__":
    # main()
