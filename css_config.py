import os
from properties import properties

HOME_ = os.path.expanduser('~')
CSS_FILE_ = f"{HOME_}/.config/gtk-4.0/gtk.css"


def get_file_data():
    with open(CSS_FILE_, "r") as file:
        return file.readlines()


def write(data):
    with open(CSS_FILE_, "r") as file:
        file.writelines(data)


def modify(prop, value):
    lines = get_file_data()
    changed = False
    new_lines = []

    for line in lines:
        if line.startswith(f"@define-color {prop}"):
            line = f"@define-color {prop} {value}"
            changed = True

        new_lines.append(line)
    if not changed:
        new_lines.append(f"@define-color {prop} {value}")

    write(new_lines)


def restore(prop, value):
    lines = get_file_data()
    new_lines = []

    for line in lines:
        if not line.startswith(f"@define-color {prop}"):
            new_lines.append(line)
    write(new_lines)
