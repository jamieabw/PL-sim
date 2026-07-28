from pl_predictor.data.data import get_team_names, DATA, pd
CORRECT_TEAM_NAMES = ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton And Hove Albion', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton',
               'Fulham', 'Ipswich Town', 'Leeds United', 'Leicester City', 'Liverpool', 'Luton Town', 'Manchester City', 'Manchester United',
                 'Newcastle United', 'Norwich City', 'Nottingham Forest', 'Sheffield United', 'Southampton', 'Tottenham Hotspur', 'Watford',
                   'West Bromwich Albion', 'West Ham United', 'Wolverhampton Wanderers']

def get_opp_names() -> list:
    """Gets the names of the teams in the opponent column of the csv, usually the one with the incorrect names

    Returns:
        list: alphabetically sorted list of team names which appear in the opponents column
    """    
    df = pd.read_csv(DATA)
    opps= {}
    for index, row in df.iterrows():
        if row["opponent"] not in opps.keys():
            opps[row["opponent"]] = 0
    return sorted(opps.keys())


def process_team_names():
    """Fixes team names to make them consistent across the dataset
    """    
    team_names = {}
    incorrect_names = get_opp_names()
    for i in range(len(CORRECT_TEAM_NAMES)):
        team_names[incorrect_names[i]] = CORRECT_TEAM_NAMES[i]
    print(team_names)
    with open(DATA, "r", encoding="utf-8") as f:
        data = f.read()
    with open("./datasets/processed/final_matches_processed.csv", "w", encoding="utf-8") as g:
        for team in team_names.keys():
            data = data.replace(team, team_names[team])
        g.write(data)

def fix_specific_team_names():
    """Fixes specific team names which cannot be fixed through the original process_team_names()
    """    
# specific team names which are included in the incorrect name break, spurs and brighton
    wrong_names = {"Tottenham Hotspur Hotspur" : "Tottenham Hotspur", "Brighton And Hove Albion And Hove Albion" : "Brighton And Hove Albion",
                   "West Bromwich Albionwich Albion" : "West Bromwich Albion", "West Ham United United" : "West Ham United"}
    for team in wrong_names.keys():
        with open("./datasets/processed/final_matches_processed.csv", "r", encoding="utf-8") as f:
            data = f.read()
        with open("./datasets/processed/final_matches_processed.csv", "w", encoding="utf-8") as g:
            data = data.replace(team, wrong_names[team])
            g.write(data)


fix_specific_team_names()