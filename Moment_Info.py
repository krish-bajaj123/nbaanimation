from Ball_Info import Ball
from Player_Info import Player

class Moment:
    """A class for keeping info about the moments"""
    def __init__(self, moment):
        self.quarter = moment[0]
        self.game_clock = moment[2]
        self.shot_clock = moment[3]
        self.ball = Ball(moment[5][0])
        self.players = [Player(player) for player in moment[5][1:]]

    def get_ball(self):
        return self.ball

    def get_players(self):
        return self.players
