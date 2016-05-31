# Shubhi Jain
# Cricket Analysis
'''
This file is my first attempt at analyzing t20 cricket matches to answer some
interesting questions!

This week's question:
'''

import pandas as pd, numpy as np, matplotlib.pyplot as plt

from util import *
from pprint import pprint

if __name__ == "__main__":
    # Just a quick test
    FILENAME = 'data/ipl/335982.yaml'
    match = data_to_match(FILENAME)
    pprint(match.team_1)
    pprint([(bowler.name, bowler.runs, bowler.wickets) for bowler in match.bowlers[match.team_1]])
    pprint(match.team_2)
    pprint([(bowler.name, bowler.runs, bowler.wickets) for bowler in match.bowlers[match.team_2]])
