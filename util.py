# Shubhi Jain
# Cricket Analysis

import pandas as pd, numpy as np
import datetime

from models.match import Match
from models.ball import Ball
from models.bowler import Bowler
from models.batsman import Batsman


def data_to_match(filename):
    match_data = pd.read_csv(filename)
    # Get Match Information
    match_info    = match_data[match_data['version'] == 'info']
    team_1        = match_info['Unnamed: 2'].iloc[0]
    team_2        = match_info['Unnamed: 2'].iloc[1]
    gender        = match_info['Unnamed: 2'].iloc[2]
    season        = match_info['Unnamed: 2'].iloc[3]
    date          = match_info['Unnamed: 2'].iloc[4]
    print date.split('/')
    date          = datetime.date(2000 + int(date.split('/')[2]),
                                  int(date.split('/')[0]),
                                  int(date.split('/')[1]))
    comp          = match_info['Unnamed: 2'].iloc[5]
    match_num     = match_info['Unnamed: 2'].iloc[6]
    venue         = match_info['Unnamed: 2'].iloc[7]
    city          = match_info['Unnamed: 2'].iloc[8]
    toss_winner   = match_info['Unnamed: 2'].iloc[9]
    toss_decision = match_info['Unnamed: 2'].iloc[10]
    pom           = match_info['Unnamed: 2'].iloc[11]
    umpire_1      = match_info['Unnamed: 2'].iloc[12]
    umpire_2      = match_info['Unnamed: 2'].iloc[13]
    umpire_r      = match_info['Unnamed: 2'].iloc[14]
    umpire_tv     = match_info['Unnamed: 2'].iloc[15]
    match_ref     = match_info['Unnamed: 2'].iloc[16]
    winner        = match_info['Unnamed: 2'].iloc[17]
    match = Match(team_1, team_2, season, date, comp, match_num, venue, city,
                  toss_winner, toss_decision, pom, umpire_1, umpire_2, umpire_r,
                  umpire_tv, match_ref, winner)
    # Get ball, batsmen, and bowler info
    balls, batsmen = [], []
    match_happenings = match_data[match_data['version'] == 'ball']
    print match_happenings


data_to_match('data/ipl_csv/335982.csv')
