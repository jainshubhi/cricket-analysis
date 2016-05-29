# Shubhi Jain
# Cricket Analysis
'''
This file describes the Match Class
'''

class Match():

    def __init__(self, team_1, team_2, gender='male', season, date, comp,
                 match_num, venue, city, toss_winner, toss_decision,
                 pom, umpire_1, umpire_2, umpire_r, umpire_tv,
                 match_ref, winner, balls=[], batsmen=[], match_type):
        self.team_1        = team_1
        self.team_2        = team_2
        self.gender        = gender
        self.season        = season
        self.date          = date
        self.comp          = comp
        self.match_num     = match_num
        self.venue         = venue
        self.city          = city
        self.toss_winner   = toss_winner
        self.toss_decision = toss_decision
        self.pom           = pom
        self.umpire_1      = umpire_1
        self.umpire_2      = umpire_2
        self.umpire_3      = umpire_3
        self.umpire_r      = umpire_r
        self.umpire_tv     = umpire_tv
        self.match_ref     = match_ref
        self.winner        = winner
        # List of balls played throughought match
        self.balls         = balls
        # List of batsmen played throughout match
        self.batsmen       = batsmen
        self.match_type    = match_type
        '''
        The match types are:
        - ipl
        - t20i
        - odi
        - test
        '''
