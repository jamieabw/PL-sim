from tkinter import Frame, Checkbutton, Button
from pl_predictor.data.data import teams

class TeamSelectionFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.selected = {}
        self.teams_to_select = [Checkbutton(self, text=team, command= lambda team=team : self.selected.__setitem__(team, True)) for team in teams]
        for team in self.teams_to_select:
            team.grid(column=0)
        Button(self, text="Unselect teams", command=self.unselect_all_teams).grid(row=27, column=0)

    def unselect_all_teams(self):
        for team in self.teams_to_select:
            self.selected[team.cget("text")] = False
            team.deselect()

    def get_selected_teams(self) -> list[str]:
        """gets the teams which are currently selected in the main screen UI

        Returns:
            list[str]: a list of the team names which were selected.
        """        
        teams = []
        for team, select in self.selected.items():
            if select:
                teams.append(team)
        return teams


