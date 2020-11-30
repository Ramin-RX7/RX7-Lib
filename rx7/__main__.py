import sys

args = sys.argv
length = len(args)

def wrong():
    print('Available Arguments:')
    print('  [-h, --help, help]       Open rx7 Documention Page (pypi Page)')
    print('  [color, colors]          Open a html Page That Contains All Colors and Information About style Class')
    print('                             (Works  Offline & Online)')
    print('-------')
    print('More Features Will be Added Soon...')

if length != 2:   #not length  or
    wrong()
elif args[1] in ('color','colors'): 
    import webbrowser
    webbrowser.open_new_tab(f'{str(__file__)[:-11]}COLORS.html')
elif args[1] in ('-h','--help','help'):
    import webbrowser
    webbrowser.open_new_tab(f'https://pypi.org/project/rx7')
else:
    wrong()
