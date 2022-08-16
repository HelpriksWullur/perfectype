from tkinter import *
from tkinter import messagebox

WIDTH = 640
HEIGHT = 480

test_text = "Hello World"


def check(ev):
    if ev.keycode != 22:
        if len(txt.get("1.0", "end-1c")) == len(in_txt.get("1.0", "end-1c") + ev.char):
            if txt.get("1.0", "end-1c") == in_txt.get("1.0", "end-1c") + ev.char:
                res_text.set("Akurat")
            else:
                res_text.set("belum akurat")


def on_closing():
    if messagebox.askokcancel("Keluar", "Apakah Anda ingin keluar?"):
        root.destroy()


root = Tk()
root.title("Perfectype")
root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT,
                                   root.winfo_screenwidth() // 2 - WIDTH // 2,
                                   root.winfo_screenheight() // 2 - HEIGHT // 2))
root.resizable(False, False)

Label(text="Text").pack()
txt = Text(root, width=100, height=10)
txt.insert(END, test_text)
txt.config(state="disabled")

txt.pack()

Label(text="Input").pack()
in_txt = Text(root, width=100, height=10)
in_txt.bind('<Key>', check)

in_txt.pack()

res_text = StringVar()
res_text.set("Waiting...")

result = Label(root, textvariable=res_text)
result.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
