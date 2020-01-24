#!/usr/bin/env python3

import yaml
from datetime import datetime
from pathlib import Path
from collections import namedtuple

Event = namedtuple("Event", ["name", "start_date", "end_date", "deadline", "url"])


def input_event():
    return Event(
        input("Event title "),
        input("Start date [YYYY-MM-DD] "),
        input("End date [YYYY-MM-DD] "),
        input("Deadline [YYYY-MM-DD] "),
        input("Url "),
    )


def check_event(event: Event):
    start_date = datetime.strptime(event.start_date, "%Y-%m-%d")
    end_date = datetime.strptime(event.end_date, "%Y-%m-%d")
    assert end_date >= start_date
    deadline = event.deadline
    if deadline:
        deadline = datetime.strptime(deadline, "%Y-%m-%d")
        assert deadline <= start_date
    assert event.name  
    

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
    event = input_event()
    check_event(event)
    edb.add_event(event)
    edb.write(path)

