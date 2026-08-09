from tkinter import Frame, Label, Button
from pl_predictor.gui.league_table import LeagueTableFrame

class ResultsScreen(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller


    def display_teams(self, data):
        table, self.match_results = data
        self.league_table = LeagueTableFrame(self)
        self.league_table.grid(row=0, column=0, columnspan=5)
        Label(self.league_table, text=f"POS").grid(row=0, column=0)
        Label(self.league_table, text="TEAM").grid(row=0, column=1)
        Label(self.league_table, text="GAMES").grid(row=0, column=2)
        Label(self.league_table, text="PTS").grid(row=0, column=3)
        Label(self.league_table, text="W").grid(row=0, column=4)
        Label(self.league_table, text="D").grid(row=0, column=5)
        Label(self.league_table, text="L").grid(row=0, column=6)
        Label(self.league_table, text="GF").grid(row=0, column=7)
        Label(self.league_table, text="GA").grid(row=0, column=8)
        Label(self.league_table, text="GD").grid(row=0, column=9)
        for i, team in enumerate(table):
            Label(self.league_table, text=f"{i+1})").grid(row=i+1, column=0)
            Label(self.league_table, text=team.get_name()).grid(row=i+1, column=1)
            Label(self.league_table, text=(len(table) - 1) * 2).grid(row=i+1, column=2)
            Label(self.league_table, text=team.get_points()).grid(row=i+1, column=3)
            Label(self.league_table, text=team.wins).grid(row=i+1, column=4)
            Label(self.league_table, text=team.draws).grid(row=i+1, column=5)
            Label(self.league_table, text=team.losses).grid(row=i+1, column=6)
            Label(self.league_table, text=team.goals_scored).grid(row=i+1, column=7)
            Label(self.league_table, text=team.goals_conceded).grid(row=i+1, column=8)
            Label(self.league_table, text=team.goals_scored - team.goals_conceded).grid(row=i+1, column=9)
            Button(self.league_table, text="View Results", command=lambda team=team: self.display_match_results(team.get_name())).grid(row=i+1, column=10)
        Button(self, text="Back", command=lambda: self.clear_screen()).grid(row=1, column=1)

    def display_match_results(self, team):
        matches_wanted = {}
        for match in self.match_results.keys():
            if team in match:
                matches_wanted[match] = self.match_results[match]
        self.controller.show_match_results(matches_wanted)


    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.controller.main_screen()
        