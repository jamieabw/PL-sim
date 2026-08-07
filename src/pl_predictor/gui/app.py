from tkinter import Tk, Button, Label, Frame
from pl_predictor.gui.main_screen import MainScreen
from pl_predictor.gui.results_screen import ResultsScreen

# TODO: add max relegation points condition, flash screen for simulations, league table screen, store match results.

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x800")
        self.resizable(False, False)
        self.container = Frame(self)
        self.container.grid(row=0, column=0)
        self.frames = {}

        for Page in (MainScreen, ResultsScreen):
            frame = Page(self.container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(MainScreen)
        self.mainloop()

    def show_frame(self, screen):
        """switches which page is being displayed in the tkinter window.

        Args:
            screen (_type_): class of tkinter page to switch to
        """        
        self.frame = self.frames[screen]
        self.frame.tkraise()

    def main_screen(self):
        self.show_frame(MainScreen)
