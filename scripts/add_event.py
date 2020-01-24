#!/usr/bin/env python3

"""
Quick script to add training schools to data file.

Kilian Lieret 2020
"""

import yaml
from datetime import datetime
from pathlib import Path
from typing import List, Optional, NamedTuple


class Event(NamedTuple):
    name: str
    start_date: str
    end_date: str
    deadline: str
    url: str

    @classmethod
    def input(cls, check=True):
        tmp_event = Event(
            input("Event title "),
            input("Start date [YYYY-MM-DD] "),
            input("End date [YYYY-MM-DD] "),
            input("Deadline [YYYY-MM-DD] "),
            input("Url "),
        )
        if check:
            tmp_event.check()
        return tmp_event

    def check(self):
        start_date = datetime.strptime(self.start_date, "%Y-%m-%d")
        end_date = datetime.strptime(self.end_date, "%Y-%m-%d")
        assert end_date >= start_date
        deadline = self.deadline
        if deadline:
            deadline = datetime.strptime(deadline, "%Y-%m-%d")
            assert deadline <= start_date
        assert self.name


class EventDatabase(object):
    def __init__(self, events: Optional[List[Event]] = None):
        if events is not None:
            self.events = events
        else:
            self.events = []
    
    @classmethod
    def from_file(cls, path: Path):
        with path.open() as stream:
            event_dict = yaml.safe_load(stream)
            if event_dict is None:
                return EventDatabase()
            else:
                return EventDatabase([Event(**dct) for dct in event_dict])

    @staticmethod
    def sort_key(event: Event):
        return event.start_date
    
    def write(self, path: Path):
        with path.open("w") as stream:
            yaml.dump(
                [
                    dict(event._asdict())
                    for event in sorted(self.events, key=self.sort_key)
                ],
                stream
            )
        
    def add_event(self, event: Event):
        self.events.append(event)


if __name__ == "__main__":
    path = Path("__file__").parent.parent / "schools.yml"
    if path.is_file():
        edb = EventDatabase.from_file(path)
    else:
        edb = EventDatabase()
    edb.add_event(Event.input())
    edb.write(path)
