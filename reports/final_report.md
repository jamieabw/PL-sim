# Final report

---
## Overview

The simulator I have created accurately simulates premier league seasons until user-chosen conditions are all fulfilled, it uses multithreading to allow the UI to be updated simulataneously along the simulations occurring.

---

## How simulations work

The simulations work by assigning each team a home and away attack and defence rating, these are calculated by finding the league average home goals, away goals, and then dividing total home goals by the average and so on to calculate each rating. This surprisingly simple approach works extremely well compared to other approaches such as ELO which give poor results.

After ratings are calculated, to simulate a game, the team ratings of both teams are used in the formula below to find the predicted xG for both teams. There is no need for any home advantage to be hardcoded in as the home ratings will reflect each team's personal home advantage. After xG has been calculated, a poisson distribution is used to calculate every possible scoreline up to 6-6, these are then placed alongside their probabilities of occurring given the xG of the teams, then a dixon-coles correct is applied. Dixon-coles makes the simulation more accurate as whilst poisson is accurate, low scoring games in football are more common than given credit by poisson, so a small correction to scorelines up to 1-1 are applied. A scoreline is then chosen based on randomised choosing which is weighted on the given probabilities.

home_xG = EPL league average home goals * home attack rating * away defence rating

away_xG = EPL league average away goals * away attack rating * home defence rating

---

## Data collection

To find the data used, such as team ratings, league averages, etc, I used a dataset which composed of the match result of every game from 2020-2021 to 2023-2024 seasons. Also, given that football rapidly changes season to season due to numerous things such as transfers, I added a time weighting multiplier to the games given how long ago they occurred relative to 2024, that formula is below.

e ** ((-TIME_FACTOR) * (2025 - year))

where e = Euler's number and TIME_FACTOR = 0.2 for this simulator

---

## What could be improved

Firstly, when simulating, the UI will inconsistently update, this is due to python GIL (Global Interpreter Lock), which makes threads compete for processing. This could be solved through the use of multithreading, which would be useful for future updates.

Secondly, an updated dataset to include the reason seasons of 2024-2025 and 2025-2026 would allow the simulator to be much more accurate, as it is already outdated by 2 years, which in football terms is significant.

Finally, dynamic ratings is also something I will consider, as currently team ratings are static after the previous seasons data has been processed. This can be improved by instead allowing the simulated games of a season to impact team ratings much more, as in real life recent form places a massive role in performances.
