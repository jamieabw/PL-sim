from tkinter import Frame, Label, Button

class MatchResultsScreen(Frame):
    def __init__(self, parent, controller):
            super().__init__(parent)
            self.parent = parent
            self.controller = controller

    def display_match_results(self, match_results):
        for teams, result in match_results.items():
            Label(self, text=f"{teams} {result}").pack()
        Button(self, text="Back", command=self.back).pack()

    def back(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.controller.show_results()