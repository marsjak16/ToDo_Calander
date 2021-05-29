import Occurrence


class Event(Occurrence):

    def __init__(self, name, date_time, description, tags, location):
        super().__init__(name, date_time, description, tags)
        self.location = location

    def get_location(self) -> str:
        return self.location

    def set_location(self, new_location):
        self.location = new_location
