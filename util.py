# Shubhi Jain
# Cricket Analysis
'''
This file defines utility functions useful in the analysis of cricket matches.
'''

import pandas as pd, numpy as np, yaml, datetime

from models.match import Match
from models.ball import Ball
from models.ball import Over
from models.bowler import Bowler
from models.batsman import Batsman
from pprint import pprint
from collections import OrderedDict

# CONSTANTS
WIDE_EXTRAS = 0


def balls_to_batsmen(balls):
    '''
    This function adds batsman info to a list of balls given a list of balls.
    '''
    BATSMEN = OrderedDict()
    for ball in balls:
        # New batsman in the lineup
        if ball.batsman.name not in BATSMEN.keys():
            # Get order
            ball.batsman.order = len(BATSMEN) + 1
        # Get runs
        ball.batsman = ball.batsman.add_runs(ball.batsman_runs)
        # One more ball faced!
        ball.batsman = ball.batsman.add_balls_faced(1)
        # Store updated batsman in OrderedDict
        BATSMEN[ball.batsman.name] = ball.batsman
        # Update non-striker as well
        if ball.non_striker.name in BATSMEN.keys():
            ball.non_striker = BATSMEN[ball.non_striker.name]
    return balls, BATSMEN

def balls_to_bowlers(balls):
    '''
    This function adds bowler info to a list of balls given a list of balls
    '''
    BOWLERS = OrderedDict()
    for ball in balls:
        # Add ball
        ball.bowler = ball.bowler.add_balls()
        # Add runs if method of extras is bowler's fault
        if ball.method_of_extras == 'wides':
            ball.bowler = ball.bowler.add_runs(extras)
        # Add batsman_runs
        ball.bowler = ball.bowler.add_runs(ball.batsman_runs)
        BOWLERS[ball.bowler.name] = ball.bowler
    return balls, BOWLERS

def data_to_match(filename):
    '''
    Convert YAML T20/ODI data to Match object
    '''
    global WIDE_EXTRAS
    with open(filename, 'r') as stream:
        match_data = yaml.load(stream)
        # Get Match Info
        team_1        = match_data['info']['teams'][0]
        team_2        = match_data['info']['teams'][1]
        gender        = match_data['info']['gender']
        date          = match_data['info']['dates'][0]
        season        = date.year
        comp          = match_data['info']['competition']
        venue         = match_data['info']['venue']
        city          = match_data['info']['city']
        toss_winner   = match_data['info']['toss']['winner']
        toss_decision = match_data['info']['toss']['decision']
        if toss_decision == 'field':
            batting_team, bowling_team = team_1 if team_1 != toss_winner else team_2, toss_winner
        else:
            bowling_team, batting_team = team_1 if team_1 != toss_winner else team_2, toss_winner
        pom           = match_data['info']['player_of_match'][0]
        umpire_1      = match_data['info']['umpires'][0]
        umpire_2      = match_data['info']['umpires'][1]
        winner        = match_data['info']['outcome']['winner']
        balls_1, balls_2 = [], []
        # 1st innings ball information
        for delivery in match_data['innings'][0]['1st innings']['deliveries']:
            for d in delivery.items():
                over         = Over(str(d[0]))
                batsman_runs = d[1]['runs']['batsman']
                batsman      = Batsman(d[1]['batsman'], batting_team)
                bowler       = Bowler(d[1]['bowler'], '', bowling_team)
                extras       = d[1]['runs']['extras']
                if extras > 0:
                    method_of_extras = d[1]['extras'].keys()[0]
                else:
                    method_of_extras = ''
                # Reset the wides
                if over.first_ball():
                    WIDE_EXTRAS = 0
                # Repeat ball due to wides
                for i in range(WIDE_EXTRAS):
                    over = over.prev()
                if extras > 0 and method_of_extras == 'wides':
                    WIDE_EXTRAS += 1
                non_striker = Batsman(d[1]['non_striker'], batting_team)
                # If a wicket took place
                if 'wicket' in d[1].keys():
                    method_of_out = d[1]['wicket']['kind']
                    out_batsman   = d[1]['wicket']['player_out']
                    # Add wicket in bowler's wicket column
                    if method_of_out != 'run out':
                        bowler = bowler.add_wicket()
                else:
                    method_of_out = None
                    out_batsman   = None
                balls_1.append(Ball(1, over, batting_team, batsman, non_striker,
                                  bowler, batsman_runs, extras,
                                  method_of_extras, 0, method_of_out,
                                  out_batsman))
        # 2nd innings ball information
        for delivery in match_data['innings'][1]['2nd innings']['deliveries']:
            for d in delivery.items():
                over         = Over(str(d[0]))
                batsman_runs = d[1]['runs']['batsman']
                batsman      = Batsman(d[1]['batsman'], bowling_team)
                bowler       = Bowler(d[1]['bowler'], '', batting_team)
                extras       = d[1]['runs']['extras']
                if extras > 0:
                    method_of_extras = d[1]['extras'].keys()[0]
                else:
                    method_of_extras = ''
                # Reset the wides
                if over.first_ball():
                    WIDE_EXTRAS = 0
                # Repeat ball due to wides
                for i in range(WIDE_EXTRAS):
                    over = over.prev()
                if extras > 0 and method_of_extras == 'wides':
                    WIDE_EXTRAS += 1
                non_striker = Batsman(d[1]['non_striker'], batting_team)
                # If a wicket took place
                if 'wicket' in d[1].keys():
                    method_of_out = d[1]['wicket']['kind']
                    out_batsman   = d[1]['wicket']['player_out']
                    # Add wicket in bowler's wicket column
                    if method_of_out != 'run out':
                        bowler = bowler.add_wicket()
                else:
                    method_of_out = None
                    out_batsman   = None
                balls_2.append(Ball(1, over, batting_team, batsman, non_striker,
                                  bowler, batsman_runs, extras,
                                  method_of_extras, 0, method_of_out,
                                  out_batsman))
        balls_1, batsmen_1 = balls_to_batsmen(balls_1)
        balls_2, batsmen_2 = balls_to_batsmen(balls_2)
        balls_1, bowlers_1 = balls_to_bowlers(balls_1)
        balls_2, bowlers_2 = balls_to_bowlers(balls_2)
        return Match(team_1, team_2, season, date, comp, venue, city,
                     toss_winner, toss_decision, pom, umpire_1, umpire_2,
                     winner, balls={batting_team:balls_1, bowling_team:balls_2},
                     batsmen={batting_team:batsmen_1, bowling_team:batsmen_2},
                     bowlers={batting_team:bowlers_2, bowling_team:bowlers_1})
