"""
All variables and functions (out of all modules) are defined here.
"""

import os   as _os
import sys  as _sys
import abc  as _abc
import time as _time
import urllib   as _urllib
import subprocess as _subprocess

from typing import (Any,Iterable,Optional,Callable)
from types import ModuleType





argv =  _sys.argv
ABC  =  _abc.ABC
exit =  _sys.exit
environ = _os.environ



from .files     import write    , read
from .io        import getpass  , Input
from .decorator import overload , Check_Type
from .style     import Styled





def repeat(function:Callable, n: int, *args, **kwargs) -> tuple:
    """Repeat function for n times with given parameters

    Args:
        function (Callable): function to be called
        n (int): number of times to execute function

    Returns:
        tuple: return the result of each call of the function in a tuple
    """
    for _ in range(n):
        function(*args, **kwargs)


def wait(seconds:int|float):
    """Sleeps the program for given `seconds`.

    Args:
        seconds (int|float): time to sleep program in seconds
    """
    _time.sleep(seconds)
sleep = wait


def cls():
    """Clears the terminal environment
    """
    import platform
    if platform.system() == "Windows":
        _os.system('cls')
    else:
        _os.system('clear')
clear = cls


def wait_for(button:str):
    """Waits For the User to press a key from Keyboard/Mouse

    Args:
        button (str): Button to click

    Raises:
        ValueError: raised when invalid button is given
    """
    button = button.lower()
    if button.lower() in ('middle', 'left', 'right', 'back', 'forward'):
        if button == 'back':
            button = 'x'
        elif button == 'forward':
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
    """Call the given function after given delay
    (NOTE: This function does not pause the program. it uses threads so
    be careful about how, when, and on what object you are going to operate on)

    Args:
        function (Callable): function to be called after delay
        delay (float, optional): delay before calling function in seconds. Defaults to 0.001.
    """
    import threading
    thread = threading.Thread(target=lambda:(sleep(delay), function(*args)))
    thread.start()
call = call_later


def convert_bytes(nom:int) -> str:
    """Convert num to idiomatic byte unit.

    Args:
        nom (int): number you want to convert (in Byte)

    Returns:
        str: number + unit

    Examples:
        >>> convert_bytes(200)
        '200.0 bytes'
        >>> convert_bytes(6000)
        '5.9 KB'
        >>> convert_bytes(80000)
        '78.1 KB'
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if nom < 1024.0:
            return "%3.1f %s" % (nom, x)
        nom /= 1024.0


def restart_app(python3:bool = False):
    """
    This Function recall the app from terminal

    Args:
        python3 (bool, optional): use 'python' or 'python3', by default False.
    """
    _os.execv(_sys.executable, ['python3' if python3 else 'python'] + _sys.argv)


def active_window_title() -> str:
    """Returns active windows title
    (Usually terminal is active window but if during executing your script you
     change window this will return the title of that window)

    Returns:
        str: cuurent active window title
    """
    import pyautogui
    return pyautogui.getActiveWindowTitle()


def open_image(path:str) -> None:
    """Open image file with default image viewer.
    (Mac OS is not supported yet)

    Args:
        path (str): path to the image file

    Raises:
        OSError: raised when be called in an unsupported OS
    """

    import platform
    os = platform.system()
    if   os == 'Windows':
        _os.system(path)
    elif os == 'Linux':
        _subprocess.getoutput(f'xdg-open {path}')
    else:
        raise OSError('Only Windows and Linux are supported for this function.')


def download(url:str, filename:str="auto", save_memory:bool=True,
             progressbar:bool =True, prefix:str='Downloading'):
    """Download the file from given url

    Args:
        url (str): url of the file
        filename (str, optional): path to save the file.
            if not given, it will be last part of the url. Defaults to "auto".
        save_memory (bool, optional):
            saves up memory when downloading huge files. Defaults to True.
        progressbar (bool, optional):
            show a progressbar when downloading. Defaults to True.
        prefix (str, optional):
            prefix of progressbar. Defaults to 'Downloading'
    """
    import requests as _requests
    if filename=='auto':
        filename = url.split('/')[-1]

    if save_memory:
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

    if progressbar:
        print()


def extract(filename:str, path:Optional[str]=None,files:Optional[Iterable[str]]=None,
            password:Optional[str]=None) -> None:
    """Extract Files from Zip files. By default it extracts all files

    Args:
        filename (str): path to .zip file
        path (Optional[str], optional):
            path to extract files (by default: current working directory).
        files (Iterable[str], optional):
            iterable of files to extract. Defaults to all files.
        password (str, optional):
            password of zip file if it is protected. Defaults to None.
    """
    import zipfile
    zipfile.ZipFile(filename, 'r').extractall(path=path,members= files,pwd=password)


def screenshot(image_name:str = 'Screenshot.png'):
    """This function will take a screenshot and save it as image_name

    Args:
        image_name (str, optional):
            path to save the screenshot. Defaults to 'Screenshot.png'.

    Returns:
        _type_: _description_
    """
    import pyscreeze
    return pyscreeze.screenshot(image_name)


def Progressbar(
    total=60, dashes_nom=30, empty_shape=' ', complete_shape='█',
    pre_text='Loading: ', left_port='|', right_port='|'):
    """Generator to display a progressbar for doing something

    Args:
        total (int, optional): total number of calls. Defaults to 60.
        dashes_nom (int, optional): number of cells. Defaults to 30.
        empty_shape (str, optional): empty parts of progressbar. Defaults to ' '
        complete_shape (str, optional): completed parts of it. Defaults to '█'.
        pre_text (str, optional): text before progressbar.Defaults to 'Loading: '
        left_port (str, optional): left side of progreesbar. Defaults to '|'.
        right_port (str, optional): right side of it. Defaults to '|'.

    Yields:
        int: number of current call
    """

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
def pixel_color(x:int=_MOUSE_X, y:int=_MOUSE_Y) -> tuple:
    """Function to return color of pixel on screen in a tuple of RGB

    Args:
        x (int, optional): screen x position. Defaults to current mouse location
        y (int, optional): screen y position. Defaults to current mouse location

    Returns:
        tuple: RGB tuple of pixel color
    """
    import pyautogui
    if not x:
        x = pyautogui.position()[0]
    if not y:
        y = pyautogui.position()[1]
    PIXEL = pyautogui.screenshot(region=(x, y, 1, 1))
    COLOR = PIXEL.getcolors()
    return COLOR[0][1]


def import_module(path:str) -> ModuleType:
    """Import modules (python code) from given file (even if they are not .py)

    Args:
        path (str): path to the file to import

    Returns:
        ModuleType: returns a module instance of the file
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
def force(tuple_:tuple, *var: Any) -> tuple:
    """Returns given tuple with adding var(s) to the end of it.

    Args:
        tuple_ (tuple): tuple you want to add items to
        *var: variables to add to it

    Returns:
        tuple: given tuple with added given items to it
    """
    return tuple(list(tuple)+[v for v in var])
#force= lambda tpl,*var: tuple(list(tpl)+[v for v in var])


def erase(tuple_:tuple, *var:Any) -> tuple:
    """Returns tuple with removing var(s) from it.

    Args:
        tuple_ (tuple): tuple you want to erase items from

    Returns:
        tuple: given tuple with removed requested items
    """
    #lstv= [v for v in var if v in tpl]
    new_tuple= list(tuple_)
    for th in [v for v in var if v in tuple_]:
        new_tuple.remove(th)
    return tuple(new_tuple)


def replace(tuple_:tuple, index:int, var:Any) -> tuple:
    """replaces tuple[index] with `var`

    Args:
        tuple_ (tuple): tuple to be changed
        index (int): index of item
        var (Any): new value for the given index

    Returns:
        tuple: updated tuple
    """
    tuple_=list(tuple_)
    if type(index) == str:
        index= tuple_.index(index)
    tuple_[index]=var
    return tuple(tuple_)


def insert(tuple_:tuple, index:int, var:Any) -> tuple:
    """Inserts `var` in tuple_[index]

    Args:
        tuple_ (tuple): tuple to be modified
        index (int): index for item to be inserted
        var (Any): value of the item to be added

    Returns:
        tuple: updated tuple
    """
    tuple_=list(tuple_)
    if type(index) == str:
        index= tuple_.index(index)
    tuple_.insert(index,var)
    return tuple(tuple_)


def pop(tuple_:tuple, index=-1) -> tuple:
    """_summary_

    Args:
        tuple_ (tuple): tuple that need to have an item popped
        index (int, optional): index to be popped. Defaults to -1.

    Returns:
        tuple: updated tuple
    """
    return tuple(list(tuple_).pop(index))
