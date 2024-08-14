from Team import Team

class Player:
    """A class for keeping info about the players"""
    def __init__(self, player_data):
        self.team = Team(player_data[0])
        self.id = player_data[1]
        self.x = player_data[2]
        self.y = player_data[3]
        self.color = self.team.color

    def get_position(self):
        return (self.x, self.y)

    def update_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
