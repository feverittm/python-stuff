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

#print(tba.district_events('2019pnw', simple=True))
for event in tba.district_events('2019pnw', simple=True):
    #print(json.dumps(event, indent=4, sort_keys=True))
    print(event['key'])