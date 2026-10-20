from tkinter import *

root = Tk()
root.title("Курсы обмена валют")

WIDTH, HEIGHT = 350, 400
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = (screen_w - WIDTH) // 2
y = (screen_h - HEIGHT) // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
root.resizable(False, False)

root.mainloop()
