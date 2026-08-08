from tkinter import Frame

class LeagueTableFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_columnconfigure(0, minsize=40)
        self.grid_columnconfigure(1, minsize=200)
        self.grid_columnconfigure(2, minsize=60)
        self.grid_columnconfigure(3, minsize=60)
        self.grid_columnconfigure(4, minsize=60)
        self.grid_columnconfigure(5, minsize=60)
        self.grid_columnconfigure(6, minsize=60)
        self.grid_columnconfigure(7, minsize=60)
        self.grid_columnconfigure(8, minsize=60)
        self.grid_columnconfigure(9, minsize=60)

