from pl_predictor.models.single_poisson_dist import Single_Poisson_Distribution
import pandas as pd

df = pd.read_csv("./data/raw/final_matches.csv")
print(df["team"])