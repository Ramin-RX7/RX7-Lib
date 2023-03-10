"""
This class is for Changing text Color,BG & Style.
(Using colored module but easier)
- style.print  to customize your print.
- style.switch to change terminal colors.
- style.switch_default for making everything default.

Also You Can Create style object.
This will allow you to:
- Because it returns string You can Add it to other strings
- Slicing and indexing (Without Color)
"""
import time as _time

from colored import fg   as  _fg
from colored import bg   as  _bg
from colored import attr as  _attr



class Style:
    """
    This class is for Changing text Color,BG & Style.
    (Using colored module but easier)
    - style.print  to customize your print.
    - style.switch to change terminal colors.
    - style.switch_default for making everything default.

    Also You Can Create style object.
    This will allow you to:
    - Because it returns string You can Add it to other strings
    - Slicing and indexing (Without Color)
    """
    def __init__(self, text, color='default', BG='default',style=0):
        self.text = text
        self.styled = ""
        if color != 'default':
            self.styled += f"{_fg(color)}"
        if BG    != 'default':
            self.styled += f"{_bg(BG)}"
        if style:
            self.styled += f"{_attr(style)}"
        self.styled += f"{text}"
        self.styled += f"{_attr(0)}"

    def __str__(self):
        return self.styled
    def __repr__(self):
        return self.styled
    def __add__(self, other):
        if type(other)!=Style:
            return self.styled+other
        else:
            return self.styled+other.styled


    @staticmethod
    def print(*values,color='default', BG='default', style=None, end='\n', sep=" "):
        '''
        text(text='Hello World',color='red',BG='white')
        output ==> 'Hello World' (With red color and white BG)
        Styles: bold - underlined - reverse - hidden
         *bold and underlined may not work. (Depends on terminal and OS)
        '''
        text = ""
        if color != 'default':
            text += f"{_fg(color)}"
        if BG    != 'default':
            text += f"{_bg(BG)}"
        if style:
            text += f"{_attr(style)}"

        if len(values):
            text += f"{values[0]}"
        for t in values[1:]:
            text += f"{sep}{t}"

        text += f"{_attr(0)}"

        print(text,end=end)


    @staticmethod
    def switch(color='default', BG='default', style=''):
        '''
        Change color,BG and style untill you call it again and change them.
        '''
        text = ""
        if color != 'default':
            text += f"{_fg(color)}"
        if BG    != 'default':
            text += f"{_bg(BG)}"
        if style:
            text += f"{_attr(style)}"

        print(f"{text}", end='')

    @staticmethod
    def switch_default():
        '''Switch Terminal Attributes to its defaults'''
        print(f'{_attr(0)}', end='')
    reset = switch_default


    def _get_now():
        return _time.strftime('%H:%M:%S',_time.localtime())
    def _log(text, color='', BG='default', style=None, add_time=True):
        #globals()['style'].print(text, color, BG, style=style)
        if add_time:
            NOW = f"[{Style._get_now(add_time)}]  "
        else:
            NOW = ""
        Style.print(f"{NOW}{text}", color=color, BG=BG, style=style)
    @staticmethod
    def log_success(text, color='green', BG='default', style=None, add_time=True):
        Style._log(text,color,BG,style,add_time)
    @staticmethod
    def log_info(text, color='dodger_blue_1', BG='default', style=None, add_time=True):
        Style._log(text,color,BG,style,add_time)
    @staticmethod
    def log_warning(text, color='gold_3a', BG='default', style=None, add_time=True):
        Style._log(text,color,BG,style,add_time)
    @staticmethod
    def log_error(text, color='red', BG='default', style=None, add_time=True):
        Style._log(text,color,BG,style,add_time)
    @staticmethod
    def log_critical(text, color='red_1', BG='default', style='bold', add_time=True):
        Style._log(text,color,BG,style,add_time)
