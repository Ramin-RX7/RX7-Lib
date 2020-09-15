import sys
if sys.argv[1] in ('color','colors'): 
    import webbrowser
    webbrowser.open_new_tab(f'{str(__file__)[:-11]}COLORS.html')
if sys.argv[1] in ('-h','--help','help'):
    import webbrowser
    webbrowser.open_new_tab(f'https://pypi.org/project/rx7')
if len(sys.argv)<2:
    print('Available Arguments:')
    print('  [-h, --help, help]       Open rx7 Documention Page (pypi Page)')
    print('  [color, colors]          Open a html Page That Contains All Colors and Information About style Class')
    print('                             (Works  Offline & Online)')
    print('-------')
    print('More Features Will be Added Soon...')