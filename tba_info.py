#!/usr/bin/python3
# https://github.com/frc1418/tbapy

import tbapy

try:
    from tba_key import key
except ImportError:
    print("Can't open the tba key file")
    raise


tba = tbapy.TBA(key)

print(tba.status())
