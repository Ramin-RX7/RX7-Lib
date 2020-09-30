'''
This Module is One to Make Your Code Shorter.
High API Will Make You Feel You're Ordering And Machine Is Doing!
Also There is Collection of most usefull function and methods from popular modules of python.
(Read Help of Functions)
Official Documention Will Be Added Soon.
'''
'''
Written By RX
Last Update: 10-01-2020
'''

__version__ = '2.6.0'

'''
TODO:
 - Screen recorder
 - Open Video
 - Open Audio
 - Make Sound
 - registery editor
 - pip install update
 - style defaults
 - time.process_time()
 - style.COLOR
 - mp3 tags
 - No_Error func
 - Style.print INFO WARNING
 - getpass.getpass
 - re module
 - CHECK 3rd-party Modules imports
'''



#START

import os
import time
import sys
import subprocess
import random as _RANDOM
from typing import Any, Iterable, Optional, Callable



#######        8888888888                         888    d8b                                   ####### 
####           888                                888    Y8P                                      #### 
####           888                                888                                             #### 
####           8888888 888  888 88888b.   .d8888b 888888 888  .d88b.  88888b.  .d8888b            #### 
####           888     888  888 888 "88b d88P"    888    888 d88""88b 888 "88b 88K                #### 
####           888     888  888 888  888 888      888    888 888  888 888  888 "Y8888b.           #### 
####           888     Y88b 888 888  888 Y88b.    Y88b.  888 Y88..88P 888  888      X88           #### 
#######        888      "Y88888 888  888  "Y8888P  "Y888 888  "Y88P"  888  888  88888P'        ####### 


def p(text='', end='\n'):
    '''
    p is print!
    But because we use it a lot, we\'ve decided to make it one letter.
    Example:
        p('Hello World')
        ==>Hello World
    '''
    print(text, end=end)

def repeat(function, n: int, **kwargs):
    '''
    Repeat function for n times with given parameters
    for more info see the example below.
    Example:
        re(rx.screenshot, 3, image_name='screenshot.png')
        ==> "function rx.screenshot will be executed 3 times."
    '''
    for _ in range(n):
        function(**kwargs)

def wait(seconds):
    '''
    Use this if you want your program wait for a certain time.
    Example:
        wait(3)
        ==> "Nothing happen and there will be no calculation for 3 seconds"
    '''
    time.sleep(seconds)
sleep = wait

def cls():
    '''
    You can use this function if you want to clear the environment.
    '''
    import platform
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
clear = cls

def progressbar(
    total=100, dashes_nom=100, delay=1, dashes_shape=' ', complete_shape='█',
    pre_text='Loading: ', left_port='|', right_port='|'):
    '''
    Use this function to make a custom in-app progress bar (Not Very Usefull).
    (Use Progressbar() Generator instead to do your stuffs while updating progressbar)
    Example:
        progressbar(
            Total=100,Dashes_Nom=10,Time=1,Dashes_Shape='-',
            Complete_Shape='#', Pre_Text='Loading')
        ==>   Loading|####------| 40/100
    '''
    def Progressbar(it, prefix="", size=60, file=sys.stdout):
        count = len(it)
        def show(j):
            x = int(size*j/count)
            file.write(f"{prefix}{right_port}{complete_shape*x}{dashes_shape*(size-x)}{left_port} {j}/{count}\r")
            file.flush()        
        show(0)
        for i, item in enumerate(it):
            yield item
            show(i+1)
        file.write("\n")
        file.flush()
    for _ in Progressbar(range(total), pre_text, dashes_nom):
        wait(delay)

def wait_for(button:str):
    '''
    If You Want to Wait For the User to Press a Key Use This Function.
    (both Keyboard and Mouse)
    '''
    button = button.lower()
    if button.lower() in ('middle', 'left', 'right', 'back', 'forward'):
        if button == 'back':
            button = 'x'
        if button == 'forward':
            button = 'x2'
        import mouse
        mouse.wait(button)
    else:
        import keyboard
        try:
            keyboard.wait(button)
        except:
            raise ValueError('Incorrect Button Name.')

def call_later(function:Callable, *args, delay=0.001):
    '''
    Do You Want to Call Your Function Later Even Between Other Operations?
    call_later() will help you to do that!
    First arg should be your function name,
    After That (*args) you can add any args that your function need,
    And last arg is delay for calling your function in seconds.
    '''
    import keyboard
    keyboard.call_later(function, args, delay)

def convert_bytes(num:int) -> str :
    """
    Convert num to idiomatic byte unit.
    num is the input number (bytes).
    
    >>> convert_bytes(200)
    '200.0 bytes'
    >>> convert_bytes(6000)
    '5.9 KB'
    >>> convert_bytes(80000)
    '78.1 KB'
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

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
default_input = Input

def restart_app(python3:bool = False):
    '''
    This Function Close App and Recall it From Terminal
    '''
    os.system('clear')
    os.execv(sys.executable, ['python3' if python3 else 'python'] + sys.argv)

def active_window_title():
    '''
    Get active windows title  
    (Usually terminal is active window title 
    but if during executing your script if you change window 
    this will return new window title)
    '''
    import pyautogui
    return pyautogui.getActiveWindowTitle()

def open_image(path:str):
    '''
    Open image file with default image viewer.  
    (Mac OS is not supported yet)
    '''
    import platform
    if platform.system() == 'Windows':
        os.system(path)
    elif platform.system() == 'Linux':
        subprocess.getoutput(f'xdg-open {path}')
    else:
        raise OSError('OS X is not supported for this function.')

BASENAME=''
def download(url:str, filename:str =BASENAME, save_memory:bool=True,
             progressbar:bool =True, prefix:str='Downloading'):
    '''
    Use this function to download files.  
    if filename is not given, it will be last part of the url.  
    filename can be path for saving file.  
    save_memory parameter is used to save memory in large files
    (save directly to storage)
    '''
    import requests, urllib
    if not filename:
        filename = url.split('/')[-1]

    if save_memory:
        '''
        with urllib.request.urlopen(url) as response, open(filename, 'wb') as f:
            shutil.copyfileobj(response, f)
        '''
        '''
        r = requests.get(url, stream = True)
        with open(filename,"wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        '''
        if progressbar:
            with open(filename, "wb") as f:
                response = requests.get(url, stream=True)
                total_length = response.headers.get('content-length')
                if total_length is None:
                    f.write(response.content)
                else:
                    dl = 0
                    done = 0
                    total_length = int(total_length)
                    for data in response.iter_content(chunk_size=4096):
                        dl += len(data)
                        f.write(data)
                        done = int(33 * dl / total_length)
                        sys.stdout.write(f"\r{prefix} {filename}: |{'█' * done}{' ' * (33-done)}| {100-((33-done)*3)}%")
                        sys.stdout.flush()
                    if 100-((33-done)*3) == 96:
                        sys.stdout.write(f"\r{prefix} {filename}: |{'█' * done}{' ' * (33-done)}| 100%")
                        sys.stdout.flush()
        else:
            with open(filename, "wb") as f:
                response = requests.get(url, stream=True)
                for data in response.iter_content(chunk_size=4096):
                    f.write(data)               
    else:
        def report(blocknr, blocksize, size):
            if progressbar:
                current = blocknr*blocksize
                sys.stdout.write("\rDownloading {1}:  {0:.2f}%".format(100.0*current/size,filename))
        def downloadFile(url):
            urllib.request.urlretrieve(url, filename, report)
        downloadFile(url)
    pass
    if progressbar: print()

def extract(
    filename:str, path:Optional[str]=None,
    files:Optional[Iterable[str]]=None, password:Optional[str]=None) -> None: 
    '''
    Extract Files from Zip File.\n
    If files parameter is None it will extract all files.\n
    path is path to extract
    '''
    import zipfile
    zipfile.ZipFile(filename, 'r').extractall(path=path,members= files,pwd=password)

def screenshot(image_name:str ='Screenshot.png'):
    '''
    This function will take a screenshot and save it as image_name
    '''
    import pyscreeze
    return pyscreeze.screenshot(image_name)

def func_info(func:Callable):

    help(func) #func.__doc__
    print('-'*30)
    print('Module  ', func.__module__)
    print('-'*30)
    try:
        _code_ = str(func.__code__)
        _code_ = _code_[_code_.index(',')+2:-1]
    except AttributeError:
        _code_ =  f'No "file" and "line" information available '
        _code_ += f' (I guess "{func}" is a built-in function)'
    print(_code_)

class Check_Type:
    """
    Function decorator for developers\n
    Use this decorator to check if user gives right argument type\n
    You need to annotate argument type when defining it.\n
    Supported Types:
    * str
    * list
    * set
    * dict
    * tuple
    * User-Defined Objects
    Typing Module Supported Types:
    * Iterable
    * Callable
    * Generatr
    * Container
    * Any
    (MORE TYPES SOON ...)
    """
    auto_correct = False

    def __init__(self, function): 
        self.function = function


    def __call__(self, *args, **kwargs): 
        special_types = ('callable', 'iterable', 'generator','container', 'any')

        i=-1
        __local__= list(locals()['args'])
        annots= list(self.function.__annotations__.keys())

        def extra_remover(correct):
            # Typing module annots check
            if correct.startswith('typing.'):
                correct = correct[7:].lower()

            # built-in types check
            elif correct.startswith('<class '):
                correct = correct[8:-2]

            return correct

        def check_specials(TYPE, LOCAL_I):
            import inspect
            wrong = ''
            if TYPE == 'generator':
                if inspect.isgeneratorfunction(LOCAL_I) or inspect.isgenerator(LOCAL_I):
                    return
                else:
                    correct = 'generator'

            elif TYPE == 'callable':
                if callable(LOCAL_I):
                    return
                else:
                    correct = 'callable'
            
            elif TYPE == 'iterable':
                if type(LOCAL_I) in (list, tuple, set, str):
                    print(type(LOCAL_I))
                    return
                else:
                    correct = 'iterable'

            elif TYPE == 'container':
                if type(LOCAL_I) in (list,set,dict,tuple):
                    return
                else:
                    correct = 'container'

            elif TYPE == 'any':
                return

            wrong = extra_remover(str(type(LOCAL_I))) if not wrong else wrong
            func_name = self.function.__name__
            Error= TypeError(f"'{func_name}()' argument '{ARG}' must be '{correct}' (not '{wrong}')")
            raise Error

        for ARG in annots:
            i += 1
            try:
                LOCAL_I = __local__[i]
                correct = str(self.function.__annotations__[ARG])
                
                '''if correct.startswith('typing.Union'):
                    correct = eval(correct[12:])
                if type(correct) != list:
                    correct = [correct]'''

                correct = extra_remover(correct)
                
                if correct in special_types:
                    print(type(LOCAL_I))
                    check_specials(correct,LOCAL_I)
                
                # Builtins and other Libraries objects
                elif not eval(correct) == type(LOCAL_I):
                    if Check_Type.auto_correct:
                        try:
                            __local__[i] = eval(correct)(LOCAL_I)
                            continue
                        except ValueError:
                            pass

                    wrong = extra_remover(str(type(LOCAL_I)))
                    #correct = str(self.function.__annotations__[ARG])#[8:-2]
                    correct = extra_remover(correct)
                    func_name = self.function.__name__
                    Error= TypeError(f"'{func_name}()' argument '{ARG}' must be '{correct}' (not '{wrong}')")
                    raise Error
            
            except (ValueError,IndexError):
                pass#raise
            except NameError:
                raise

            
        
        return self.function(*__local__, **kwargs)

def Progressbar(
    total=60, dashes_nom=30, dashes_shape=' ', complete_shape='█',
    pre_text='Loading: ', left_port='|', right_port='|'):
    '''
    Make your code more beautiful with progressbars!
     this is generator function so use it like this:
        >>> for _ in generator(100,10):
                do_this()
                do_that()
        Loading: |████      | 40/100
    '''
    echo = sys.stdout
    def show(j):
        x = int(dashes_nom*j/total)
        echo.write(
            f"{pre_text}{right_port}{complete_shape*x}{dashes_shape*(dashes_nom-x)}{left_port} {j}/{total}\r")
        echo.flush()        
    show(0)
    for i, item in enumerate(range(total)):
        yield item
        show(i+1)
    echo.write("\n")
    echo.flush()

_MOUSE_X = ''
_MOUSE_Y = ''
def pixel_color(x=_MOUSE_X, y=_MOUSE_Y) -> tuple:
    '''
    Function to return color of pixel of screen in RGB
    By default x and y are last mouse position
    '''
    import pyautogui
    if not x:
        x = pyautogui.position()[0]
    if not y:
        y = pyautogui.position()[1]
    PIXEL = pyautogui.screenshot(region=(x, y, 1, 1))
    COLOR = PIXEL.getcolors()
    return COLOR[0][1]




#######         .d8888b.   888  888                                                          ####### 
####           d88P  Y88b  888  888                                                             #### 
####           888    888  888  888                                                             #### 
####           888         888  888   8888b.   .d8888b   .d8888b    .d88b.   .d8888b            #### 
####           888         888  888      "88b  88K       88K       d8P  Y8b  88K                #### 
####           888    888  888  888  .d888888  "Y8888b.  "Y8888b.  88888888  "Y8888b.           #### 
####           Y88b  d88P  888  888  888  888       X88       X88  Y8b.           X88           #### 
#######         "Y8888P"   888  888  "Y888888   88888P'   88888P'   "Y8888    88888P'        ####### 


from .Filex import *
from .Tuple_tools import *
#from .RX_obj import *
from .System import *
#from .Date_Time import *
write = files.write
read  = files.read


class random:
    '''
    random Variable Generator Class.
    (ALL FUNCTIONS ARE STATIC METHODS)
    '''
    
    @staticmethod
    def choose(iterator,k: int =1,duplicate=True):
        '''
        Return a random element from a non-empty sequence.
        '''
        if type(k) != int:
            raise TypeError('k must be integer.')
        
        if k == 1:
            return _RANDOM.choice(iterator)
        elif k > 1:
            if duplicate:
                return _RANDOM.choices(iterator,k=k)
            else:
                return _RANDOM.sample(iterator,k=k)
        else:
            raise ValueError('k Must Be Higher 0')     
    
    @staticmethod
    def integer(first_number,last_number):
        '''
        Return _RANDOM integer in range [a, b], including both end points.
        '''
        return _RANDOM.randint(first_number,last_number)
    
    @staticmethod
    def O1(decimal_number=17):
        '''
        return x in the interval [0, 1)
        '''
        return round(_RANDOM.random(),decimal_number)
    
    @staticmethod
    def number(first_number,last_number):
        '''
        return x in the interval [F, L]
        '''
        return _RANDOM.uniform(first_number,last_number)

    @staticmethod
    def shuffle(iterable):
        '''
        Return shuffled version of iterable
        '''
        real_type = type(iterable)
        new_iterable = list(iterable)

        _RANDOM.shuffle(new_iterable)

        if real_type in (set,tuple):
            return real_type(new_iterable)

        elif real_type == str:
            return ''.join(new_iterable)

        elif real_type == dict:
            return {item:iterable[item] for item in new_iterable}

        else:
            return new_iterable
Random = random

from colored import fg, bg, attr
class Style:
    '''
    This class is for Changing text Color,BG & Style.
    (Using colored module but easier)
    - style.print  to customize your print.
    - style.switch to change terminal colors.
    - style.switch_default for making everything default.

    Also You Can Create style object.  
    This will allow you to:
    - Because it returns string You can Add it to other strings
    - Slicing and indexing (Without Color)
    '''
    def __init__(self, text, color='default', BG='black'):
        try:
            self.color = color.lower()
            self.BG = BG.lower()
            #style = style.lower()
        except:
            pass        
        if color == 'default':
            self.color = 7 #188
        self.text = text
        self.content = f"{fg(color)}{bg(BG)}{text}{attr(0)}"
    def __str__(self):
        return self.content
    def __repr__(self):
        return self.content
    def __add__(self, other):
        #print(type(other))
        if type(other)!=style:
            return self.content+other
        else:
            return self.content+other.content
    def __mul__(self, nom):
        return self.content*nom
    def __getitem__(self, index):
        return f'{fg(self.color)}{bg(self.BG)}{self.text}'+self.content[index]+attr(0)
    

    @staticmethod
    def print(text='', color='default', BG='default', style='None', end='\n'):
        '''
        text(text='Hello World',color='red',BG='white')
        output ==> 'Hello World' (With red color and white BG)
        Styles: bold - underline - reverse - hidden
         *bold and underline may not work. (Depends on terminal and OS)
        '''
        try:
            color = color.lower()
            BG = BG.lower()
            style = style.lower()
        except:
            raise
        

        if style == 'none':
            style = 0

        if color=='default' and BG!='default':  # bg & !clr
            print(f'{attr(style)}{bg(BG)}{text}{attr(0)}', end=end)

        elif color!='default' and BG=='default':  # !bg & clr
            print(f'{attr(style)}{fg(color)}{text}{attr(0)}', end=end)

        elif color=='default' and BG=='default':  # !bg & !clr
            print(f'{attr(style)}{text}{attr(0)}', end=end)

        elif color!='default' and BG!='default':  # bg & clr
            print(f'{attr(style)}{bg(BG)}{fg(color)}{text}{attr(0)}', end=end)

    @staticmethod
    def switch(color='default', BG='black', style='None'):
        '''
        Change color,BG and style untill you call it again and change them.
        '''
        try:
            color = color.lower()
            BG = BG.lower()
            style = style.lower()
        except:
            pass

        if style == 'none':
            style = 0
        if color == 'default':
            color = 7

        print(f'{attr(style)}{bg(BG)}{fg(color)}', end='')

    @staticmethod
    def switch_default():
        '''Switch Terminal Attributes to its defaults'''
        print('%s' % (attr(0)), end='')
style = Style

class Record:
    '''
    Use this method to record an action time in second.
    Usage:
        Start= record()
        #Some codes here...
        Finnish= Start.lap()
        print(Finnish) ==> 0.25486741
        #Some more codes here...
        Finnish= Start.lap() ==> 0.4502586
        Start.laps -->  [0.25486741, 0.4502586]
    Use Start.stop() to finnish recording and save memory.
    (after self.stop() using self.lap will cause error.)
    '''
    def __init__(self):
        self.__start = time.time()
        self.__end__ = False
        self.laps = []
    def __str__(self):
        if not self.__end__:
            running = True
        else:
            running = False
        return f'Running={str(running)} \nLaps: {self.laps}'
    def __repr__(self):
        if not self.__end__:
            running = True
        else:
            running = False
        return f'Running={str(running)} \nLaps: {self.laps}'

    class EndError(Exception):
        def __init__(self, message='Recording Has Been Finnished. Can Not Add a Lap.'):
            super().__init__(message)
    def lap(self, save=True, Round=15):
        '''
        Return time passed from creating time of self.
        (Read 'record' Doc String)
        If save is True, time will be added to self.laps
        '''        
        if not self.__end__:
            lp = time.time() - self.__start
            lp = round(lp,Round)
            if save:
                self.laps.append(lp)
            return lp
        else:
            raise self.EndError
    def stop(self):
        self.__end__ = True
        '''del self
        return self.laps'''
    def reset(self, reset_start=False):
        '''
        This will erase self.laps 
        If reset_start is True, start time will reset too.
        '''
        self.laps = []
        if reset_start:
            self.__start = time.time()
record = Record

class Terminal:
    """
    Run Terminal Commands with Terminal functions
    (ALL FUNCTIONS ARE STATIC METHODS)
    """
    @staticmethod
    def run(command:str) -> None:
        '''
        Execute the command in a subshell
        (NO RETURN, LIVE EXECUTION, OUTPUT WILL BE PRINTED)
        '''
        os.system(command)

    @staticmethod
    def getoutput(command:str) -> str:
        '''
        Return output of executing command in a shell
        (RETURN STR, RETURN AFTER EXECUTING CODE)
        '''
        return subprocess.getoutput(command)
terminal = Terminal


#END
