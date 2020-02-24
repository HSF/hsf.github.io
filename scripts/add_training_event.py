#!/usr/bin/env python3

"""
Quick script to add training schools to data file.

Kilian Lieret 2020
"""

import yaml
import datetime
from pathlib import Path
from typing import List, Optional, Union


class Event(object):
    def __init__(
        self,
        title: str,
        date: Union[str, datetime.date],
        end_date: Union[str, datetime.date],
        source: str, author: str,
        deadline: Union[str, datetime.date] = ""
    ):
        self.title = title
        self.date = self._interpret_date(date)
        self.end_date = self._interpret_date(end_date)
        self.deadline = self._interpret_date(deadline, empty_ok=True)
        self.source = source
        self.author = author

        if not self.end_date >= self.date:
            raise ValueError(
                f"End date {self.end_date} is BEFORE the date {self.date} for "
                f"training event '{self.title}'."
            )
        if self.deadline:
            if not self.deadline <= self.date:
                raise ValueError(
                    f"Deadline {self.deadline} is after start date {self.date}"
                    f" for training evnet '{self.title}'."
                )
        assert self.title

    @staticmethod
    def _interpret_date(date: Union[datetime.date, str], empty_ok=False):
        if not date and empty_ok:
            return date
        elif isinstance(date, datetime.date):
            return date
        else:
            return datetime.datetime.strptime(date, "%Y-%m-%d").date()

    @classmethod
    def input(cls):
        tmp_event = Event(
            title=input("Event title ").strip(),
            date=input("Start date [YYYY-MM-DD] ").strip(),
            end_date=input("End date [YYYY-MM-DD] ").strip(),
            deadline=input("Deadline [YYYY-MM-DD or ''] ").strip(),
            source=input("Url ").strip(),
            author=input("Author ").strip(),
        )
        return tmp_event

    def to_dict(self):
        return self.__dict__


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
        return event.date
    
    def write(self, path: Path):
        with path.open("w") as stream:
            yaml.dump(
                [
                    event.to_dict()
                    for event in sorted(self.events, key=self.sort_key)
                ],
                stream,
                default_flow_style=False
            )
        
    def add_event(self, event: Event):
        self.events.append(event)


if __name__ == "__main__":
    path = Path(__file__).resolve().parent.parent / "_data" / "training-schools.yml"
    if path.is_file():
        edb = EventDatabase.from_file(path)
        print(f"Loaded {len(edb.events)} events from database.")
    else:
        print(f"Did not find database at {path}. Initializing empty one.")
        edb = EventDatabase()
    edb.add_event(Event.input())
    edb.write(path)
    print("Added event to database. Please commit and submit a PR to add it to the"
          " webpage.")
