from pl_predictor.models.single_poisson_dist import Single_Poisson_Distribution
from pl_predictor.data.data import get_team_rating, get_team_names
from pl_predictor.models.team import Team
from pl_predictor.simulation.simulate import simulate_season
import pandas as pd

def get_teams() -> dict:
    teams = {}
    for team in get_team_names():
        teams[team] = Team(team, get_team_rating(team))
    return teams

teams = get_teams()
counter = 0
while counter < 10:
    counter +=1
    table = simulate_season(teams)
    """if table[0].get_name() == "Arsenal":
        break"""
    print(f"champion: {table[0].get_name()}")
    for team in table:
        team.reset_points()


"""for team in table:
    print(f"{team.get_name()} - {team.points}")"""
print(counter)
