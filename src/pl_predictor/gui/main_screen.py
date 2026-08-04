from tkinter import Frame, Button, Checkbutton
from pl_predictor.gui.results_screen import ResultsScreen
from pl_predictor.data.data import get_team_names
from pl_predictor.gui.team_selection import TeamSelectionFrame
from pl_predictor.gui.condition_selection import ConditionSelectionFrame
from pl_predictor.simulation.simulate import simulate_season
from pl_predictor.data.data import get_team_rating
from pl_predictor.models.team import Team

class MainScreen(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        Button(self, text="Switch frame", command=lambda : controller.show_frame(ResultsScreen)).grid(row=1, column=1) # test
        self.team_selection_frame = TeamSelectionFrame(self)
        self.team_selection_frame.grid(row=0, column=0, rowspan=3)
        self.condition_selection_frame = ConditionSelectionFrame(self)
        self.condition_selection_frame.grid(row=0, column=1)
        Button(self, text="Simulate", command=lambda :self.start_simulation() ).grid(row=3, column=3)

    def start_simulation(self):
        league_teams, champion, relegated_teams, max_sims = self.get_simulation_conditions()
        team_ratings = {}
        for team in league_teams:
            team_ratings[team] = Team(team, get_team_rating(team))
        for i in range(max_sims):
            print(f"Simulation: {i+1}")
            table = simulate_season(team_ratings)
            if champion != "Any" and champion == table[0].get_name():
                break
            for team in table:
                team.reset()
        print([(t.get_name(), t.points) for t in table])



    def get_simulation_conditions(self) -> tuple[list]:
        """gets the simulation conditions: teams selected, champion, relegated teams, maximum simulations.

        Returns:
            tuple[list]: ([selected teams], [champion], [relegated teams], [max sims])
        """
        return (self.team_selection_frame.get_selected_teams(), self.condition_selection_frame.get_selected_champion(),
                 self.condition_selection_frame.get_relegated_teams(), self.condition_selection_frame.get_max_sims())
        ...




