import random
from tkinter import *
from tkinter import messagebox
from threading import Thread


class App:
    WIDTH = 640
    HEIGHT = 480

    with open("src/raw.txt", 'r') as text:
        raw_texts = text.read().split()

    test_text = ""
    rand_count = 0

    def __init__(self):
        self.rnd()
        self.root = Tk()
        self.root.title("Perfectype")
        self.root.geometry("{}x{}+{}+{}".format(App.WIDTH, App.HEIGHT,
                                                self.root.winfo_screenwidth() // 2 - App.WIDTH // 2,
                                                self.root.winfo_screenheight() // 2 - App.HEIGHT // 2))
        self.root.resizable(False, False)

        Label(text="Text").pack()
        self.txt = Text(self.root, width=100, height=6, padx=5, pady=5)
        self.txt.insert(END, App.test_text)
        self.txt.config(state="disabled", font="arial 19")

        self.txt.pack()

        Label(text="Input").pack()
        self.in_txt = Text(self.root, width=100, height=6, padx=5, pady=5)
        self.in_txt.config(font="arial 19")
        self.in_txt.focus()
        self.in_txt.pack()

        self.res_text = StringVar()

        result = Label(self.root, textvariable=self.res_text)
        result.pack()

        Button(self.root, text="random", command=self.rnd).pack()

        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        self.t = Thread(target=self.check)
        self.t.daemon = True
        self.t.start()

    def run(self):
        self.root.mainloop()

    def callback(self):
        if messagebox.askokcancel("Keluar", "Apakah Anda ingin keluar?"):
            self.root.quit()

    def rnd(self):
        App.rand_count += 1
        random.shuffle(App.raw_texts)
        App.test_text = " ".join(App.raw_texts[0:30])
        if App.rand_count > 1:
            self.txt.config(state="normal")
            self.txt.delete("1.0", END)
            self.txt.insert(END, App.test_text)
            self.txt.config(state="disabled")
            self.in_txt.delete("1.0", END)
            self.res_text.set("Menunggu...")

    def check(self):
        while True:
            if len(self.txt.get("1.0", "end-1c")) == len(self.in_txt.get("1.0", "end-1c")):
                if self.txt.get("1.0", "end-1c") == self.in_txt.get("1.0", "end-1c"):
                    self.res_text.set("Akurat")
                else:
                    self.res_text.set("belum akurat")
            else:
                self.res_text.set("Menunggu...")


app = App()
app.run()
