#!/usr/bin/env python3

import yaml
from datetime import datetime
from pathlib import Path
import typing


class Event(typing.NamedTuple):
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
    def __init__(self, events=None):
        if events is not None:
            self.events = events
        else:
            self.events = []
    
    @classmethod
    def from_file(cls, path: Path):
        with path.open() as stream:
            events = yaml.safe_load(stream)
        return EventDatabase(events)
    
    def write(self, path: Path):
        with path.open("w") as stream:
            yaml.dump(self.events, stream)
        
    def add_event(self, event: Event):
        self.events.append(dict(event._asdict()))


if __name__ == "__main__":
    path = Path("__file__").parent.parent / "schools.yml"
    if path.is_file():
        edb = EventDatabase.from_file(path)
    else:
        edb = EventDatabase()
    edb.add_event(Event.input())
    edb.write(path)

