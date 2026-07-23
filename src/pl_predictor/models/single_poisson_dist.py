from math import e, factorial
class Single_Poisson_Distribution:
    @staticmethod
    def calculate(l : float, k: int) -> float:
        return ((l ** k) * (e ** -l)) / (factorial(k))