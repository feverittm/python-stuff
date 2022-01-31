#!/usr/bin/python3
# https://github.com/frc1418/tbapy

import tbapy
import json
import sys
import numpy as np
import pandas as pd

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

# Which teams are in this district
#  Fields we need:
#       key, nickname, city

# need to rearrange json into dataframe keyed to 'key'
#
teams = tba.district_teams(district_key, simple=True)
df_pre = pd.json_normalize(teams)
df_teams = df_pre[['key', 'city', 'state_prov', 'team_number', 'nickname']].sort_values(by=['team_number'])
#print("Pacific Northwest Teams:")
#with pd.option_context('display.max_rows', None,
#                       'display.max_columns', None,
#                       'display.precision', 3,
#                       ):
#   print(df_teams[['key', 'nickname']])


# which events did my team participate in during the specified year
pnw_team_events={}
for _team in teams:
    #print(json.dumps(_team, indent=4, sort_keys=True))
    #print("Team: ", _team['key'])
    team_events = tba.team_events(_team['key'], year=m_year, simple=True)
    for team_event in team_events:
        #print(json.dumps(team_event, indent=4, sort_keys=True))
        if team_event['event_type'] < 2:
            mylist = pnw_team_events.get(_team['key'])
            if mylist:
                mylist.append(team_event['key'])
            else:
                # key not found
                mylist = [team_event['key']]
                pnw_team_events[_team['key']] = mylist
                
for team_event in pnw_team_events:
    if any(elem in ['2019orwil', '2019orlak'] for elem in  pnw_team_events[team_event]):
        print(team_event, ": ",pnw_team_events[team_event])
        
sys.exit()
    

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

# For prediction we need to know:
#   match key
#   Teams in the match, red/blue
#   autonomous points: "autoPoints"
#   teleoperated points: "cargoPoints", "hatchPanelPoints", "teleopPoints"
#   end game points: "habClimbPoints"
#   foul points: "foulPoints", "foulCount"
#   total match Points: "totalPoints"
#   Ranking Points: "rp"
#   "Winning Alliance"

# For each event (let's focus on one event first...) create a table/list of each match and
# include: event_id, match_type, match_id

# To start with read the match data into a dataframe indexed by the match key.

# Need to break the event data apart and map them to each team.

matches = tba.event_matches('2019orwil', simple=False)
idx=0
for match in matches:
    print("Match: ",idx,", Comp Level:",match["comp_level"])
    df = pd.json_normalize(match, "score_breakdown")
    print(json.dumps(match, indent=4, sort_keys=True))
    idx += 1
    #if match["comp_level"] != "qm":
    #    continue
    sys.exit()