from tkinter import Frame, Button
from pl_predictor.gui.results_screen import ResultsScreen

class MainScreen(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        Button(self, text="Switch frame", command=lambda : controller.show_frame(ResultsScreen)).pack() # test