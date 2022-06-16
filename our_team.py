#!/usr/bin/python3
# https://github.com/frc1418/tbapy

import tbapy
import json
import sys
import numpy as np
import pandas as pd
import tabulate

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

# Which events did we go to this year...

mylist = ()
team_events = tba.team_events(team_key, year=m_year, simple=True)
for team_event in team_events:
    print(json.dumps(team_event, indent=4, sort_keys=True))
    if team_event['event_type'] <= 2:
        if mylist:
            mylist.append(team_event['key'])
        else:
            # key not found
            mylist = [team_event['key']]

for event in mylist:
    print(event)
    oprs=tba.event_oprs(event)
    #print(json.dumps(oprs, indent=4, sort_keys=True))
    print('oprs: :',oprs['oprs']['frc997'])
    print('dprs: :',oprs['dprs']['frc997'])
    print('ccwms: :',oprs['ccwms']['frc997'])