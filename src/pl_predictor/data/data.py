import pandas as pd
from math import e
DATA = "./datasets/processed/final_matches_processed.csv"
TIME_FACTOR = 0.2
LEAGUE_AVG = (1.5626315789473684, 1.3531578947368421)
teams = ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton And Hove Albion', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Ipswich Town',
          'Leeds United', 'Leicester City', 'Liverpool', 'Luton Town', 'Manchester City', 'Manchester United', 'Newcastle United', 'Norwich City', 'Nottingham Forest',
            'Sheffield United', 'Southampton', 'Tottenham Hotspur', 'Watford', 'West Bromwich Albion', 'West Ham United', 'Wolverhampton Wanderers']


precalculated_ratings = {
    "Arsenal" : (1.3504489211058675, 0.7319490666854639, 1.3481009765010645, 0.6259769408285687),
    "Aston Villa" : (1.201198244479833, 0.9486135313802051, 0.9290591795967746, 0.9372089296742059),
    "Bournemouth" : (0.7917753180068172, 0.9015513441306777, 1.0704395813492598, 1.2280698480939969),
    "Brentford" : (1.100717343457286, 1.1065792651392294, 0.9960149096374009, 0.9463810616288407),
    "Brighton And Hove Albion" : (0.9627343336806715, 0.9446177405193531, 1.122517248357838, 1.018158592743009),
    "Burnley" : (0.5881236102021852, 1.3071139271384218, 0.7563472491257779, 1.0493225645567472),
    "Chelsea" : (1.1461448962054246, 0.8051341425967344, 1.1334407278046132, 0.8517611750716787),
    "Crystal Palace" : (0.8902738987909656, 0.9638282239450081, 0.8718829897860523, 0.9641252191762754),
    "Everton" : (0.7759620378950888, 0.9161414729268207, 0.690625058273652, 0.9621466081186215),
    "Fulham" : (0.884962141707784, 1.0810672632308156, 0.937513313817087, 0.9355052709447891),
    "Ipswich Town" : (0.47153923880094306, 1.7113963438350837, 0.8556981719175418, 1.2798922196025597),
    "Leeds United" : (0.8163046326147914, 1.2843256684342719, 0.9941899226924069, 1.3083711689652446),
    "Leicester City" : (0.8122795151913024, 1.1398571167119262, 0.982607218139236, 1.290310633965491),
    "Liverpool" : (1.4765563668412767, 0.6161320832174152, 1.5163864233758404, 0.8110726570157584),
    "Luton Town" : (0.943078477601886, 1.4391287436795017, 0.9334889148191363, 1.616705961603233),
    "Manchester City" : (1.7011366238286483, 0.7067694102144858, 1.4400446846804777, 0.5721669113366753),
    "Manchester United" : (1.034905542845003, 0.91776358791439, 0.9645884649782501, 0.9569752237541238),
    "Newcastle United" : (1.2575587533509527, 0.8593132956682525, 1.0907253779409716, 1.0114893405712069),
    "Norwich City" : (0.40417649040080844, 1.6725009723842865, 0.427849085958771, 1.3809363422027623),
    "Nottingham Forest" : (0.8958652886987754, 0.8852400196603107, 0.8967410849622108, 1.2149826690640178),
    "Sheffield United" : (0.5564026319831783, 1.8035662849775902, 0.5120673064879955, 1.4517419794032922),
    "Southampton" : (0.6429653890804073, 1.402302601635139, 0.6400146483296493, 1.3385854250323113),
    "Tottenham Hotspur" : (1.23142241841088, 1.0403994541793082, 1.2540853131059753, 1.024461005437043),
    "Watford" : (0.5725833614011452, 1.7891870867366784, 0.661221314663555, 1.0441226002020885),
    "West Bromwich Albion" : (0.5052206130010107, 1.5169194865810973, 0.7779074290159473, 1.2462108454024927),
    "West Ham United" : (0.9494234626538872, 1.0837737235637863, 0.9566163043893434, 1.0759198362282307),
    "Wolverhampton Wanderers" : (0.7865499342381982, 1.0587374609486517, 0.7953976132521066, 1.0927564939000285)
}



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
            """if row["team"] in "Ipswich Town Watford Southampton Sheffield United Luton Town Norwich City Leicester City": # temp for testing purposes.
                continue"""
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
            weighting = float(get_time_weighting(int(row["season"]))) # decay the effect depending on how old
            home_games += weighting
            home_goals_scored += int(row["gf"]) * weighting
            home_goals_conceded += int(row["ga"]) * weighting
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
            weighting = float(get_time_weighting(int(row["season"]))) # decay the effect depending on how old
            away_games += weighting
            away_goals_scored += int(row["ga"]) * weighting
            away_goals_conceded += int(row["gf"]) * weighting
    return (away_games, away_goals_scored, away_goals_conceded)

"""def get_team_games_played(team_name: str) -> int:
    ... prbably not needed"""


def get_team_rating_from_data(team_name: str) -> tuple:
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

def get_team_rating(team_name: str) -> tuple:
    """gets the precalculated team rating.

    Args:
        team_name (str): team name for the team to get ratings for

    Returns:
        tuple: home attack, home defence, away attack, away defence ratings in that order
    """    
    return precalculated_ratings[team_name]


def get_time_weighting(year: int) -> float:
    """gets the time weighting to weight older matches less than newer ones.

    Args:
        year (int): the year the game took place

    Returns:
        _float_: the time weighting
    """    
    ...
    return e ** ((-TIME_FACTOR) * (2025 - year))


def output_all_team_ratings():
    team_names = get_team_names()
    print("TEAM NAME : (ATTACK RATING (H), DEFENCE RATING (H), ATTACK RATING (A), DEFENCE RATING (A))")
    for team in team_names:
        print(f"{team} : {get_team_rating(team)}")

