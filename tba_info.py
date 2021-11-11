#!/usr/bin/python3
# https://github.com/frc1418/tbapy

import tbapy
import json

try:
    from tba_key import key
    tba = tbapy.TBA(key)
except ImportError:
    print("Can't open the tba key file")
    raise

# setup
year = str(2019)
district = year + 'pnw'

# what events were in the district?
events = tba.district_events(district, simple=True)
for event in events:
    #print(json.dumps(event, indent=4, sort_keys=True))
    print(event['key'])

# which teams are in this district
teams = tba.district_teams('2019pnw', simple=True)
for team in teams:
    print(json.dumps(team, indent=4, sort_keys=True))

# for each event in the district, get a list of teams and find
# which matches they participate in and then extract the information
# for that match.

# if it is possible to seperate a team's contribution to the final score
# then we can apply matrix algebra and predict the outcome of a match and
# even possibly the event?
# possible predictor/factors: opr, average score
# 

# https://www.chiefdelphi.com/t/overview-and-analysis-of-first-stats/144569
# The well-known Offensive Power Rating (OPR), Combined Contribution to Winning Margin (CCWM),
# and Defensive Power Rating (DPR) measures are discussed and analyzed.