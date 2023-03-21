#!/usr/bin/env python3

"""Generates md redirect files from _redirects.csv"""

import csv
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

def create_redirect(source: str, dest: str) -> None:
    (SCRIPT_DIR / (source + ".md")).write_text( "\n".join([
        "---",
        f"redirect_to: {dest}",
        "---",
        "<!-- THIS FILE WAS AUTOMATICALLY GENERATED. ",
        "PLEASE CHANGE _redirects.csv AND THEN RUN _redirection_generator.py -->"
    ]))


if __name__ == "__main__":
    with (SCRIPT_DIR / "_redirects.csv").open() as infile:
        csv_reader = csv.reader(infile)
        for row in csv_reader:
            source, dest = row
            create_redirect(source, dest)