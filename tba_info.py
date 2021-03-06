#!/usr/bin/python3
# https://github.com/frc1418/tbapy

import tbapy
import json
import sys
import numpy as np
import pandas as pd
from tabulate import tabulate
import csv

try:
    from tba_token import key
    tba = tbapy.TBA(key)
except ImportError:
    print("Can't open the tba key file")
    raise

# setup
myteam = 997
m_year = 2022
district = 'pnw'
team_key = 'frc' + str(myteam)
district_key = str(m_year) + district
event_key = str(m_year) + 'orwil'

# Which teams are in this district
#  Fields we need:
#       key, nickname, city

# need to rearrange json into dataframe keyed to 'key'
#
#teams = tba.district_teams(district_key, simple=True)
#df_pre = pd.json_normalize(teams)
#df_teams = df_pre[['key', 'city', 'state_prov', 'team_number', 'nickname']].sort_values(by=['team_number'])
#print("Pacific Northwest Teams:")
#with pd.option_context('display.max_rows', None,
#                       'display.max_columns', None,
#                       'display.precision', 3,
#                       ):
#   print(df_teams[['key', 'nickname']])


# Which teams are coming to a same event as my test amd which other events are
# they going to.
# pnw_team_events={}
# for _team in teams:
#     #print(json.dumps(_team, indent=4, sort_keys=True))
#     #print("Team: ", _team['key'])
#     team_events = tba.team_events(_team['key'], year=m_year, simple=True)
#     for team_event in team_events:
#         #print(json.dumps(team_event, indent=4, sort_keys=True))
#         if team_event['event_type'] < 2:
#             mylist = pnw_team_events.get(_team['key'])
#             if mylist:
#                 mylist.append(team_event['key'])
#             else:
#                 # key not found
#                 mylist = [team_event['key']]
#                 pnw_team_events[_team['key']] = mylist
                
#for team in pnw_team_events:
#    if any(elem in pnw_team_events[team_key] for elem in  pnw_team_events[team]):
#        print(team, ": ",pnw_team_events[team])

    
# Unpack the match data.
#
# Need to iterate across matches in current and previous events to our current event
# and generate the model features we need to predict the outcome.
#
# For each event in the district, get a list of teams and find
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

# For predictions in 2019 we need to know:
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

# Need to break the event data apart and map them to each tea

# 2/3/2022:
# We actually need to seperate by match and then index by team number (so in a csv file they
# would show up as a column per team and a row per match).  Then sort by match number and align rows.
# Then add the metch results (auto score, teleop score, etc) to the match row.  This should allow
# calculation of OPR and CCWR after removing penaly points.


# event_teams = tba.event_teams(event_key, simple=False)
# print (event_key, "has", len(event_teams), "teams")
# i=0
# team={}
# for iteam in event_teams:
#     team[iteam["key"]] = i
#     #print(i," : ", iteam["key"])
#     i += 1

# 6/8/2022:
# We need a simpler list.
# From /event/{event_key}/matches -> event_matches
# ... really only interested in qualification matches (i.e. where 'comp_level' = 'qm')
# team_key : event_key_match_key : 

match_data = [['match_number', 'comp_level', 'team', 'alliance', 'auto points', 'taxi points', 'foul points', 'teleop points',
                     'endgame_points', 'hanger ranking pt', 'score', 'rp']]
matches = tba.event_matches(event_key, simple=False)
idx=0
for match in matches:
    if match["comp_level"] != "qm":
        continue
    print("... key:", match['comp_level'], match['match_number'])
    print("Index: ",idx,", Comp Level:",match["comp_level"])
    df = pd.json_normalize(match, "score_breakdown")
    sb = match["score_breakdown"]
    #print(json.dumps(match, indent=4, sort_keys=True))
    #print(json.dumps(sb, indent=4, sort_keys=True))
    for alliance in ["red", "blue"]:
        auto_points = sb[alliance]["autoPoints"]
        taxi_points = sb[alliance]["autoTaxiPoints"]
        teleop_points = sb[alliance]["teleopPoints"]
        foul_points = sb[alliance]["foulPoints"]
        endgame_points = sb[alliance]["endgamePoints"]
        rp = sb[alliance]["rp"] # ranking points
        alliance_info = match["alliances"][alliance]
        alliance_teams = alliance_info["team_keys"]
        for team in alliance_teams:
            #print (alliance, " team: ", team,
            #   ", Auto Points:", auto_points, ", Foul Points:", foul_points, "Teleop Points:", teleop_points,
            #   ", Endgame Points:", endgame_points, ", Alliance Score:", alliance_info["score"], ", Ranking Points:", rp)
            matchinfo = (match['match_number'], match['comp_level'], team, alliance, auto_points, taxi_points, foul_points, teleop_points,
                     endgame_points, sb[alliance]["hangarBonusRankingPoint"], alliance_info['score'], rp)
            match_data.append(matchinfo)
            #print(matchinfo)
    idx += 1

print(tabulate(match_data, headers='firstrow'))

with open('first.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(match_data)
