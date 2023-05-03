import os   as _os
import sys  as _sys
import abc  as _abc
import time as _time
import urllib   as _urllib
import subprocess as _subprocess

from typing import (Any,Iterable,Optional,Callable)





argv =  _sys.argv
ABC  =  _abc.ABC
exit =  _sys.exit
environ = _os.environ



from .files     import write    , read
from .io        import getpass  , Input
from .decorator import overload , Check_Type
from .style     import Styled





def p(text:str='', end='\n'):
    '''
    p is print!
    But because we use it a lot, we\'ve decided to make it one letter.
    Example:
        p('Hello World')
        ==>Hello World
    '''
    print(text, end=end)


def repeat(function:Callable, n: int, **kwargs):
    '''
    Repeat function for n times with given parameters
    for more info see the example below.
    Example:
        re(rx.screenshot, 3, image_name='screenshot.png')
        ==> "function rx.screenshot will be executed 3 times."
    '''
    for _ in range(n):
        function(**kwargs)


def wait(seconds:int):
    '''
    Use this if you want your program wait for a certain _time.

    Parameters
    ----------
    seconds : [int/float]
        time to sleep program in seconds
    '''
    _time.sleep(seconds)
sleep = wait


def cls():
    '''
    You can use this function if you want to clear the terminal environment.
    '''
    import platform
    if platform.system() == "Windows":
        _os.system('cls')
    else:
        _os.system('clear')
clear = cls


def wait_for(button:str):
    """
    If You Want to Wait For the User to Press a Key (Keyboard/Mouse)
     Use This Function.

    Parameters
    ----------
    button : str
        Button to click

    Raises
    ------
    ValueError
        It will be raised when invalid button is given
    """
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
    """
    Call Your Function Later Even Between Other Operations
    (This function uses threading module so be careful about
     how, when, and on what object you are going to operate on)

    Parameters
    ----------
    function : Callable
        this should be your function name

    delay : float,int
        delay before calling function in seconds, by default 0.001
    """
    import threading
    thread = threading.Thread(target=lambda: (sleep(delay), function(*args)))
    thread.start()
    #keyboard.call_later(function, args, delay)
call = call_later


def convert_bytes(nom:int) -> str:
    """
    Convert num to idiomatic byte unit.

    Parameters
    ----------
    num : int
        number you want to convert (in Byte)

    Returns
    -------
    str
        number + unit

    Examples
    --------
    >>> convert_bytes(200)
    '200.0 bytes'
    >>> convert_bytes(6000)
    '5.9 KB'
    >>> convert_bytes(80000)
    '78.1 KB'
    """
    '''


    '''
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if nom < 1024.0:
            return "%3.1f %s" % (nom, x)
        nom /= 1024.0


def restart_app(python3:bool = False):
    """
    This Function Close App and Recall it From Terminal
    (It uses terminal.run to run command 'python[3] *argv')

    Parameters
    ----------
    python3 : bool, optional
        use 'python' or 'python3', by default False
    """
    _os.execv(_sys.executable, ['python3' if python3 else 'python'] + _sys.argv)
    _sys.exit()


def active_window_title() -> str:
    """
    Get active windows title
    (Usually terminal is active window title
    but if during executing your script you change window
    this will return new window title)

    Returns
    -------
    str
        string of active window title
    """
    import pyautogui
    return pyautogui.getActiveWindowTitle()


def open_image(path:str) -> None:
    """
    Open image file with default image viewer.
    (Mac OS is not supported yet)

    Parameters
    ----------
    path : str
        path to the image file

    Raises
    ------
    OSError
        It will be raised when you run this function in not supported OS
    """
    import platform
    if platform.system() == 'Windows':
        _os.system(path)
    elif platform.system() == 'Linux':
        _subprocess.getoutput(f'xdg-open {path}')
    else:
        raise OSError('Only Windows and Linux are supported for this function.')

def download(url:str, filename:str="auto", save_memory:bool=True,
             progressbar:bool =True, prefix:str='Downloading'):
    '''
    Use this function to download files.
    if filename is not given, it will be last part of the url.
    filename can be path for saving file.
    save_memory parameter is used to save memory in large files
    (save directly to storage)
    '''
    import requests as _requests
    if filename=='auto':
        filename = url.split('/')[-1]

    if save_memory:
        '''
        with _urllib.request.urlopen(url) as response, open(filename, 'wb') as f:
            _shutil.copyfileobj(response, f)
        '''
        '''
        r = _requests.get(url, stream = True)
        with open(filename,"wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        '''
        if progressbar:
            with open(filename, "wb") as f:
                response = _requests.get(url, stream=True)
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
                        _sys.stdout.write(f"\r{prefix} {filename}: |{'█' * done}{' ' * (33-done)}| {100-((33-done)*3)}%")
                        _sys.stdout.flush()
                    if 100-((33-done)*3) == 96:
                        _sys.stdout.write(f"\r{prefix} {filename}: |{'█' * done}{' ' * (33-done)}| 100%")
                        _sys.stdout.flush()
        else:
            with open(filename, "wb") as f:
                response = _requests.get(url, stream=True)
                for data in response.iter_content(chunk_size=4096):
                    f.write(data)
    else:
        def report(blocknr, blocksize, size):
            if progressbar:
                current = blocknr*blocksize
                _sys.stdout.write("\rDownloading {1}:  {0:.2f}%".format(100.0*current/size,filename))
        def downloadFile(url):
            _urllib.request.urlretrieve(url, filename, report)
        downloadFile(url)
    pass
    if progressbar: print()


def extract(filename:str, path:Optional[str]=None,files:Optional[Iterable[str]]=None,
            password:Optional[str]=None) -> None:
    """
    Extract Files from Zip files
    By default it extracts all files

    Parameters
    ----------
    filename : str
        path to .zip file
    path : str, optional
        path to extract files (by default: folder in current working directory)
    files : Iterable[str], optional
        Iterable of files you want to extract, by default None
    password : str, optional
        password if your .zip file is password protected, by default None
    """
    import zipfile
    zipfile.ZipFile(filename, 'r').extractall(path=path,members= files,pwd=password)

def screenshot(image_name:str = 'Screenshot.png'):
    '''
    This function will take a screenshot and save it as image_name
    '''
    import pyscreeze
    return pyscreeze.screenshot(image_name)


def func_info(func:Callable):
    """
    print some information about 'func'

    Parameters
    ----------
    func : Callable
        function you want to get its information
    """
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


def Progressbar(
    total=60, dashes_nom=30, empty_shape=' ', complete_shape='█',
    pre_text='Loading: ', left_port='|', right_port='|'):
    '''
    Make your code more beautiful with progressbars!
     this is generator function so use it like this:
        >>> for _ in generator(100,10):
                do_this()
                do_that()
        Loading: |████      | 40/100
    '''
    echo = _sys.stdout
    def show(j):
        x = int(dashes_nom*j/total)
        echo.write(
            f"{pre_text}{right_port}{complete_shape*x}{empty_shape*(dashes_nom-x)}{left_port} {j}/{total}\r")
        echo.flush()
    show(0)
    for i, item in enumerate(range(total)):
        yield item
        show(i+1)
    echo.write("\n")
    echo.flush()


_MOUSE_X = 0
_MOUSE_Y = 0
def pixel_color(x=_MOUSE_X, y=_MOUSE_Y) -> tuple:
    """
    Function to return color of pixel of screen in tuple of RGB

    Parameters
    ----------
    x : int
        pixel of column x, by default last x of mouse
    y : int
        pixel of row y, by default last y of mouse

    Returns
    -------
    tuple
        tuple with 3 integers: (RED,GREEN,BLUE)
    """
    import pyautogui
    if not x:
        x = pyautogui.position()[0]
    if not y:
        y = pyautogui.position()[1]
    PIXEL = pyautogui.screenshot(region=(x, y, 1, 1))
    COLOR = PIXEL.getcolors()
    return COLOR[0][1]


def import_module(path:str):
    """
    Import modules from files even if they are not .py

    Parameters
    ----------
    path : str
        path to file to import it

    Returns
    -------
    ModuleType
        return module
    """
    import importlib.machinery
    import importlib.util
    loader = importlib.machinery.SourceFileLoader('MOD', path)
    spec = importlib.util.spec_from_loader(loader.name, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod



#######################
#     TUPLE FUNCS     #
#######################
def force(tpl: Any, *var: Any) -> tuple:
    '''
    (TUPLE FUNCTION)
    It returns tpl with adding var(s) to it.
    '''
    return tuple(list(tpl)+[v for v in var])
#force= lambda tpl,*var: tuple(list(tpl)+[v for v in var])


def erase(tpl: tuple, *var: Any) -> tuple:
    '''
    (TUPLE FUNCTION)
    It returns tpl with removing var(s) from it.
    '''
    #lstv= [v for v in var if v in tpl]
    lstt= list(tpl)
    for th in [v for v in var if v in tpl]:
        lstt.remove(th)
    return tuple(lstt)


def replace(tpl: tuple, index:int, var: Any) -> tuple:
    '''
    (TUPLE FUNCTION)
    Replace tpl[ind] with var
    '''
    tpl=list(tpl)
    if type(index) == str:
        index= tpl.index(index)
    tpl[index]=var
    return tuple(tpl)


def insert(tpl: tuple, index:int, var: Any) -> tuple:
    '''
    (TUPLE FUNCTION)
    Exactly like tpl[ind]=var in lists but for tuples.
    '''
    tpl=list(tpl)
    if type(index) == str:
        index= tpl.index(index)
    tpl.insert(index,var)
    return tuple(tpl)


def pop(tuple,index=-1):
    '''
    (TUPLE FUNCTION)
    pop method that is used in lists but for tuples
    '''
    return tuple(list(tuple).pop(index))
