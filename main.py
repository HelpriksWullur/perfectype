from tkinter import *

WIDTH = 600
HEIGHT = 400

root = Tk()
root.title("Perfectype")
root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT,
                                   root.winfo_screenwidth() // 2 - WIDTH // 2,
                                   root.winfo_screenheight() // 2 - HEIGHT // 2))
root.resizable(False, False)

root.mainloop()
