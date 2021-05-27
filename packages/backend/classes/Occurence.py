import datetime


class Occurrence:

    def __init__(self, name, date_time, description, tags):
        self.name = name
        self.date_time = date_time
        self.description = description
        self.tags = tags

    def get_name(self) -> str:
        return self.name

    def get_date_time(self) -> datetime.datetime:
        return self.date_time

    def get_description(self) -> str:
        return self.description

    def get_tags(self) -> list:
        return self.tags

    def set_name(self, new_name):
        self.name = new_name

    def set_date_time(self, new_date_time):
        self.date_time = new_date_time

    def set_description(self, new_description):
        self.description = new_description

    def add_to_description(self, additional_description):
        self.description += additional_description

    def add_tag(self, new_tag):
        self.tags.append(new_tag)

    def remove_tag(self, tag):
        self.tags.remove(tag)
