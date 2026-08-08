class Team:
    def __init__(self, name: str, rating: tuple):
        self.__name = name
        self.__rating = rating
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_scored = 0
        self.goals_conceded = 0

    def get_name(self) -> str:
        return self.__name

    def get_points(self) -> int:
        return (3 * self.wins) + self.draws

    def get_rating(self) -> tuple:
        return self.__rating

    def reset(self):
        self.goals_scored = 0
        self.goals_conceded = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0

    def __gt__(self, other) -> bool:
        if self.get_points() > other.get_points():
            return True
        if self.get_points() == other.get_points():
            if self.goals_scored - self.goals_conceded > other.goals_scored - other.goals_conceded:
                return True
        return False

    def __lt__(self, other) -> bool:
        if self > other:
            return False
        if other > self:
            return True
        return False

    def __eq__(self, other) -> bool:
        if self.points == other.points and self.goals_scored - self.goals_conceded == other.goals_scored - other.goals_conceded:
            return True
        return False
