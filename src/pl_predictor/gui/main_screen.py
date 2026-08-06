from tkinter import Frame, Button, Checkbutton, messagebox
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
        self.team_selection_frame = TeamSelectionFrame(self)
        self.team_selection_frame.grid(row=0, column=0, rowspan=3)
        self.condition_selection_frame = ConditionSelectionFrame(self)
        self.condition_selection_frame.grid(row=0, column=1)
        Button(self, text="Simulate", command=lambda :self.start_simulation() ).grid(row=3, column=3)


    def check_simulation(self, league_teams: list[str], champion: str, relegated_teams: list[str], max_sims: int, min_champ_points: int) -> bool:
        """checks whether simulation conditions are valid for the selected teams, before beginning simulating.

        Args:
            league_teams (list[str]): list of teams selected to simulate EPL with
            champion (str): team to simulate until theyre the chmapion
            relegated_teams (list[str]): teams to simulate until theyre all relegated
            max_sims (int): maximum sims to perform for conditions to match
            min_champ_points (int): the minimum points a team wins EPL with

        Returns:
            bool: true if conditions are not compatible, false if they are compatible 
        """
        return (champion not in league_teams and champion != "Any") or any(relegated_team not in league_teams for relegated_team in relegated_teams) or (len(league_teams) - 1) * 6 < min_champ_points

    def start_simulation(self):
        league_teams, champion, relegated_teams, max_sims, min_champ_points = self.get_simulation_conditions()
        if self.check_simulation(league_teams, champion, relegated_teams, max_sims, min_champ_points):
            messagebox.showerror(title="Simulation Error", message="The conditions selected are not compatible with the teams selected. Please change conditions or team selection.")
            return
        team_ratings = {}
        for team in league_teams:
            team_ratings[team] = Team(team, get_team_rating(team))
        print(self.run_simulations(league_teams, champion, relegated_teams, max_sims, min_champ_points, team_ratings))
        

    def run_simulations(self, champion: str, relegated_teams: list[str], max_sims: int, min_champ_points: int, team_ratings: dict) -> list[Team]:
        """runs simulations until conditions are met with the specified team or until the max simulation threshold is met.

        Args:
            champion (str): team to simulate until theyre the chmapion
            relegated_teams (list[str]): teams to simulate until theyre all relegated
            max_sims (int): maximum sims to perform for conditions to match
            min_champ_points (int): the minimum points a team wins EPL with
            team_ratings (dict): name of team : (tuple of team rating)

        Returns:
            list[Team]: the ordered league table of either the closest simulation (when implemented) or the simulation where conditions are met
        """        
        for i in range(max_sims):
            print(f"Simulation: {i+1}")
            table = simulate_season(team_ratings)
            if (champion == "Any" or champion == table[0].get_name()) and table[0].points >= min_champ_points:
                print(f"champion: {table[0].get_name()}")
                # this is probably not the best way to do this, temporarily here.
                flag = True
                for j in range(len(relegated_teams)):
                    if relegated_teams[j] not in f"{table[-1].get_name()} {table[-2].get_name()} {table[-3].get_name()}":
                        flag = False
                if flag:
                    break
                for team in table:
                    team.reset()
        return [(t.get_name(), t.points) for t in table]



    def get_simulation_conditions(self) -> tuple[list]:
        """gets the simulation conditions: teams selected, champion, relegated teams, maximum simulations.

        Returns:
            tuple[list]: ([selected teams], [champion], [relegated teams], [max sims])
        """
        return (self.team_selection_frame.get_selected_teams(), self.condition_selection_frame.get_selected_champion(),
                 self.condition_selection_frame.get_relegated_teams(), self.condition_selection_frame.get_max_sims(), self.condition_selection_frame.get_min_champ_points())   
        ...




