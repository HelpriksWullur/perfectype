import tkinter
from tkinter import *


WIDTH = 640
HEIGHT = 480

test_text = "Hello World"


def check(ev):
    if ev.keycode != 22:
        if len(txt.get("1.0", "end-1c")) == len(in_txt.get("1.0", "end-1c") + ev.char):
            if txt.get("1.0", "end-1c") == in_txt.get("1.0", "end-1c") + ev.char:
                print("100% akurat")
            else:
                print("belum akurat")


root = Tk()
root.title("Perfectype")
root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT,
                                   root.winfo_screenwidth() // 2 - WIDTH // 2,
                                   root.winfo_screenheight() // 2 - HEIGHT // 2))
root.resizable(False, False)

Label(text="Text").pack()
txt = Text(root, width=100, height=10)
txt.insert(tkinter.END, test_text)

txt.pack()

Label(text="Input").pack()
in_txt = Text(root, width=100, height=10)
in_txt.bind('<Key>', check)

in_txt.pack()

root.mainloop()
