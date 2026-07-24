import pandas as pd

def get_league_averages() -> tuple:
    """gets the league average home and away goals per game from historical data.

    Returns:
        tuple: first element is average home goals per game, second element is average away goals per game.
    """    
    data = "./data/raw/final_matches.csv"
    total_home_goals, total_away_goals = (0,0)
    df = pd.read_csv(data)
    c = 0
    for index, row in df.iterrows():
        if row["venue"] == "Home":
            c += 1
            total_home_goals += int(row["gf"])
            total_away_goals += int(row["ga"])
    return (total_home_goals / c, total_away_goals / c)

def get_team_names() -> list[str]:
    """gets all team names present in the dataset.

    Returns:
        list[str]: a list of teams which appear in the dataset atleast once.
    """
    data = "./data/raw/final_matches.csv"
    teams = {}
    df = pd.read_csv(data)
    for index, row, in df.iterrows():
        if row["team"] not in teams.keys():
            teams[row["team"]] = 0
    return teams.keys()
