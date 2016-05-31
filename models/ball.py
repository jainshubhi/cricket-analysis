# Shubhi Jain
# Cricket Analysis
'''
This file describes the Ball Class.
'''

from math import floor
from decimal import Decimal


class Ball:

    def __init__(self, innings, over, batting_team, batsman, non_striker,
                 bowler, batsman_runs, extras, method_of_out,
                 out_batsman, ball_length='', ball_width='', ball_type='',
                 ball_pace=0, method_of_extras=''):
        self.innings          = innings
        self.over             = over
        self.batting_team     = batting_team
        self.batsman          = batsman
        self.non_striker      = non_striker
        self.bowler           = bowler
        self.batsman_runs     = batsman_runs
        self.extras           = extras
        self.method_of_extras = method_of_extras
        '''
        The methods of extras:
        - wides
        - legbyes
        - byes
        - no_ball
        - penalty_runs
        '''
        self.method_of_out    = method_of_out
        '''
        The methods to get out:
        - caught
        - bowled
        - stumping
        - lbw
        - run_out
        - hit_wicket
        - hit_twice
        - field_obstruction
        - hand_ball
        - retire_out
        - time_out
        '''
        self.out_batsman      = out_batsman
        self.ball_length      = ball_length
        '''
        The kinds of ball lengths:
        - short
        - back_of_length
        - full
        - yorker
        - full_toss
        '''
        self.ball_width       = ball_width
        '''
        The kinds of ball widths:
        - wide
        - leg_stump
        - mid_stump
        - off_stump
        - off_off_stump
        - leg_side
        '''
        self.ball_type        = ball_type
        '''
        The kinds of ball types:
        - leg_cutter
        - off_cutter
        - in_swing
        - out_swing
        - googly
        - doosra
        - carrom
        - off_spin
        - leg_spin
        - straight
        '''
        # Ball pace in km/hr
        self.ball_pace        = ball_pace

    def __repr__(self):
        return 'Ball (%s to %s in the %s over. %d runs.)' % (self.bowler,
            self.batsman, self.over, self.extras + self.batsman_runs)

class Over:

    def __init__(self, number):
        self.overall_over = int(number.split('.')[0])
        self.ball         = int(number.split('.')[1])

    def next(self):
        '''
        This function defines how an over is defined for the next ball.
        '''
        if self.ball <= 5:
            self.ball += 1
        else:
            self.overall_over += 1
            self.ball = 1
        return self

    def prev(self):
        '''
        This function defines how an over is defined for the previous ball.
        '''
        if self.ball > 1:
            self.ball -= 1
        else:
            self.overall_over -= 1
            self.ball = 6
        return self

    def first_ball(self):
        return self.ball == 1

    def __repr__(self):
        return '%d.%d' % (self.overall_over, self.ball)
