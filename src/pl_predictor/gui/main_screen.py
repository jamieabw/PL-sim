from tkinter import Frame, Button, Checkbutton, messagebox, Toplevel, Label
from pl_predictor.gui.results_screen import ResultsScreen
from pl_predictor.data.data import get_team_names
from pl_predictor.gui.team_selection import TeamSelectionFrame
from pl_predictor.gui.condition_selection import ConditionSelectionFrame
from pl_predictor.simulation.simulate import simulate_season
from pl_predictor.data.data import get_team_rating
from pl_predictor.models.team import Team
import queue
import threading

class MainScreen(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        self.progress_queue = queue.Queue()
        self.team_selection_frame = TeamSelectionFrame(self)
        self.sim_label = Label(self)
        self.team_selection_frame.grid(row=0, column=0, rowspan=3)
        self.condition_selection_frame = ConditionSelectionFrame(self)
        self.condition_selection_frame.grid(row=0, column=1)
        self.sim_button = Button(self, text="Simulate", command=lambda :self.start_simulation() )
        self.sim_button.grid(row=3, column=3)
        self.sim_cancel_button = Button(self, text="Cancel Simulation", command=lambda : self.cancel_simulation(), state="disabled")
        self.sim_cancel_button.grid(row=3, column=4)
        self.cancel_event = threading.Event()

    def cancel_simulation(self):
        if self.sim_thread.is_alive():
            self.cancel_event.set()


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
        self.cancel_event.clear()
        self.sim_cancel_button.config(state="normal")
        self.sim_label.grid(row=4, column=3)
        if self.check_simulation(league_teams, champion, relegated_teams, max_sims, min_champ_points):
            messagebox.showerror(title="Simulation Error", message="The conditions selected are not compatible with the teams selected. Please change conditions or team selection.")
            return
        self.sim_button.config(state="disabled")
        self.sim_thread = threading.Thread(target=self.run_simulations, args=(league_teams, champion, relegated_teams, max_sims, min_champ_points), daemon=True)
        self.sim_label.config(text="Starting Simulation...", fg="black")
        self.sim_thread.start()
        self.after(50, self.check_progress)
        #table = self.run_simulations(champion, relegated_teams, max_sims, min_champ_points, team_ratings)
        #self.controller.show_frame(ResultsScreen)
        #self.controller.frame.display_teams(table)


    def check_progress(self):
        try:
            message_title, data = self.progress_queue.get_nowait()
            if message_title == "progress":
                self.sim_label.config(text=f"Simulation: {data}")
            elif message_title == "complete":
                self.sim_button.config(state="normal")
                self.sim_cancel_button.config(state="disabled")
                self.controller.show_frame(ResultsScreen)
                self.controller.frame.display_teams(data)
                return
            elif message_title == "cancelled":
                self.sim_button.config(state="normal")
                self.sim_cancel_button.config(state="disabled")
                self.sim_label.config(text="Simulation Cancelled.")
            elif message_title == "failure":
                self.sim_button.config(state="normal")
                self.sim_cancel_button.config(state="disabled")
                self.sim_label.config(text="No simulations found.", fg="red")
        except queue.Empty:
            pass
        self.after(10, self.check_progress)
        

    def run_simulations(self, league_teams: list[str], champion: str, relegated_teams: list[str], max_sims: int, min_champ_points: int) -> list[Team]:
        """runs simulations until conditions are met with the specified team or until the max simulation threshold is met.

        Args:
            league_teams (list[str]) : list of league teams to simulate
            champion (str): team to simulate until theyre the chmapion
            relegated_teams (list[str]): teams to simulate until theyre all relegated
            max_sims (int): maximum sims to perform for conditions to match
            min_champ_points (int): the minimum points a team wins EPL with

        Returns:
            list[Team]: the ordered league table of either the closest simulation (when implemented) or the simulation where conditions are met
        """
        team_ratings = {}
        for team in league_teams:
                    team_ratings[team] = Team(team, get_team_rating(team))
        for i in range(max_sims):
            
            if i % 5 == 0:
                self.progress_queue.put(("progress", i+1))
            table, match_results = simulate_season(team_ratings)
            if (champion == "Any" or champion == table[0].get_name()) and table[0].get_points() >= min_champ_points:
                #print(f"champion: {table[0].get_name()}")
                # this is probably not the best way to do this, temporarily here.
                flag = True
                for j in range(len(relegated_teams)):
                    if relegated_teams[j] not in f"{table[-1].get_name()} {table[-2].get_name()} {table[-3].get_name()}":
                        flag = False
                if flag:
                    self.progress_queue.put(("complete", (table, match_results)))
                    return
            if self.cancel_event.is_set():
                self.progress_queue.put(("cancelled", None))
                return
            #print(f"champion: {table[0].get_name()}")
            #print((t.get_name(), t.points) for t in table)
            for team in table:
                team.reset()
        self.progress_queue.put(("failure", None))



    def get_simulation_conditions(self) -> tuple[list]:
        """gets the simulation conditions: teams selected, champion, relegated teams, maximum simulations.

        Returns:
            tuple[list]: ([selected teams], [champion], [relegated teams], [max sims])
        """
        return (self.team_selection_frame.get_selected_teams(), self.condition_selection_frame.get_selected_champion(),
                 self.condition_selection_frame.get_relegated_teams(), self.condition_selection_frame.get_max_sims(), self.condition_selection_frame.get_min_champ_points())   
        ...




