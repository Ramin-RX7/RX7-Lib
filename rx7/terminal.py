"""
Run Terminal Commands with Terminal functions
"""
import os as _os
import subprocess as _subprocess



from . functions import clear

@staticmethod
def run(command:str) -> None:
    '''
    Execute the command in a subshell
    Returns exit code
    (LIVE EXECUTION, OUTPUT WILL BE PRINTED)
    '''
    return _os.system(command)

@staticmethod
def getoutput(command:str) -> str:
    '''
    Return output of executing command in a shell
    (RETURN STR, RETURN AFTER EXECUTING CODE)
    '''
    return _subprocess.getoutput(command)
@staticmethod
def size() -> tuple:
    '''
    Return terminal size in tuple (columns,rows)
    '''
    return _os.get_terminal_size()
