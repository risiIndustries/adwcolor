#!/usr/bin/env python3.10

import sys

import adwcolor.functions


def help_prompt():
    print("""adwcolor: Quickly and easily customize Libadwaita's look

Basic Management
  adwcolor reset                                Restore default Libadwaita theme.
  adwcolor install <path/libadwaita_theme.css>  Replaces ~/.config/gtk-4.0/gtk.css with Libadwaita css file.
  adwcolor export <path/libadwaita_theme.css>   Export Libadwaita css file (creates clone of ~/.config/gtk-4.0/gtk.css)

Modifying Current Theme
  adwcolor listproperties                       Lists available properties to modify.
  adwcolor modify <property> <value>            Set property to css color. (ex: "adwcolor modify accent_color @green_4")
  adwcolor default <property>                   Restore modified property to default. (ex: "adwcolor restore accent_color)
    """)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help_prompt()
        exit(1)


    def check_arguments(arg):
        if not len(sys.argv) - 1 == arg:
            help_prompt()
            exit(1)


    match sys.argv[1]:
        case "reset":
            check_arguments(1)
            adwcolor.functions.reset()
            print("Libadwaita theme reset.")
        case "install":
            check_arguments(2)
            adwcolor.functions.install(sys.argv[2])
            print("Installation successful.")
        case "export":
            check_arguments(2)
            adwcolor.functions.export(sys.argv[2])
            print(f"Exported to {sys.argv[2]}.")
        case "modify":
            check_arguments(3)
            adwcolor.functions.check_properties(sys.argv[2])
            adwcolor.functions.modify(sys.argv[2], sys.argv[3])
            print(f"{sys.argv[2]} set to {sys.argv[3]}.")
        case "default":
            check_arguments(2)
            adwcolor.functions.check_properties(sys.argv[2])
            adwcolor.functions.restore(sys.argv[2])
            print(f"{sys.argv[2]} restored to default.")
        case "listproperties":
            adwcolor.functions.list_properties()
        case default:
            help_prompt()
