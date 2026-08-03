from tkinter import Frame, Checkbutton, Button
from pl_predictor.data.data import teams

class TeamSelectionFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.teams_to_select = [Checkbutton(self, text=team) for team in teams]
        for team in self.teams_to_select:
            team.grid(column=0)
        Button(self, text="Unselect teams", command=self.unselect_all_teams).grid(row=27, column=0)

    def unselect_all_teams(self):
        for team in self.teams_to_select:
            team.deselect()


