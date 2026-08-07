from tkinter import Frame, Label, Button
from pl_predictor.gui.league_table import LeagueTableFrame

class ResultsScreen(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller


    def display_teams(self, table):
        self.league_table = LeagueTableFrame(self)
        self.league_table.grid(row=0, column=0, columnspan=5)
        Label(self.league_table, text=f"POS").grid(row=0, column=0)
        Label(self.league_table, text="TEAM").grid(row=0, column=1)
        Label(self.league_table, text="GAMES").grid(row=0, column=2)
        Label(self.league_table, text="PTS").grid(row=0, column=3)
        Label(self.league_table, text="GF").grid(row=0, column=4)
        Label(self.league_table, text="GA").grid(row=0, column=5)
        Label(self.league_table, text="GD").grid(row=0, column=6)
        for i, team in enumerate(table):
            Label(self.league_table, text=f"{i+1})").grid(row=i+1, column=0)
            Label(self.league_table, text=team.get_name()).grid(row=i+1, column=1)
            Label(self.league_table, text=(len(table) - 1) * 2).grid(row=i+1, column=2)
            Label(self.league_table, text=team.points).grid(row=i+1, column=3)
            Label(self.league_table, text=team.goals_scored).grid(row=i+1, column=4)
            Label(self.league_table, text=team.goals_conceded).grid(row=i+1, column=5)
            Label(self.league_table, text=team.goals_scored - team.goals_conceded).grid(row=i+1, column=6)
        Button(self, text="Back", command=lambda: self.clear_screen()).grid(row=1, column=1)


    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.controller.main_screen()
        



    """def display_teams(self, table):
        self.grid_columnconfigure(0, weight=1)
        self.league_table = LeagueTableFrame(self)
        self.league_table.grid(row=0, column=0, sticky="ew")
        self.league_table.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.league_table.grid_columnconfigure(0, weight=1)
        for i, team in enumerate(table):
            row = Frame(self.league_table, bg="white")
            row.grid_columnconfigure(0, minsize=40)
            row.grid_columnconfigure(1, minsize=250)
            row.grid_columnconfigure(2, minsize=60)
            row.grid_columnconfigure(3, minsize=60)
            row.grid_columnconfigure(4, minsize=60)
            row.grid_columnconfigure(5, minsize=60)
            row.grid(row=i, column=0, sticky="ew")
            row.grid_columnconfigure(1, weight=1)

            Label(row, text=f"{i+1})").grid(row=0, column=0, padx=10)
            Label(row, text=team.get_name(), anchor="w").grid(row=0, column=1, sticky="ew")
            Label(row, text=team.points).grid(row=0, column=2, padx=10)
            Label(row, text=team.goals_scored).grid(row=0, column=3, padx=10)
            Label(row, text=team.goals_conceded).grid(row=0, column=4, padx=10)
            Label(row, text=team.goals_scored - team.goals_conceded).grid(row=0, column=5, padx=10)
        Button(self, text="Back", command=lambda: self.controller.main_screen()).grid(column=6, row=10)"""

