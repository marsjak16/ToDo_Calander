import datetime
from packages.backend.classes import Occurrence


class Task(Occurrence):

    def __init__(self, name, date_time, description, tags, importance, reminder_date):
        super().__init__(name, date_time, description, tags)
        self.importance = importance
        self.reminder_date = reminder_date

    def get_importance(self) -> int:
        return self.importance

    def get_reminder_date(self) -> datetime.datetime:
        return self.reminder_date

    def set_importance(self, new_importance):
        self.importance = new_importance

    def set_reminder_date(self, new_reminder_date):
        self.reminder_date = new_reminder_date
