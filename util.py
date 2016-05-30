# Shubhi Jain
# Cricket Analysis
'''
This file defines utility functions useful in the analysis of cricket matches.
'''

import pandas as pd, numpy as np
import datetime

from models.match import Match
from models.ball import Ball
from models.ball import Over
from models.bowler import Bowler
from models.batsman import Batsman
from pprint import pprint

# CONSTANTS
BALL_EXTRAS = 0


def row_to_ball(row, match):
    '''
    This helper function defines a ball given a row of data.
    '''
    global BALL_EXTRAS
    innings       = row[1]['1']
    over          = Over(int(row[1]['Unnamed: 2'].split('.')[0]),
                         int(row[1]['Unnamed: 2'].split('.')[1]))
    batting_team  = row[1]['Unnamed: 3']
    batsman       = row[1]['Unnamed: 4']
    non_striker   = row[1]['Unnamed: 5']
    bowler        = row[1]['Unnamed: 6']
    batsman_runs  = int(row[1]['Unnamed: 7'])
    extras        = int(row[1]['Unnamed: 8'])
    if BALL_EXTRAS > 0 and over.first_ball():
        BALL_EXTRAS = 0
    try_count     = 0
    for i in range(BALL_EXTRAS):
        over = over.prev()
        try_count = i
    if extras > 0:
        BALL_EXTRAS += 1
    method_of_out = row[1]['Unnamed: 9']
    out_batsman   = row[1]['Unnamed: 10']
    batsman = Batsman(batsman, batting_team)
    non_striker = Batsman(non_striker, batting_team)
    bowler = Bowler(bowler, '',
                    match.team_1 if match.team_1 != batting_team
                    else match.team_2)
    return Ball(innings, over, batting_team, batsman, non_striker, bowler,
                batsman_runs, extras, try_count, method_of_out, out_batsman)

def data_to_match(filename):
    match_data = pd.read_csv(filename)
    # Get Match Information
    match_info    = match_data[match_data['version'] == 'info']
    team_1        = match_info['Unnamed: 2'].iloc[0]
    team_2        = match_info['Unnamed: 2'].iloc[1]
    gender        = match_info['Unnamed: 2'].iloc[2]
    season        = match_info['Unnamed: 2'].iloc[3]
    date          = match_info['Unnamed: 2'].iloc[4]
    # Format date into datetime date object
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
    # Create the match object
    match = Match(team_1, team_2, season, date, comp, match_num, venue, city,
                  toss_winner, toss_decision, pom, umpire_1, umpire_2, umpire_r,
                  umpire_tv, match_ref, winner)
    # Get ball, batsmen, and bowler info
    balls, batsmen, bowlers = [], [], []
    match_happenings = match_data[match_data['version'] == 'ball']
    for row in match_happenings.iterrows():
        balls.append(row_to_ball(row, match))
    pprint(balls)


data_to_match('data/ipl_csv/335982.csv')
