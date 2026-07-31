class Team:
    def __init__(self, name: str, rating: tuple):
        self.__name = name
        self.__rating = rating
        self.points = 0

    def get_name(self) -> str:
        return self.__name

    def get_rating(self) -> tuple:
        return self.__rating

    def reset_points(self):
        self.points = 0