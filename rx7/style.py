'''
This class is for Changing text Color,BG & Style.
(Using colored module but easier)
- print()  to customize your print.
- switch() to change terminal colors.
- switch_default() for making everything default.
Also You Can Create `styled` object.
This will allow you to:
- Because it returns string You can Add it to other strings
- Slicing and indexing (Without Color)
'''
import builtins as _builtins
import time as _time

from colored import fg   as  _fg
from colored import bg   as  _bg
from colored import attr as  _attr



from pprint import pprint,pformat

_default = -1
class Styled(str):
    """
    Styled object is a string with given color/background color/style
    (All methods and attributes of strings are accepted on Styled objects since it inherits string)
    """
    def __new__(cls, text, color=_default, BG=_default, style=0):
        string = ""
        if color != 'default':
            string += f"{_fg(color)}"
        if BG    != 'default':
            string += f"{_bg(BG)}"
        if style:
            string += f"{_attr(style)}"
        string += f"{text}"
        string += f"{_attr(0)}"
        return super().__new__(str, string)



def print(*values,color=_default, BG=_default, style=0, sep=" ", end='\n') -> None:
    """prints out the given values decorated with given color/bg/style.

    (You can get list of all colors and styles with: $ python -m rx7 --colors)

    Args:
        color (str, optional): color to use when printing. Defaults to 'default'.
        BG (str, optional): background color of output. Defaults to 'default'.
        style (_type_, optional): style of output text. Defaults to None.
        end (str, optional): last part of print. Defaults to '\n'.
        sep (str, optional): Separator of values in output. Defaults to " ".
    """
    values = map(str, values)
    string = Styled(sep.join(values)+end, color=color, BG=BG, style=style)
    _builtins.print(string, end="")


def switch(color=_default, BG=_default, style='') -> None:
    '''
    Changes the color, BG and style of terminal output until you change it again
    '''
    text = ""
    if color != _default:
        text += f"{_fg(color)}"
    if BG    != _default:
        text += f"{_bg(BG)}"
    if style:
        text += f"{_attr(style)}"
    _builtins.print(f"{text}", end='')


def switch_default() -> None:
    '''Switch terminal attributes to their defaults'''
    _builtins.print(f'{_attr(0)}', end='')
reset = switch_default


def _get_now():
    return _time.strftime('%H:%M:%S',_time.localtime())
def _log(pre, text, color='', BG='default', style=None, add_time=True):
    #globals()['style'].print(text, color, BG, style=style)
    if add_time:
        NOW = f"[{_get_now()}]  "
    else:
        NOW = ""
    print(f"{NOW}{text}", color=color, BG=BG, style=style)


def log_success(text, color='green', BG='default', style=None, add_time=True):
    _log("[+]",text,color,BG,style,add_time)

def log_info(text, color='dodger_blue_1', BG='default', style=None, add_time=True):
    _log("[*]",text,color,BG,style,add_time)

def log_warning(text, color='gold_3a', BG='default', style=None, add_time=True):
    _log("[*]",text,color,BG,style,add_time)

def log_error(text, color='red', BG='default', style=None, add_time=True):
    _log("[!]",text,color,BG,style,add_time)

def log_critical(text, color='red_1', BG='default', style='bold', add_time=True):
    _log("[!]",text,color,BG,style,add_time)
