from tkinter import Frame, Listbox, OptionMenu, StringVar, Entry, Label
from pl_predictor.data.data import teams

class ConditionSelectionFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.champion_condition = StringVar(self, "Any")
        self.max_sims = StringVar(self, 10000)
        team_options = teams
        team_options.append("Any")
        self.champion_option = OptionMenu(self, self.champion_condition, *team_options)
        self.champion_option.grid(row=0, column=1)
        Label(self, text="Champion").grid(row=0, column=0)
        Label(self, text="Maximum simulations").grid(row=1, column=0)
        self.max_sims_option = Entry(self, textvariable=self.max_sims)
        self.max_sims_option.grid(row=1, column=1)
        self.relegation_option = Listbox(self, selectmode="multiple")
        for team in team_options:
            self.relegation_option.insert("end", team)
        self.relegation_option.bind("<<ListboxSelect>>", self.limit_selection)
        self.relegation_option.grid(row=2, column=1)
        Label(self, text="Relegation (MAX 3)").grid(row=2, column=0)

    def limit_selection(self, event):
        selected = self.relegation_option.curselection()
        if len(selected) > 3:
            self.relegation_option.selection_clear(selected[-1]) # clear the previous selection if more than 3 selected