from tkinter import Frame, Label, Button

class ResultsScreen(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller


    def display_teams(self, table):
        temp = [Label(self, text=team) for team in table]
        for t in temp:
            t.pack()
        Button(self, text="Back", command=lambda: self.controller.main_screen()).pack()
