import os
import shutil
import sys

import css_config

HOME_ = os.path.expanduser('~')


def reset():
    os.remove(css_config.CSS_FILE_)


def install(file):
    os.remove(css_config.CSS_FILE_)
    shutil.copyfile(file, css_config.CSS_FILE_)


def export(file):
    shutil.copyfile(css_config.CSS_FILE_, file)


