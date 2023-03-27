from tkinter import *

root = Tk()
root.title("Рисуем")
root.geometry("1000x1000")

gomove=False
def move(event):
    if gomove:
        x = event.x
        y = event.y
        x0, y0, x1, y1 = canvas.coords(rect1)
        canvas.coords(rect1, x-50, y-50, x, y)

def start(event):
    global gomove
    gomove=True

def stop(event):
    global gomove
    gomove=False


canvas = Canvas(bg="white", width=950, height=950)
canvas.pack(anchor=CENTER, expand=2)

# Начало программы рисования

rect1 = canvas.create_rectangle(50, 50, 100, 100)


root.bind('<Motion>', move)
root.bind('<Button-1>', start)
root.bind('<Button-3>', stop)
root.mainloop()