import webbrowser
import argparse


parser = argparse.ArgumentParser(
    "RX7 module",
    add_help = False
    # allow_abbrev=True
)

parser.add_argument(
    "--help","-h",
    action="store_true",
    help="Shows this help message and exit"
)
parser.add_argument(
    "--wiki","--docs",
    action = "store_true",
    help = "Opens official documentation of `rx7` module"
)
parser.add_argument(
    "--colors", "--color", "-c",
    action = "store_true",
    help = "Open a html Page That Contains All Colors and Information About style Class"
)

args = parser.parse_args()

if args.help or (not any([args.wiki,args.colors])):
    print('Available Arguments:')
    print('  [-h, --help]       Open rx7 Documention Page (pypi Page)')
    print('  [--colors]          Open a html Page That Contains All Colors and Information About style Class')
    print('-------')
elif args.wiki:
    webbrowser.open_new_tab(f'./../COLORS.html')
elif args.colors:
    webbrowser.open_new_tab('https://github.com/Ramin-RX7/RX7-Lib')
else:
    ...#print('Wrong command. use "python -m rx7 --help"')
