import pandas as pd
from Event import Event
from Team import Team
from Constant import Constant

class Game:
    """A class for keeping info about the games"""

    def __init__(self, path_to_json, event_index):
        self.home_team = None
        self.guest_team = None
        self.event = None
        self.path_to_json = path_to_json
        self.event_index = event_index

    def read_json(self):
        try:
            data_frame = pd.read_json(self.path_to_json)
            last_default_index = len(data_frame) - 1
            self.event_index = min(self.event_index, last_default_index)
            index = self.event_index
            print(Constant.MESSAGE + str(last_default_index))
            event = data_frame['events'][index]
            self.event = Event(event)
            self.home_team = Team(event['home']['teamid'])
            self.guest_team = Team(event['visitor']['teamid'])
        except Exception as e:
            print(f"Error reading JSON: {e}")

    def start(self):
        if self.event:
            self.event.show()
        else:
            print("No event loaded. Please read the JSON file first.")
