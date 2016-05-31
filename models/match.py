# Shubhi Jain
# Cricket Analysis
'''
This file describes the Match Class
'''

class Match():

    def __init__(self, team_1, team_2, season, date, comp, venue,
                 city, toss_winner, toss_decision, pom, umpire_1, umpire_2,
                 winner, gender='male', balls=[], match_type='ipl'):
        self.team_1        = team_1
        self.team_2        = team_2
        self.gender        = gender
        self.season        = season
        self.date          = date
        self.comp          = comp
        self.venue         = venue
        self.city          = city
        self.toss_winner   = toss_winner
        self.toss_decision = toss_decision
        self.pom           = pom
        self.umpire_1      = umpire_1
        self.umpire_2      = umpire_2
        self.winner        = winner
        # List of balls played throughought match
        self.balls         = balls
        self.match_type    = match_type
        '''
        The match types are:
        - ipl
        - t20i
        - odi
        - test
        '''

    def __repr__(self):
        return "%s played %s at %s on %s and %s won!" % (self.team_1,
            self.team_2, self.venue, str(self.date), self.winner)
