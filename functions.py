import os
import shutil
from adwcolor.properties import properties

HOME_ = os.path.expanduser('~')
CSS_FILE_ = f"{HOME_}/.config/gtk-4.0/gtk.css"
CSS_FILE_3_ = f"{HOME_}/.config/gtk-3.0/gtk.css"


# Creates the environment for theming if it doesn't exist
def create_environment():
    # Create CSS directories if they don't exist
    if not os.path.exists(f"{HOME_}/.config/gtk-4.0"):
        os.makedirs(f"{HOME_}/.config/gtk-4.0")
    if not os.path.exists(f"{HOME_}/.config/gtk-3.0"):
        os.makedirs(f"{HOME_}/.config/gtk-3.0")

    # Create CSS file if it doesn't exist
    if not os.path.exists(CSS_FILE_):  # Create Gtk4 config file
        open(CSS_FILE_, 'w+')
    if not os.path.exists(CSS_FILE_3_):  # Symlink gtk4 config file to gtk3
        os.symlink(CSS_FILE_, CSS_FILE_3_)


create_environment()


def get_value(prop):
    lines = get_file_data()

    for line in lines:
        if line.startswith(f"@define-color {prop}"):
            return line.replace(f"@define-color {prop} ", "").replace(";\n", "")
    return None


def list_properties():
    for prop in properties:
        print(prop)


def get_file_data():
    create_environment()
    with open(CSS_FILE_, "r") as file:
        return file.readlines()


def write(data):
    with open(CSS_FILE_, "w+") as file:
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


# Deprecated function
def restore(prop):
    default(prop)


def default(prop):
    lines = get_file_data()
    new_lines = []

    for line in lines:
        if not line.startswith(f"@define-color {prop}"):
            new_lines.append(line)
    write(new_lines)


def reset():
    if os.path.exists(CSS_FILE_):
        os.remove(CSS_FILE_)
    if os.path.exists(CSS_FILE_3_):
        os.remove(CSS_FILE_3_)
    create_environment()


def install(file):
    reset()
    shutil.copyfile(file, CSS_FILE_)


def export(file):
    shutil.copyfile(CSS_FILE_, file)
