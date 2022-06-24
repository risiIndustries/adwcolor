import os
import shutil
from properties import properties

HOME_ = os.path.expanduser('~')
CSS_FILE_ = f"{HOME_}/.config/gtk-4.0/gtk.css"


def check_properties(prop):
    if prop not in properties:
        print("Invalid property.\nPlease run \"adwcolor listproperties\" to list currently existing properties.")
        exit(1)


def list_properties():
    for prop in properties:
        print(prop)


def get_file_data():
    with open(CSS_FILE_, "r") as file:
        return file.readlines()


def write(data):
    with open(CSS_FILE_, "w") as file:
        file.writelines(data)


def modify(prop, value):
    lines = get_file_data()
    changed = False
    new_lines = []

    for line in lines:
        if line.startswith(f"@define-color {prop} "):
            line = f"@define-color {prop} {value};\n"
            changed = True

        new_lines.append(line)
    if not changed:
        new_lines.append(f"@define-color {prop} {value};\n")

    write(new_lines)


def restore(prop):
    lines = get_file_data()
    new_lines = []

    for line in lines:
        if not line.startswith(f"@define-color {prop}"):
            new_lines.append(line)
    write(new_lines)


def reset():
    if os.path.exists(CSS_FILE_):
        os.remove(CSS_FILE_)


def install(file):
    reset()
    shutil.copyfile(file, CSS_FILE_)


def export(file):
    shutil.copyfile(CSS_FILE_, file)
