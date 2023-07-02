"""
Functions related to working with running terminal

- run():  run a command from shell
- getoutput():  get the result of a command from terminal
- size():  returns size of terminal
- clear():  clears the terminal
"""
import os as _os
import subprocess as _subprocess



from . functions import clear


@staticmethod
def run(command:str) -> int:
    '''
    Execute the command in a subshell.
    Returns exit code
    '''
    return _os.system(command)


@staticmethod
def getoutput(command:str) -> str:
    '''
    Return output of given command in a shell
    '''
    return _subprocess.getoutput(command)


@staticmethod
def size() -> tuple:
    '''
    Return terminal size in tuple (columns,rows)
    '''
    return _os.get_terminal_size()
