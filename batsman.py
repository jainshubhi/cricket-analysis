# Shubhi Jain
# Cricket Analysis
'''
This file describes the Batsman Class.
'''


class Batsman():
    # Class variable keeping track of all batsmen
    batsmen = []

    def __init__(self, name, team, order, runs, balls_faced):
        self.name        = name
        '''
        Format will be [first_name]-[last_name]
        '''
        self.team        = team
        self.order       = order
        self.runs        = runs
        self.balls_faced = balls_faced
        if name not in batsmen:
            Batsman.batsmen.append(name)

    def strike_rate(self):
        '''
        This function returns the strike rate of the batsman.
        '''
        return (float(runs) / balls_faced) * 100
