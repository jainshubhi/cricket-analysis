# Shubhi Jain
# Cricket Analysis
'''
This file describes the Batsman Class.
'''


class Batsman():
    # Class variable describes all the batsmen (by name)
    batsmen = []

    def __init__(self, name, team, order=0, runs=0, balls_faced=0, out=False):
        self.name        = name
        '''
        Format will be [first_name]-[last_name]
        '''
        self.team        = team
        self.order       = order
        self.runs        = runs
        self.balls_faced = balls_faced
        self.out         = out
        if name not in Batsman.batsmen:
            Batsman.batsmen.append(name)

    def strike_rate(self):
        '''
        This function returns the strike rate of the batsman.
        '''
        return (float(runs) / balls_faced) * 100

    def __repr__(self):
        return '(Batsman %s of %s)' % (self.name, self.team)
