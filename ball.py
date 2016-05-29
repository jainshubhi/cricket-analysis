# Shubhi Jain
# Cricket Analysis
'''
This file describes the Ball Class.
'''


class Ball:

    def __init__(self, innings, over, batting_team, batsman, non_striker, bowler
                 batsman_runs, extras, try_count, method_of_out, out_batsman,
                 ball_length, ball_width, ball_type, ball_pace):
        self.innings       = innings
        self.over          = over
        self.batting_team  = batting_team
        self.batsman       = batsman
        self.non_striker   = non_striker
        self.bowler        = bowler
        self.batsman_runs  = batsman_runs
        self.extras        = extras
        self.try_count     = try_count
        self.method_of_out = method_of_out
        '''
        The four methods to get out:
        - caught
        - bowled
        - stumping
        - run_out
        '''
        self.out_batsman   = out_batsman
        self.ball_length   = ball_length
        '''
        The five kinds of ball lengths:
        - short
        - back_of_length
        - full
        - yorker
        - full_toss
        '''
        self.ball_width    = ball_width
        '''
        The six kinds of ball widths:
        - wide
        - leg_stump
        - mid_stump
        - off_stump
        - off_off_stump
        - leg_side
        '''
        self.ball_type     = ball_type
        '''
        The ten kinds of ball types:
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
        self.ball_pace     = ball_pace
