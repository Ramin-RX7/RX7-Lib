import re as _re
from typing import Iterable,Callable,Any
from . import style

def wait_for_input(prompt=""):
    answer= ''
    while not answer:
        answer = input(prompt).strip()
    return answer

def selective_input(prompt:Any, choices:Iterable|Callable[[str],bool], default:Any=None,
                    ignore_case:bool=False, invalid_message:Any='Invalid input',
                    pre_action:Callable=...,post_action:Callable=...):
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
        elif not inp:
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

def yesno_input(prompt,default=None):
    error= "Invalid Input" if bool(default) else ""
    def action(inp):
        if inp.lower() in ("yes","y"):
            return True
        elif inp.lower() in ("no","n"):
            return False
    return selective_input(prompt,['y','yes','n','no'],default,True,error,action)

def Input(prompt:str ='', default_value:str =''):
    '''
    (WINDOWS ONLY)
    Make Default Value For Your Input!
    prompt is what you want and it's input(prompt) .
    default_value is what there should be after prompt.
    E.g:
    >>> Input('Is rx7 Library Easy to Learn?  ', 'Yes')
    Is rx7 Library Easy to Learn?  Yes
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

def regex_input(prompt,pattern,method="match"):
    """Checks the """
    inp = input(prompt)
    if method == "match":
        result = _re.match(pattern,inp)
    elif method == "search":
        result = _re.search(pattern,inp)
    else:
        raise ValueError
    if result:
        return True
    return False
