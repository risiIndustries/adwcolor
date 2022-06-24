import sys

import functions


def help_prompt():
    print("""adwcolor: Quickly and easily customize Libadwaita's look

Basic Management
  adwcolor reset                                Restore default Libadwaita theme.
  adwcolor install <path/libadwaita_theme.css>  Replaces ~/.config/gtk-4.0/gtk.css with Libadwaita css file.
  adwcolor export <path/libadwaita_theme.css>   Export Libadwaita css file (creates clone of ~/.config/gtk-4.0/gtk.css)

Modifying Current Theme
  adwcolor listproperties                       Lists available properties to modify.
  adwcolor modify <property> <value>            Set property to css color. (ex: "adwcolor modify accent_color @green_4")
  adwcolor restore <property>                   Restore modified property to default. (ex: "adwcolor restore accent_color)
    """)


if len(sys.argv) < 2:
    help_prompt()
    exit(1)


def check_arguments(arg):
    if not len(sys.argv) - 1 == arg:
        help_prompt()
        exit(1)


match sys.argv[1]:
    case "reset":
        functions.reset()
    case "install":
        check_arguments(2)
        functions.install(sys.argv[2])
    case "export":
        check_arguments(2)
        functions.export(sys.argv[2])
    case "modify":
        check_arguments(3)
        functions.check_properties(sys.argv[2])
        functions.modify(sys.argv[2], sys.argv[3])
    case "restore":
        check_arguments(2)
        functions.check_properties(sys.argv[2])
        functions.restore(sys.argv[2])
    case "listproperties":
        functions.list_properties()
    case default:
        help_prompt()
