import random
from tkinter import *
from tkinter import messagebox

WIDTH = 640
HEIGHT = 480

raw_texts = ['aku', 'dia', 'kamu', 'pergi', 'harus', 'uang', 'rumah', 'bernyanyi', 'kembali', 'hutang', 'bayar', 'dokter', 'malam', 'hati', 'sakit', 'tinggal', 'siapa']
test_text = ""
rand_count = 0


def rnd():
    global test_text, rand_count, stat
    rand_count += 1
    random.shuffle(raw_texts)
    test_text = " ".join(raw_texts)
    if rand_count > 1:
        txt.config(state="normal")
        txt.delete("1.0", END)
        txt.insert(END, test_text)
        txt.config(state="disabled")
        in_txt.delete("1.0", END)


def check(ev):
    if ev.keycode != 22:
        if len(txt.get("1.0", "end-1c")) == len(in_txt.get("1.0", "end-1c") + ev.char):
            if txt.get("1.0", "end-1c") == in_txt.get("1.0", "end-1c") + ev.char:
                res_text.set("Akurat")
            else:
                res_text.set("belum akurat")
        else:
            if ev.keycode != 50 and ev.keycode != 62:
                if ev.char == txt.get("1.0", "end-1c")[len(in_txt.get("1.0", "end-1c"))]:
                    print("benar")
                else:
                    print("salah")


def on_closing():
    if messagebox.askokcancel("Keluar", "Apakah Anda ingin keluar?"):
        root.destroy()


rnd()

root = Tk()
root.title("Perfectype")
root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT,
                                   root.winfo_screenwidth() // 2 - WIDTH // 2,
                                   root.winfo_screenheight() // 2 - HEIGHT // 2))
root.resizable(False, False)

Label(text="Text").pack()
txt = Text(root, width=100, height=10, padx=5, pady=5)
txt.insert(END, test_text)
txt.config(state="disabled")

txt.pack()

Label(text="Input").pack()
in_txt = Text(root, width=100, height=10, padx=5, pady=5)
in_txt.bind('<Key>', check)
in_txt.focus()

in_txt.pack()

res_text = StringVar()
res_text.set("Waiting...")

result = Label(root, textvariable=res_text)
result.pack()

Button(root, text="random", command=rnd).pack()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
