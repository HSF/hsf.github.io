#!/usr/bin/env python3

# std
from pathlib import Path
import oyaml as yaml  # keep order
from typing import List

this_directory = Path(__file__).resolve().parent
profile_directory = this_directory.parent / "_educators"


def get_content_header(lines: List[str]):
    """ Get header of Jekyll file """
    header_lines = []
    content_lines = []
    is_content = False
    for i_line, line in enumerate(lines):
        line = line.strip()
        if i_line == 0:
            assert line == "---"
            continue
        if line == "---":
            is_content = True
            continue
        if is_content:
            content_lines.append(line)
        else:
            header_lines.append(line)
    header = "\n".join(header_lines)
    content = "\n".join(content_lines)
    return content, yaml.safe_load(header)


def read_transform_write(path: Path, header_transform_fct):
    with Path(path).open("r") as file:
        content, header = get_content_header(file.readlines())
        header = header_transform_fct(header)
    new_file_content = "---\n"
    new_file_content += yaml.dump(header)
    new_file_content += "---\n"
    new_file_content += content
    with Path(path).open("w") as file:
        file.write(new_file_content)


def main():
    for file in profile_directory.iterdir():
        read_transform_write(file, lambda x: x)


if __name__ == "__main__":
    main()