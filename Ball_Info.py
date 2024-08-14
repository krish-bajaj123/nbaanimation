class Ball:
    """A class for keeping info about the balls"""

    def __init__(self, ball):
        self.x = ball[2]
        self.y = ball[3]
        self.radius = ball[4]
        self.color = '#ff8c00'  # Hardcoded orange

    def get_position(self):
        """Return the current position of the ball."""
        return (self.x, self.y)

    def update_position(self, new_x, new_y):
        """Update the position of the ball."""
        self.x = new_x
        self.y = new_y
