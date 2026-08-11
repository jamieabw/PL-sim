# Premier League Simulator
---

## Overview

This application allows you to choose any selection of teams, simulate a premier league season with them and also choose particular conditions which will simulate until are matched. For example, you can choose the lineup for the 2022-2023 season, and choose Tottenham to win the league, then you can see how many simulations it would take for Tottenham to win the league.

---

## How to install
- You will need python
- First, clone the repository into a folder, use your terminal to get into the folder and then run setup.bat (or the equivalent linux commands), this will install all required modules and the required virtual environment
- Then, run run.bat (or the equivalent linux commands)

---

## How to use

After the application loads, you will see a UI of a team selection and conditions selection. Firstly, choose which teams you want to simulate a season with (it can be any amount of teams, each team will play every other team twice, at home and away). Then choose the conditions you wish to simulate until you find a season which matches. The current supported conditions are as follows: Champion condition (who wins the league), Minimum champion points (Whoever wins the league needs to win the league with atleast this many points), Relegated teams (what teams are relegated, maximum of 3) and a maximum number of simulations.

Finally, after choosing your conditions you can run the simulations, by using the button. Once a match has been found, you will be shown the final league table, here you can view the match results of any of the teams to see how the league unfolded over time.