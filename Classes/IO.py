from typing import Any,Callable,Iterable
from ..rx7 import Style as style




def wait_for_input(prompt):
    answer= ''
    while not answer:
        answer = input(prompt).strip()
    return answer


def selective_input(prompt:Any, choices:Iterable|Callable[[str],bool], default:Any=None,
                    ignore_case:bool=False, invalid_message:Any='Invalid input',
                    action:Callable=None):

    assert (callable(action) or action==None)

    if not callable(choices):
        Choices = choices
        if type(choices) == dict:
            Choices = list(choices.keys())+list(choices.values())
        if ignore_case:
            Choices = [item.lower() for item in Choices if isinstance(item,str)]

    while True:
        inp = input(prompt)
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

    if action:
        inp = action(inp)

    return inp


def yesno_input(prompt,default=None):
    error= "Invalid Input" if bool(default) else ""
    def action(inp):
        if inp.lower() in ("yes","y"):
            return True
        else:
            return False
    return selective_input(prompt,['y','yes','n','no'],default,True,error,action)


def Input(prompt:str ='', default_value:str =''):
    '''
    Make Default Value For Your Input!
    (THIS ONLY WORK ON WINDOWS (SORRY))
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


def getpass(prompt):
    '''
    Prompt for a password, with echo turned off.
    '''
    import getpass as Getpass
    return Getpass.getpass(prompt=prompt)
