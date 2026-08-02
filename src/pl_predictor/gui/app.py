from tkinter import Tk, Button, Label

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x800")
        self.resizable(False, False)
        self.mainloop()



gui = App()