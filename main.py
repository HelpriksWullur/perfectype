from tkinter import *

WIDTH = 640
HEIGHT = 480

root = Tk()
root.title("Perfectype")
root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT,
                                   root.winfo_screenwidth() // 2 - WIDTH // 2,
                                   root.winfo_screenheight() // 2 - HEIGHT // 2))
root.resizable(False, False)

Label(text="Text").pack()
txt = Text(root, width=100, height=10)

txt.pack()

Label(text="Input").pack()
in_txt = Text(root, width=100, height=10)

in_txt.pack()

root.mainloop()
