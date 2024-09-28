import tkinter as tk
import random


def get_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


def on_hover(event):
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    button_width = random.randint(50, 200)
    button_height = random.randint(20, 100)

    x = random.randint(0, window_width - button_width)
    y = random.randint(0, window_height - button_height)

    button.config(bg=get_random_color())

    button.place(x=x, y=y, width=button_width, height=button_height)


def on_leave(event):
    button.config(text="Кнопка")


root = tk.Tk()
root.title("Кнопка меняющая форму и цвет")

root.geometry("500x400")

button = tk.Button(root, text="Наведи мышь!", width=20, height=2)
button.place(x=200, y=150)

button.bind("<Enter>", on_hover)
button.bind("<Leave>", on_leave)

root.mainloop()
