# Report 1
---

## Overview

### The goal: Accurately simulate Premier League seasons.

This project aims to use historical data, along with statistical methods such as bivariate poisson + Dixon-Coles correct and poisson regression to predict the results of games, which can be chained together to predict entire premier league seasons.

---
### Steps 

1) Clean the data sets to allow easy access to data which will be useful in adjusting the models used.

2) Compute basic team strengths (such as attack and defence ratings).
    - This will be done by computing home/away attack strength, home/away defence strength as ratios vs league averages, then using particular formulas to calculate expected scorelines.

3) Replace the fixed formulas with poisson regression for higher realism, which can take into account home advantage, recency bias, etc.

4) Upgrade the score model to Dixon-Coles/bivariate poisson.

5) Integrate xG to improve regression model.

6) Add dynamic team strength (improves/worsens based on results).

7) Build the season simulator.

8) Evaluate the accuracy of the models.

- Expected goals model will use poisson regression.
- Scoreline distribution model will use bivariate poisson, however will initially use single poisson for debugging and testing purposes.