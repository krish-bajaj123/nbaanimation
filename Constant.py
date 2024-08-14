class Constant:
    """A class for handling constants"""

    NORMALIZATION_COEF = 7
    PLAYER_CIRCLE_SIZE = 12 / NORMALIZATION_COEF
    INTERVAL = 10
    DIFF = 6

    # Court dimensions
    X_MIN = 0
    X_MAX = 100
    Y_MIN = 0
    Y_MAX = 50

    COL_WIDTH = 0.3
    SCALE = 1.65
    FONTSIZE = 6

    # Center coordinates
    X_CENTER = X_MAX / 2 - DIFF / 1.5 + 0.10
    Y_CENTER = Y_MAX - DIFF / 1.5 - 0.35

    MESSAGE = 'You can rerun the script and choose any event from 0 to '

    @classmethod
    def get_court_dimensions(cls):
        return (cls.X_MIN, cls.X_MAX, cls.Y_MIN, cls.Y_MAX)

    @classmethod
    def get_center_coordinates(cls):
        return (cls.X_CENTER, cls.Y_CENTER)
