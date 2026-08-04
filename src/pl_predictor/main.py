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

while True:
    table = simulate_season(teams)
    if table[19].points == 0:
        break
    for team in table:
        team.reset()

for idx, team in enumerate(table):
    print(f"{idx + 1}) {team.get_name()} : {team.points} points : {team.goals_scored - team.goals_conceded} GD")
