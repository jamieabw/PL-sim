RHO = -0.1

def tau(home_goals: int, away_goals: int, home_xg: float, away_xg: float) -> float:
    """the tau function for dixon-coles correct, corrects the probabilities of low scoring games
    which are usually not accounted for by base poisson models.

    Args:
        home_goals (int): number of home goals scored
        away_goals (int): number of away goals scored
        home_xg (float): amount of home xG
        away_xg (float): amount of away xG

    Returns:
        float: returns the new probability for the scoreline.
    """    
    if home_goals == 0 and away_goals == 0:
        return 1 - (home_xg * away_xg * RHO)
    elif home_goals == 0 and away_goals == 1:
        return 1 + (home_xg * RHO)
    elif home_goals == 1 and away_goals == 0:
        return 1 + (away_xg * RHO)
    elif home_goals == 1 and away_goals == 1:
        return 1 - RHO
    return 1