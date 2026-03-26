"""
Demo: print a filesystem tree using Rich Tree renderable.

Based on original Rich Tree example: 
    https://github.com/Textualize/rich/blob/master/rich/tree.py
    
Plus fix for directories with a lack of access permissions:
    - Show "[ACCESS DENIED]" instead of unhandled exception.
"""

import os
import pathlib
import sys

from rich import print
from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree
from rich.panel import Panel

def walk_directory(directory: pathlib.Path, tree: Tree) -> None:
    """Recursively build a Tree with directory contents."""

    if directory.is_dir():
        # Abort if dir is not readable
        if not os.access(directory, os.X_OK):
            error_panel = Panel(f"Provided directory is not readable: {directory}", title="[ACCESS DENIED]")
            print(error_panel)
            return

    # Sort dirs first then by filename
    paths = sorted(
        pathlib.Path(directory).iterdir(),
        key=lambda path: (path.is_file(), path.name.lower()),
    )

    for path in paths:
        # Skip hidden files
        if path.name.startswith("."):
            continue

        if path.is_dir():
            # Skip dir if not readable
            if not os.access(path, os.X_OK):
                tree.add( Text(path.name, "white") + Text(" [ACCESS DENIED]", "red"))
                continue

            style = "dim" if path.name.startswith("__") else ""
            branch = tree.add(
                f"[magenta]:open_file_folder: [link file://{path}]{escape(path.name)}",
                style=style,
                guide_style=style,
            )
            walk_directory(path, branch)
        else:
            text_filename = Text(path.name, "green")
            text_filename.highlight_regex(r"\..*$", "bold red")
            text_filename.stylize(f"link file://{path}")
            file_size = path.stat().st_size
            text_filename.append(f" ({decimal(file_size)})", "blue")
            # Mark executables
            icon = "*" if os.access(path, os.X_OK) else " "
            tree.add(Text(icon) + text_filename)

def main():
    try:
        directory = os.path.abspath(sys.argv[1])
    except IndexError:
        print("[b]Usage:[/] python tree.py <DIRECTORY>")
    else:
        tree = Tree(
            f":open_file_folder: [link file://{directory}]{directory}",
            guide_style="bright_blue",
        )
        walk_directory(pathlib.Path(directory), tree)
        print(tree)

if __name__ == "__main__":
    main()
