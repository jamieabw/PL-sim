from pl_predictor.models.single_poisson_dist import Single_Poisson_Distribution
from pl_predictor.data.data import get_league_averages
import numpy as np
def simulate_xg(home_team_rating: tuple, away_team_rating: tuple, league_averages: tuple) -> tuple:
    """gets the predicted xg for the game given the home team and away team's ratings.

    Args:
        home_team_rating (tuple): (attack rating (H), defence rating (H), attack rating (A), defence rating (A))
        away_team_rating (tuple): (attack rating (H), defence rating (H), attack rating (A), defence rating (A))
        league_averages (tuple): (average home goals, average away goals)

    Returns:
        tuple: (home xG, away xG)
    """
    home_xG = league_averages[0] * home_team_rating[0] * away_team_rating[3] # average home goals x home team attack x away team defence
    away_xG = league_averages[1] * away_team_rating[2] * home_team_rating[1] # average away goals x away team attack x home team defence
    return (home_xG, away_xG)

def build_score_matrix(home_xG, away_xG) -> list[list]:
    """creates a 2D array representing the probabilities of each scoreline.

    Args:
        home_xG (_type_): _description_
        away_xG (_type_): _description_

    Returns:
        list[list]: _description_
    """
    score_matrix = []
    for home in range(7):
        temp = []
        for away in range(7):
            temp.append(Single_Poisson_Distribution.calculate(home_xG, home) * Single_Poisson_Distribution.calculate(away_xG, away))
        score_matrix.append(temp)
    return score_matrix

def get_scoreline_probabilities(score_matrix: list[list]) -> tuple[list]:
    """gets the probabilites associated with their scorelines

    Args:
        score_matrix (list[list]): score matrix which has probabilities of [home_score][away_score]

    Returns:
        tuple[list]: (probabilities, associated_scorelines)
    """
    probabilities = []
    for away in range(7):
        for home in range(7):
            probabilities.append(score_matrix[home][away])
    total = sum(probabilities)
    probabilities = [p / total for p in probabilities] # normalise to ensure they sum to 1
    scorelines = []
    for away in range(7):
        for home in range(7):
            scorelines.append((home,away))
    #print(scorelines)
    return (probabilities, scorelines)

def simulate_game(home_team_rating: tuple, away_team_rating: tuple, league_averages: tuple) -> tuple:
    """simulates the scoreline of a game given two team's ratings and the league averages.

    Args:
        home_team_rating (tuple): attack rating (H), defence rating (H), attack rating (A), defence rating (A))
        away_team_rating (tuple): attack rating (H), defence rating (H), attack rating (A), defence rating (A))
        league_averages (tuple): (average home goals, average away goals)

    Returns:
        tuple: (home goals, away goals)
    """    
    home_xG, away_xG = simulate_xg(home_team_rating, away_team_rating, league_averages)
    probabilities, scorelines = get_scoreline_probabilities(build_score_matrix(home_xG, away_xG))
    index = np.random.choice(len(scorelines), p=probabilities)
    home, away = scorelines[index]
    return (home, away)


"""build_score_matrix(2.8345535445214587, 0.43235276054781063) # Arsenal vs Norwich City for testing purposes.
get_scoreline_probabilities(build_score_matrix(2.8345535445214587, 0.43235276054781063))"""

ARSENAL = (1.3135735938026274, 0.7467911318553092, 1.3146635550369505, 0.653418659481307)
CITY = (1.7177500842034354, 0.6845585375340334, 1.47024504084014, 0.5456382620410913)

league_avg = get_league_averages()
for i in range(10):
    print(simulate_game(CITY, ARSENAL, league_avg)) # test CITY VS ARSENAL 10 times
    """
    (1, 2)
    (1, 1)
    (1, 3)
    (3, 1)
    (3, 2)
    (2, 2)
    (1, 0)
    (2, 2)
    (1, 2)
    (1, 3)
    """


