from tkinter import Frame, Label, Button, Scrollbar, Canvas
from pl_predictor.gui.match_results import MatchResultsFrame

class MatchResultsScreen(Frame):
    def __init__(self, parent, controller):
            super().__init__(parent)
            self.parent = parent
            self.controller = controller
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.canvas = Canvas(self) # think this is needed for scrollbar?
            self.match_results_frame = MatchResultsFrame(self.canvas)
            self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
            self.canvas.create_window(0, 0, window=self.match_results_frame, anchor="nw")
            self.canvas.configure(yscrollcommand=self.scrollbar.set)
            self.match_results_frame.bind("<Configure>", lambda event : self.canvas.configure(scrollregion=self.canvas.bbox("all")))
            self.canvas.grid(row=0, column=0, sticky="nsew")
            self.scrollbar.grid(row=0,column=1, sticky="ns")


    def display_match_results(self, match_results):
        for row, (teams, result) in enumerate(match_results.items()):
            Label(self.match_results_frame, text=f"{teams} {result}").grid(row=row, column=0)
        Button(self.match_results_frame, text="Back", command=self.back).grid(column=5, row=0)

    def back(self):
        for widget in self.match_results_frame.winfo_children():
            widget.destroy()
        self.controller.show_results()