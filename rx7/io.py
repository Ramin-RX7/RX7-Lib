"""
High-level functions to manipulate user inputs
"""

import re as _re
from typing import Iterable,Callable,Any

from . import style



def wait_for_input(prompt="") -> str:
    """keeps prompting for user input until something but whitespace is entered

    Args:
        prompt (str, optional): Prompt. Defaults to "".

    Returns:
        str: user's input
    """
    answer= ''
    while not answer:
        answer = input(prompt).strip()
    return answer


def selective_input(prompt:Any, choices:Iterable|Callable[[str],bool], default:Any=...,
                    *,
                    ignore_case:bool=False, invalid_message:Any='Invalid input',
                    pre_action:Callable=...,post_action:Callable=...) -> str|Any:
    """Prompts for user input and waits until a acceptable input is given

    Args:
        prompt (Any): prompt to ask for user input
        choices (Iterable | Callable[[str],bool]):
            Either a callable that returns True/False for user input validation or
            an iterable that contains valid inputs
        default (Any, optional):
            default value if user does not enter anything . Defaults to Ellipsis
    Keyword-only Args:
        ignore_case (bool, optional):
            ignores case of letters. Defaults to False.
        invalid_message (Any, optional):
            Text to display when user enters wrong input. Defaults to 'Invalid input'
        pre_action (Callable, optional):
            function to call with given input before checking with validator.
        post_action (Callable, optional):
            function to call with given input after checking with validator.

    Returns:
        str|Any: user input as a string unless pre_action/post_action change the string type
    """
    assert (callable(pre_action )  or  pre_action==...)
    assert (callable(post_action)  or  post_action==...)
    if not callable(choices):
        Choices = choices
        if type(choices) == dict:
            Choices = list(choices.keys())+list(choices.values())
        if ignore_case:
            Choices = [item.lower() for item in Choices if isinstance(item,str)]
    while True:
        inp = input(prompt)
        if pre_action != ...:
            inp = pre_action(inp)
        inp = inp.lower() if ignore_case else inp
        if callable(choices):
            if choices(inp):
                break
            elif invalid_message:
                style.print(invalid_message, color='red')
        elif inp == "":
            if default:
                inp = default
                break
            else:
                if invalid_message:
                    style.print(invalid_message, color='red')
        elif inp in Choices:
            break
        else:
            if invalid_message:
                style.print(invalid_message, color='red')
    if type(choices) == dict:
        try:
            inp = choices[inp]
        except KeyError:
            pass
    if post_action != ...:
        inp = post_action(inp)
    return inp


def yesno_input(prompt:Any="", default=...) -> bool:
    """Asks for user to enter (yes,no,y,n)

    Args:
        prompt (Any, optional): Prompt
        default (Any, optional):
            Default value when user does not enter any input. Defaults to None.

    Returns:
        bool: True if user enters y/yes and False if n/no
    """
    error= "Invalid input" if bool(default) else ""
    def post_action(inp):
        if inp.lower() in ("yes","y"):
            return True
        elif inp.lower() in ("no","n"):
            return False
    return selective_input(
                prompt, ['y','yes','n','no'], default,
                ignore_case=True,
                invalid_message=error,
                post_action=post_action
    )


def Input(prompt:str ='', default_value:str =''):
    '''
    (WINDOWS ONLY)
    Writes default value for user input.
    `default_value` is what there should be by default after prompt.
    '''
    import win32console
    _stdin = win32console.GetStdHandle(win32console.STD_INPUT_HANDLE)
    keys = []
    for c in str(default_value):
        evt = win32console.PyINPUT_RECORDType(win32console.KEY_EVENT)
        evt.Char = c
        evt.RepeatCount = 1
        evt.KeyDown = True
        keys.append(evt)
    _stdin.WriteConsoleInput(keys)
    return input(str(prompt))


def getpass(prompt:str="Password: "):
    '''
    Prompt for a password, with echo turned off.
    '''
    import getpass
    return getpass.getpass(prompt=prompt)


def regex_input(prompt:Any, pattern:str, method="match") -> bool:
    """Checks to see if user input matches with given regex pattern or not

    Args:
        prompt (Any): Prompt
        pattern (str): regex pattern to check user input for validation
        method (str, optional):
            regex function to use for validation (only `search` and `match` are supported).
            Defaults to "match".

    Raises:
        ValueError: _description_

    Returns:
        bool: _description_
    """
    inp = input(prompt)
    if method == "match":
        result = _re.match(pattern,inp)
    elif method == "search":
        result = _re.search(pattern,inp)
    else:
        raise ValueError("method argument must be either `match` or `search`")

    if result:
        return True
    return False
