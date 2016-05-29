# Shubhi Jain
# Cricket Analysis
'''
This file describes the Bowler Class.
'''


class Bowler():
    # Class variable describes all the bowlers (by name)
    bowlers = []

    def __init__(self, name, bowler_type, team, runs, balls, wickets):
        self.name        = name
        self.bowler_type = bowler_type
        self.team        = team
        self.runs        = runs
        self.balls       = balls
        self.wickets     = wickets
        if name not in bowlers:
            bowlers.append(name)

    def economy(self):
        '''
        This function returns the economy of the bowler.
        '''
        return runs / (float(balls) / 6)

    def average(self):
        '''
        This function returns the average of the bowler.
        '''
        return 0
