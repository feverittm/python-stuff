#!/usr/bin/python3
# https://github.com/frc1418/tbapy

import tbapy
import json

try:
    from tba_token import key
    tba = tbapy.TBA(key)
except ImportError:
    print("Can't open the tba key file")
    raise

# setup
myteam = 997
m_year = 2019
district = 'pnw'
team_key = 'frc' + str(myteam)
district_key = str(m_year) + district

# what events were in the district?
events = tba.district_events(district_key, simple=True)
for event in events:
    #print(json.dumps(event, indent=4, sort_keys=True))
    print(event['key'])

# which teams are in this district
teams = tba.district_teams(district_key, simple=True)
#for team in teams:
#    print(json.dumps(team, indent=4, sort_keys=True))

# which events did my team participate in during the specified year
team_events = tba.team_events(team_key, year=m_year, simple=True)
for team_event in team_events:
    if team_event['event_type'] < 5:
        #print(json.dumps(team_event, indent=4, sort_keys=True))
        print(team_event['event_code']," ",team_event['name'])
    

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

# For each event (let's focus on one event first...) create a table/list of each match and
# include: event_id, match_type, match_id, 