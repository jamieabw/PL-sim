import pandas as pd

DATA = "./datasets/processed/final_matches_processed.csv"
TIME_FACTOR = 1
LEAGUE_AVG = (1.5626315789473684, 1.3531578947368421)
e = 2.71828



def get_league_averages() -> tuple:
    """gets the league average home and away goals per game from historical data.

    Returns:
        tuple: first element is average home goals per game, second element is average away goals per game.
    """    
    total_home_goals, total_away_goals = (0,0)
    df = pd.read_csv(DATA)
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
    teams = {}
    df = pd.read_csv(DATA)
    for index, row, in df.iterrows():
        if row["team"] not in teams.keys() or row["opponent"] not in teams.keys():
            if row["team"] == "team":
                continue
            if row["team"] in "West Bromwich Albion Watford Southampton Sheffield United Luton Town Norwich City Leicester City": # temp for testing purposes.
                continue
            teams[row["team"]] = 0
    return teams.keys()


def get_team_home_stats(team_name: str) -> tuple:
    """ get home stats for a specified teams

    Args:
        team_name (str): name of the team you want the stats for.

    Returns:
        tuple: (home games played, home goals scored, goals conceded)
    """    
    home_goals_scored: int = 0
    home_goals_conceded: int = 0
    home_games: int = 0
    df = pd.read_csv(DATA)
    for index, row in df.iterrows():
        if row["team"] == team_name and row["venue"] == "Home": # home game for the specified team
            home_games += 1
            home_goals_scored += int(row["gf"])
            home_goals_conceded += int(row["ga"])
    return (home_games, home_goals_scored, home_goals_conceded)

def get_team_away_stats(team_name: str) -> tuple:
    """get away stats for a specifiec teams

    Args:
        team_name (str): name of the team you want the stats for.

    Returns:
        tuple: (away games played, away goals scored, away goals conceded)
    """    
    away_goals_scored: int = 0
    away_goals_conceded: int = 0
    away_games: int = 0
    df = pd.read_csv(DATA)
    for index, row in df.iterrows():
        if row["opponent"] == team_name and row["venue"] == "Home": # away game for the specified team
            away_games += 1
            away_goals_scored += int(row["ga"])
            away_goals_conceded += int(row["gf"])
    return (away_games, away_goals_scored, away_goals_conceded)

"""def get_team_games_played(team_name: str) -> int:
    ... prbably not needed"""


def get_team_rating(team_name: str) -> tuple:
    """gets the attack and defence rating of a particular team

    Args:
        team_name (str): the name of the team you want the ratings of

    Returns:
        tuple: a tuple consisting of (attack rating HOME, defence rating HOME, attack rating AWAY, defence rating AWAY)
    """
    home_games, home_goals_scored, home_goals_conceded = get_team_home_stats(team_name)
    away_games, away_goals_scored, away_goals_conceded = get_team_away_stats(team_name)
    average_home_goals, average_away_goals = LEAGUE_AVG
    return ((home_goals_scored / home_games) / average_home_goals,
             (home_goals_conceded / home_games) / average_away_goals, (away_goals_scored / away_games) / average_away_goals,
               (away_goals_conceded / away_games) / average_home_goals)


def get_time_weighting(year: int) -> float:
    """gets the time weighting to weight older matches less than newer ones.

    Args:
        year (int): the year the game took place

    Returns:
        _float_: the time weighting
    """    
    ...
    return e ** (-TIME_FACTOR * 2024 - year)


def output_all_team_ratings():
    team_names = get_team_names()
    print("TEAM NAME : (ATTACK RATING (H), DEFENCE RATING (H), ATTACK RATING (A), DEFENCE RATING (A))")
    for team in team_names:
        print(f"{team} : {get_team_rating(team)}")

#print(get_league_averages())
#output_all_team_ratings()