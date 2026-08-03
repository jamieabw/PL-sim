from tkinter import Frame, Button, Checkbutton
from pl_predictor.gui.results_screen import ResultsScreen
from pl_predictor.data.data import get_team_names
from pl_predictor.gui.team_selection import TeamSelectionFrame
from pl_predictor.gui.condition_selection import ConditionSelectionFrame

class MainScreen(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        Button(self, text="Switch frame", command=lambda : controller.show_frame(ResultsScreen)).grid(row=1, column=1) # test
        TeamSelectionFrame(self).grid(row=0, column=0, rowspan=3)
        ConditionSelectionFrame(self).grid(row=0, column=1)
        Button(text="Simulate").grid(row=3, column=3)




