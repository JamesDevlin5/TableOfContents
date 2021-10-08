#!/usr/bin/env python3
"""Generates a Table of Contents for some target markdown document."""

import argparse
import sys
from pathlib import Path


class Header:
    """A single header line, prefixed by one or more `#` symbols."""

    def __init__(self, level, line):
        self._level = level
        self._line = line
        self._children = []
        self.parent = None

    @classmethod
    def from_line(cls, line):
        """Constructs a header object from a single provided line of a document."""
        level, content = line.split(" ", 1)
        return cls(len(level), content)

    @property
    def level(self):
        """The level number of this header (number of preceding `#`'s)."""
        return self._level

    @property
    def line(self):
        """The contents of this line; the string representation of this header."""
        return self._line

    @property
    def parent(self):
        """Getter for the parent node. This node will inhabit the child list."""
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node

    def add_child(self, child):
        """Appends a child header to this parent header."""
        self._children.append(child)
        child.parent = self


def open_file(target):
    """
    Validates that the target file is a markdown document, then returns an opened file object.

    Args:
        target  str: The path to a file.

    Returns:
        An opened file object corresponding to the provided markdown document.
    """
    path = Path(target)
    # Ensure markdown document
    if path.suffix != ".md":
        print("Cannot parse a non-markdown document!")
        sys.exit(1)
    # Ensure file exists
    if not path.exists():
        print("Document does not exist!")
        sys.exit(1)
    # Open the file
    return path.open()


def make_arg_parser():
    """
    Creates an argument parser.

    Defines an argument processor that accepts a single target, a markdown document.
    The parser must be consumed via a call to `parse_args()`.

    Returns:
        An argument parser accepting a single file path.
    """
    parser = argparse.ArgumentParser(
        description="Generate a table of contents for the target markdown document."
    )
    parser.add_argument(
        "file",
        metavar="FILE",
        type=open_file,
        help="The markdown document to scan for a TOC",
    )
    return parser


def read_lines(lines):
    """
    Reads a series of Header objects from a file's lines.

    All non-header lines will be filtered out.

    Arguments:
        lines   file-object: The opened file which yields lines from the markdown document.
    """
    doc = []
    for raw_line in lines:
        line = raw_line.strip()
        if line.startswith("#"):
            header = Header.from_line(line)
            doc.append(header)
    return doc


def main():
    """The main program runner."""
    args = make_arg_parser().parse_args()
    lines = read_lines(args.file)
    for header in lines:
        spaces = "".join(" " for _ in range(header.level * 2))
        print(f"{spaces}- {header.line}")


if __name__ == "__main__":
    main()
