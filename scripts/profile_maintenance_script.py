#!/usr/bin/env python3

"""
Script to maintain (i.e. bulk edit) profiles of educators/conveners/etc.

Kilian Lieret 2020
"""

# std
from pathlib import Path
import oyaml as yaml  # same as normal yaml, only it keeps order of keys
from typing import List, Callable, Tuple, Dict, Any

this_directory = Path(__file__).resolve().parent
profile_directory = this_directory.parent / "_educators"


def get_content_header(lines: List[str]) -> Tuple[str, Dict[str, Any]]:
    """ Get header of Jekyll file

    Args:
        lines: Lines of profile

    Returns:
        content (everything below header as a string),
        header (parsed yaml, i.e. as dictionary structure)
    """
    header_lines = []
    content_lines = []
    is_content = False
    for i_line, line in enumerate(lines):
        line = line.strip()
        if i_line == 0:
            assert line == "---", lines
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


def read_transform_write(
    path: Path, header_transform_fct: Callable[[Dict[str, Any]], Dict[str, Any]]
) -> None:
    """ Opens profile, reads it, transforms the header, writes back

    Args:
        path: Path to open
        header_transform_fct: Function that takes parsed yaml and returns a new
            nested data structure that should be written back

    Returns:
        None
    """
    with Path(path).open("r") as file:
        content, header = get_content_header(file.readlines())
        header = header_transform_fct(header)
    new_file_content = "---\n"
    new_file_content += yaml.dump(header)
    new_file_content += "---\n"
    new_file_content += content
    with Path(path).open("w") as file:
        file.write(new_file_content)


def change_key(self, old, new):
    """ Change key in ordered dictionary """
    return {new if key == old else key: value for key, value in self.items()}

# ------------------------------------------------------------------------------
# Transformation functions
# ------------------------------------------------------------------------------

def linked_in_handle_instead_url(header: Dict[str, Any]) -> Dict[str, Any]:
    """ Use linkedin handles rather than full URL
    """
    linkedin = header.get("linkedin")
    if linkedin is None:
        return header
    if linkedin.endswith("/"):
        linkedin = linkedin[:-1]
    handle = linkedin.split("/")[-1]
    assert handle, (linkedin, handle)
    linkedin = handle
    header["linkedin"] = linkedin
    return header


def rename_training_only_keys(header: Dict[str, Any]) -> Dict[str, Any]:
    """ Rename some keys to generalize profiles """

    header = change_key(header, "years", "training_years")
    header = change_key(header, "roles", "training_roles")
    return header

    # years = header.pop("years", None)
    # if years is not None:
    #     header["training-active-years"] = years
    # roles = header.pop("roles", None)
    # if roles is not None:
    #     header["training-roles"] = roles
    # return header


# ------------------------------------------------------------------------------


def main():
    """ Loop over all profiles and apply read_transform_write.

    MAKE SURE YOU SET THE RIGHT TRANSFORMATION FUNCTION HERE!

    Returns:
        None
    """
    for file in profile_directory.iterdir():
        if "readme" in file.name.lower():
            continue
        read_transform_write(file, rename_training_only_keys)


if __name__ == "__main__":
    main()
