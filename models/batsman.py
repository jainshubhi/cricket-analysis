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
        return (float(self.runs) / self.balls_faced) * 100

    def add_runs(self, runs):
        self.runs += runs
        return self

    def add_balls_faced(self, balls_faced):
        self.balls_faced += balls_faced
        return self

    def __repr__(self):
        return '(Batsman %s of %s has a strike rate of %f.)' % (self.name,
                self.team, self.strike_rate())
