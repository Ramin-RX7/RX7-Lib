"""
This Module is One to Make Your Code Shorter.

High API Will Make You Feel You're Ordering And Machine Is Doing!

Also There is Collection of most usefull function and methods from popular modules of python.
(Read Help of Functions)

Official documentation in https://github.com/Ramin-RX7/RX7-Lib
"""
'''
Written By RX
Last Update: 04-28-2022
'''
__version__ = '3.3.0'


"""
< Release Changes >

"""





#START

import os   as _os
import re   as _re
import sys  as _sys
import abc  as _abc
import time as _time
import socket   as _socket
import urllib   as _urllib
import shutil   as _shutil
import random   as _random
import datetime as _datetime
import calendar as _calendar
import subprocess as _subprocess
import platform as _platform
# import requests as _requests
    # imported requests in any method that uses it to improve importing speed
import psutil as _psutil

from functools import wraps
from typing import (Any,Iterable,Optional,Callable,
                    Union,Text,Generator,Literal)







argv    = _sys.argv
ABC     = _abc.ABC
exit = _sys.exit
environ = _os.environ

write = ...
read  = ...
decorator  = ...
Check_Type = ...
overload   = ...
Input   = default_input  = ...
getpass = password_input = ...





#######       8888888888                         888    d8b                                  #######
####          888                                888    Y8P                                     ####
####          888                                888                                            ####
####          8888888 888  888 88888b.   .d8888b 888888 888  .d88b.  88888b.  .d8888b           ####
####          888     888  888 888 "88b d88P"    888    888 d88""88b 888 "88b 88K               ####
####          888     888  888 888  888 888      888    888 888  888 888  888 "Y8888b.          ####
####          888     Y88b 888 888  888 Y88b.    Y88b.  888 Y88..88P 888  888      X88          ####
#######       888      "Y88888 888  888  "Y8888P  "Y888 888  "Y88P"  888  888  88888P'       #######


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


"""
Terminal title in mac: "\033]0;{}\007".format(title)

 def screen_recorder():
    from screen_recorder_sdk import screen_recorder
    #screen_recorder.enable_dev_log ()
    screen_recorder.disable_log()
    pid = 2456
    screen_recorder.init_resources(pid)
    screen_recorder.start_video_recording ('video1.mp4', 30, 8000000, True)
    _time.sleep(10)
    print('hello')
    for i in range(100):
        x= i**3
    screen_recorder.stop_video_recording ()
    screen_recorder.free_resources()

 class Error(Exception):
    '''
    This module is for creating you own Error and Exception!
     Useage:
     >>> MyError = Error(name='MyError', msg='An Error occurred')
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     MyError: An Error occurred

     Also You can raise it directly:
     >>> raise Error(name='MyError', msg='An Error occurred')
     Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
     MyError: An Error occurred

    '''
    def __new__(cls, msg, name=''):
        Error.__name__ = name
        return super(Error, cls).__new__(cls, msg)

    def __init__(self, **kwargs):
        pass

"""





#######        .d8888b.   888  888                                                         #######
####          d88P  Y88b  888  888                                                            ####
####          888    888  888  888                                                            ####
####          888         888  888   8888b.   .d8888b   .d8888b    .d88b.   .d8888b           ####
####          888         888  888      "88b  88K       88K       d8P  Y8b  88K               ####
####          888    888  888  888  .d888888  "Y8888b.  "Y8888b.  88888888  "Y8888b.          ####
####          Y88b  d88P  888  888  888  888       X88       X88  Y8b.           X88          ####
#######        "Y8888P"   888  888  "Y888888   88888P'   88888P'   "Y8888    88888P'       #######



class Random:
    '''
    random Variable Generator Class.
    (ALL FUNCTIONS ARE STATIC METHODS)
    '''

    @staticmethod
    def choose(iterable:Iterable, k:int=1, duplicate=True):
        """
        Return a random element from a non-empty sequence.

        Args:
            iterator (Iterator): The iterator you wanna choose a random member of it
            k (int): number of items to randomly get from iterator
            duplicate (bool): wether or not getting duplicate items (if k>1)

        Returns:
            Any: one of members of iterator if k=1
            List[Any]: if k>1

        Raise:
            ValueError: Occurs when k<1
        """
        if type(k) != int:
            raise TypeError('k must be integer.')

        if k == 1:
            return _random.choice(iterable)
        elif k > 1:
            if duplicate:
                return _random.choices(iterable,k=k)
            else:
                return _random.sample(iterable,k=k)
        else:
            raise ValueError('k Must Be Higher 0')

    @staticmethod
    def integer(first_number:int, last_number:int):
        """
        Return random integer in range [a, b], including both end points.

        Args:
            first_number (int):  a
            last_number  (int):  b

        Return:
            int: a random number in [a, b] range
        """
        return _random.randint(first_number,last_number)

    @staticmethod
    def O1(decimal_number:int = 17):
        """
        Return x in the interval [0, 1)

        Arg:
            decimal_number (int): how many decimal numbers to round

        Return:
            float: random number in interval [0,1)
        """
        return round(_random.random(),decimal_number)

    @staticmethod
    def number(first_number:float, last_number:float):
        """
        Return x in the interval [a, b]

        Args:
            first_number (float):  a
            last_number  (float):  b

        Return:
            flaot: a random number in interval [a, b]
        """
        return _random.uniform(first_number,last_number)

    @staticmethod
    def shuffle(iterable:Iterable):
        """
        Return shuffled version of iterable

        Arg:
            iterable (Iterable): The iterable you want to shuffle it's items

        Return:
            Iterable[Any]: shuffled version of given iterable
        """
        # copied = type(iterable)(iterable)
        # random.shuffle(copied)
        # return copied
        real_type = type(iterable)
        new_iterable = list(iterable)

        _random.shuffle(new_iterable)

        if real_type in (set,tuple):
            return real_type(new_iterable)

        elif real_type == str:
            return ''.join(new_iterable)

        elif real_type == dict:
            return {item:iterable[item] for item in new_iterable}

        else:
            return new_iterable
random = Random



class Files:
    '''
    (STATIC METHODS)\n
    Actions and information about files.\n
    (READ FUNCTIONS DOCSTRING)

    GET INFORMATION:
      - exists
      - size
      - abspath
      - mdftime
      - acstime
      - basename
      - dirname
      - content
      - is_file
      - is_dir
      - is_readonly
      - is_hidden

    ACTIONS:
      - remove
      - rename
      - move
      - copy
      - hide
      - read only
      - write
    '''
    @staticmethod
    def size(path:str) -> int:
        '''
        return size of the file in byte(s).
        Also work on directories.
        '''
        if Files.isdir:
            total_size = 0
            for dirpath, dirnames, filenames in _os.walk(path):
                for f in filenames:
                    fp = _os.path.join(dirpath, f)
                    # skip if it is symbolic link
                    if not _os.path.islink(fp):
                        total_size += _os.path.getsize(fp)
            return total_size
        return _os.path.getsize(path)
        #rooye pooshe emtehan she

    @staticmethod
    def remove(path:str,force:bool=False) -> None:
        '''
        Use this to delete a file or a directory.
        If force is True it will delete non-empty directories.
        '''
        if _os.path.isfile(path):
            _os.remove(path)
        else:
            if force:
                _shutil.rmtree(path)
            else:
                try:
                    _os.rmdir(path)
                except OSError:
                    raise OSError(f"[WinError 145] The directory is not empty: '{path}'" + '\n' + ' '*23 +
                                   '(Use force=True as an argument of remove function to remove non-empty directories.)') from None
    delete = remove

    @staticmethod
    def rename(old_name:str, new_name:str) -> None:
        '''Rename files with this function.'''
        _os.rename(old_name,new_name)

    @staticmethod
    def abspath(path:str) -> str:
        '''
        return absolute path of given path.
        '''
        return _os.path.abspath(path)

    @staticmethod
    def exists(path:str) -> bool:
        '''
        Search for the file And Returns a boolean.
        if file exists: True
        else: False
        '''
        return _os.path.exists(path)

    @staticmethod
    def mdftime(path:str) -> float:
        '''
        Get last modify time of the path.
        '''
        return _os.path.getmtime(path)

    @staticmethod
    def acstime(path:str) -> float:
        '''
        Get last access time of the path.
        '''
        return _os.path.getatime(path)
        # change to date bayad biad

    @staticmethod
    def move(src:str, dest:str) -> None:
        '''
        Move (cut) file/directory from src to dst.
        '''
        _shutil.move(src,dest)
        #live_path= dst
        #works for dirs too or not?

    @staticmethod
    def copy(src:str, dest:str, preserve_metadata:bool=True) -> None:
        '''
        Copy the file from src to destination.
        preserve_metadata is for preserving metadata of file when copying.
        (You can use it instead of rename too.
         e.g:
            copy('D:\\Test.py','E:\\Ali.py')
            (It copies Test.py to E drive and renames it to Ali.py)
         )
        '''
        if files.isdir(src):
            _shutil.copytree(src,dest)
        else:
            if preserve_metadata: _shutil.copy2(src,dest)
            else: _shutil.copy(src,dest)

    @staticmethod
    def hide(path:str, mode:bool=True) -> None:
        '''
        Hide file or folder.
        If mode==False: unhides the file/folder
        (WINDOWS ONLY)
        '''
        try:
            import win32api, win32con
        except:
            raise ImportError('Please install pywin32 via pip')
        if mode:
            win32api.SetFileAttributes(path,win32con.FILE_ATTRIBUTE_HIDDEN)
        else:
            win32api.SetFileAttributes(path,win32con.FILE_ATTRIBUTE_NORMAL)

    @staticmethod
    def read_only(path:str, mode:bool=True) -> None:
        '''
        Make file attribute read_only.
        If mode==False: makes 'not read_only'
        '''
        if type(mode)==bool:
            from stat import S_IREAD,S_IWUSR
            if mode==True:
                _os.chmod(path, S_IREAD)
            elif mode==False:
                _os.chmod(path, S_IWUSR)
        else:
            raise Exception('Second argumant (mode) should be boolean.')

    @staticmethod
    def read(file_path:str) -> str:
        '''
        This can help you to read your file faster.
        Example:
            read('C:\\users\\Jack\\test.txt')
            ==> "Content of 'test.txt' will be shown."
        '''
        with open(file_path) as f:
            FileR= f.read()
        return FileR

    @staticmethod
    def write(file_path:str, text:Text=None, mode='replace', start='') -> None:
        '''
        With this method you can change content of the file.
        file:   File you want to change its content.
        content:   Content you want to add to file.
        mode:   Type of writing method.
             'a' or 'continue' for add content to end of the file.
             'w' or 'replace'  for overwriting to file content.
        start: I use this when I use mode='continue'
        '''
        if mode in ("w",'replace'):
            op= open(file_path,mode='w')
            if text==None:
                text= input('Type what you want.\n\n')
            op.write(text)
            op.close()
        elif mode in ("a",'continue'):
            op=open(file_path,'a')
            if text==None:
                text= input('Type what you want to add in the end of the file.\n\n')
            op.write(text)
            op.close()
        else:
            raise ValueError('mode can only be: replace(default) or continue Not "{0}"'.format(mode))

    @staticmethod
    def isdir(path:str) -> bool:
        return _os.path.isdir(path)

    @staticmethod
    def isfile(path:str):
        return _os.path.isfile(path)

    @staticmethod
    def is_readonly(path:str):
        '''
        Return True if path is readonly else False.
        (May Not Work in Linux)
        '''
        return  not _os.access(path, _os.R_OK)

    @staticmethod
    def is_hidden(path:str):
        """
        Check whether a file is presumed hidden, either because
        the pathname starts with dot or because the platform
        indicates such.
        Return True if File or Directory is hidden.
        (Work on both Linux and Windows)
        """
        import platform
        full_path = _os.path.abspath(path)
        name = _os.path.basename(full_path)
        def no(path): return False
        platform_hidden = globals().get('is_hidden_' + platform.system(), no)
        return name.startswith('.') or platform_hidden(full_path)

    @staticmethod
    def is_hidden_Windows(path:str):
        import ctypes
        res = ctypes.windll.kernel32.GetFileAttributesW(path)
        assert res != -1
        return bool(res & 2)

    @staticmethod
    def search_file(pattern:str, path:str='.\\', return_mode:Literal[list,Generator]=list):
        '''
        Search for files in path.
        Return list or generator.
        pattern:
        -  'x.py'  :    search for 'x.py' in path.
        -  '*.py'  :    search for all files with .py extension in path.
        -  '*.*'   :    search for all files in path
        -  '**/*'  :    search for any file in path and also all sub-directories.
        -  '**/*.py:    search for all python files in path and also sub-directories.
        -  'mydir/**/*.py'   :    search for all python files in path/mydir/ and all of its sub-directories.
        '''
        if return_mode not in (list,Generator):
            raise ValueError(f"return_mode should be either 'list' or 'generator'  not {return_mode}")
        import glob
        #print(_os.path.join(path,pattern))
        if return_mode=='list': return glob.glob(_os.path.join(path,pattern), recursive=True)
        else: return glob.iglob(_os.path.join(path,pattern), recursive=True)

    @staticmethod
    def search_content(path:str,word:str):
        ALL= [val for sublist in [[_os.path.join(i[0], j) for j in i[2]] for i in _os.walk(path)] for val in sublist]
        '''lst=[]
        for file in ALL:
            if word in rx.read(file):
                lst.append(file)
        return lst'''
        return [file for file in ALL if word in open(file).read()]

    @staticmethod
    def mkdir(path:str):
        path = _os.path.normpath(path)
        NEW= ''
        for FILE in path.split('\\'):
            NEW+= FILE+'\\'
            try:
                _os.mkdir(NEW)
            except (FileExistsError,FileNotFoundError):
                pass

    @staticmethod
    def generate_tree(dir_path:str, level: int=-1, limit_to_directories: bool=False,
                      length_limit: int=1000, print_info: bool=True):
        """Given a directory Path object return a visual tree structure"""
        from pathlib import Path
        from itertools import islice
        space= '    '; branch = '│   '; tee= '├── '; last= '└── '
        dir_path = Path(dir_path) # accept string coerceable to Path
        files = 0
        directories = 0
        def inner(dir_path: Path, prefix: str='', level=-1):
            nonlocal files, directories
            if not level:  return # 0, stop iterating
            if limit_to_directories: contents = [d for d in dir_path.iterdir() if d.is_dir()]
            else:  contents = list(dir_path.iterdir())
            pointers = [tee] * (len(contents) - 1) + [last]
            for pointer, path in zip(pointers, contents):
                if path.is_dir():
                    yield prefix + pointer + path.name
                    directories += 1
                    extension = branch if pointer == tee else space
                    yield from inner(path, prefix=prefix+extension, level=level-1)
                elif not limit_to_directories:
                    yield prefix + pointer + path.name
                    files += 1
        RETURN=''
        RETURN+=dir_path.name+'\n'
        iterator = inner(dir_path, level=level)
        for line in islice(iterator, length_limit):
            RETURN+=line+'\n'
        if next(iterator, None):
            RETURN+=f'... length_limit, {length_limit}, reached, counted:'
        if print_info:
            RETURN+=f'\n{directories} directories' + (f', {files} files' if files else '')
        return RETURN

    @staticmethod
    def get_drives() -> tuple:
        """WINDOWS ONLY

        Gets devices and drives in windows
        """
        return (drive for drive in "CDEFGHIJKLMNOPQRSTUVWXYZ" if files.exists(f"{drive}:/"))

    @staticmethod
    def basename(path:str) -> str:
        """Returns the final component of a pathname"""
        return _os.path.basename(path)

    @staticmethod
    def join_paths(path:str, *paths) -> str:
        return _os.path.join(path,*paths)

    @staticmethod
    def dirname(path:str) -> str:
        """Returns the directory component of a pathname"""
        return _os.path.dirname(path)

    class MEMBERS:
        @staticmethod
        def all_exactdir(dir:str):
            return _os.listdir(dir)
        @staticmethod
        def all_all_sep(dir:str):
            return [i for i in _os.walk(dir)]
        @staticmethod
        def files_exactdir(dir:str, abspath:bool=True):
            if abspath:
                return [dir+'/'+file_ for file_ in [i for i in _os.walk(dir)][0][2]]
            return [i for i in _os.walk(dir)][0][2]
        @staticmethod
        def files_all(dir:str):
            return [val for sublist in [[_os.path.join(i[0], j) for j in i[2]] for i in _os.walk(dir)] for val in sublist]
        @staticmethod
        def files_all_sep(dir:str):
            return [[_os.path.join(i[0], j) for j in i[2]] for i in _os.walk(dir)]
        @staticmethod
        def dirs_exactdir(dir:str, abspath:str=True):
            if dir.endswith('/'): dir=dir[:-1]
            elif dir.endswith('\\'): dir=dir[:-1]
            if abspath:
                return [dir+'/'+folder for folder in [i for i in _os.walk(dir)][0][1]]
            return [i for i in _os.walk(dir)][0][1]
        @staticmethod
        def dirs_all(dir:str):
            return [TPL[0] for TPL in [i for i in _os.walk(dir)]]
files = Files
write = files.write
read  = files.read



class System:
    '''
    Some system actions and information.
    - Information about ram, ip, terminal, etc.
    - Some System Actions like Shutdown and Restart
    (ALL FUNCTIONS ARE STATIC METHODS)
    '''
    @staticmethod
    def accname() -> str:
        '''
        return account username you have logged in.
        '''
        return _os.getlogin()
    @staticmethod
    def pid() -> int:
        '''
        Get pid number of terminal and return it.
        '''
        return _os.getpid()
    '''@staticmethod
    def disk_usage(path):
        ####
        return _shutil.disk_usage(path)'''
    @staticmethod
    def chdir(path:str) -> None:
        '''
        Change directory of terminal.
        '''
        _os.chdir(path)
    @staticmethod
    def SHUT_DOWN():
        '''
        Shut down the PC. (WINDOWS)
        '''
        _os.system("shutdown /s /t 1")
    @staticmethod
    def RESTART():
        '''
        Restart the PC. (WINDOWS)
        '''
        _os.system("shutdown /r /t 1")
    @staticmethod
    def terminal_size() -> tuple:
        '''
        Return terminal size in tuple (columns,rows)
        '''
        size= _os.get_terminal_size()
        return (size.columns,size.lines)
    @staticmethod
    def cwd() -> str:
        '''
        Return a unicode string representing the current working directory.
        '''
        return _os.getcwd()
    @staticmethod
    def ip_global() -> str:
        """
        Return ip with by http://ipinfo.io/ip api.
        returns global ip as string
        """
        import requests as _requests
        try:
            new_session = _requests.session()
            response = new_session.get("http://ipinfo.io/ip")
            import re
            ip_list = _re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", response.text)
            new_session.close()
            return ip_list[0]
        except:
            raise ConnectionError('No Internet Connection') from None
    """ip_global= internet.ip_global"""
    @staticmethod
    def ip_local() -> str:
        """
        Return local ip of computer in windows by _socket. module
        and in unix with hostname command in shell.
        """
        #return [l for l in ([ip for ip in _socket.gethostbyname_ex(_socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [_socket._socket.(_socket.AF_INET, _socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
        '''
        s = _socket._socket.(_socket.AF_INET, _socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP
        '''
        import platform
        class NetworkError(Exception):
            pass
        try:
            ip = _socket.gethostbyname(_socket.gethostname())
            if ip and ip != "127.0.1.1":
                return ip
            elif platform.system() != "Windows":
                command = _subprocess.Popen(["hostname", "-I"],stdout=_subprocess.PIPE,stderr=_subprocess.PIPE,stdin=_subprocess.PIPE,shell=False)
                response = list(command.communicate())
                if len(response[0]) > 0:
                    return str(response[0])[2:-4]
                raise NetworkError('No Network Connection')
            raise NetworkError('No Network Connection')
        except:
            raise
    """ip_local= internet.ip_local"""
    @staticmethod
    def ram_total(convert:bool=True) -> str:
        """
        Return total ram of board as string
        parameter convert: flag for convert mode (using of convert_byte function)
        """
        response = list(_psutil.virtual_memory())
        if convert:
            return convert_bytes(int(response[0]))
        return str(response[0])
    @staticmethod
    def ram_used(convert:bool=True) -> str:
        """
        Return how much ram is using.
        parameter convert: flag for convert mode (convert with convert_byte function)
        """
        response = list(_psutil.virtual_memory())
        if convert:
            return convert_bytes(int(response[3]))
        return str(response[3])
    @staticmethod
    def ram_free(convert:bool=True) -> str:
        """
        Return how much ram is available.
        parameter convert: flag for convert mode (convert with convert_byte function)
        """
        response = list(_psutil.virtual_memory())
        if convert:
            return convert_bytes(int(response[1]))
        return str(response[1])
    @staticmethod
    def ram_percent(ONLY_NOM:bool=False) -> str:
        """
        Return available ram percentage as an integer if ONLY_NOM, as string with % if not ONLY_NOM
        Parameter ONLY_NOM: flag for return type and value.
        """
        response = list(_psutil.virtual_memory())
        if ONLY_NOM:
            return response[2]
        return str(response[2]) + " %"
    @staticmethod
    def boot_time() -> str:
        '''
        Return the system boot time expressed in seconds since the epoch.
        '''
        return _psutil.boot_time()
    @staticmethod
    def device_name() -> str:
        return _socket.gethostname()
    @staticmethod
    def ip_website(url:str) -> str:
        '''get IP address of Web Site'''
        return _socket.gethostbyname(url)
    """ip_webs= internet.ip_website"""
    @staticmethod
    def win10_notification(title:str, message:str, icon=None, duration:int=5) -> None:
        '''
        (THIS ONLY WORKS FOR "WINDOWS 10")\n
        Display Notification with title, message and icon for speciefic _time.
        '''
        try:
            from win10toast import ToastNotifier
            ToastNotifier().show_toast(title,message,duration=duration)
        except:
            raise ImportError('Use "pip install win10toast" to install required module')
    @staticmethod
    def cpu_count(logical=True) -> int:
        '''
        Return the number of logical CPUs in the system
         (same as _os.cpu_count() in Python 3.4).
        If *logical* is False return the number of physical cores only
         (e.g. hyper thread CPUs are excluded).
        Return None if undetermined.
        '''
        return _psutil.cpu_count(logical)
    @staticmethod
    def pyshell_execute_bit() -> int:
        '''to determine whether a Python shell is executing in 32bit or 64bit'''
        #return platform.architecture()[0][:2]     # SLOW
        #return ctypes.sizeof(ctypes.c_voidp)*8
        import struct
        return struct.calcsize("P") * 8
    @staticmethod
    def pids() -> list:
        '''Return a list of current running PIDs'''
        return _psutil.pids()
    @staticmethod
    def cpu_percent() -> float:
        '''
        Return a float representing the current system-wide CPU utilization as a percentage.'''
        return _psutil.cpu_percent()
    @staticmethod
    def pid_exists(pid:int) -> bool:
        return _psutil.pid_exists(pid)
    @staticmethod
    def mac_address(formatted:bool=False) -> str:
        import uuid
        mac = uuid.getnode()
        if formatted:
            return ':'.join(['{:02x}'.format((mac >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
        return hex(mac)
    @staticmethod
    def os_name():
        return _platform.system()
system = System



from colored import fg   as  _fg
from colored import bg   as  _bg
from colored import attr as  _attr
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
        if type(other)!=style:
            return self.styled+other
        else:
            return self.styled+other.styled

    from pprint import pprint,pformat

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
    def _log(pre, text, color='', BG='default', style=None, add_time=True):
        #globals()['style'].print(text, color, BG, style=style)
        if add_time:
            NOW = f"[{Style._get_now()}]  "
        else:
            NOW = ""
        Style.print(f"{NOW}{text}", color=color, BG=BG, style=style)
    @staticmethod
    def log_success(text, color='green', BG='default', style=None, add_time=True):
        Style._log("[+]",text,color,BG,style,add_time)
    @staticmethod
    def log_info(text, color='dodger_blue_1', BG='default', style=None, add_time=True):
        Style._log("[*]",text,color,BG,style,add_time)
    @staticmethod
    def log_warning(text, color='gold_3a', BG='default', style=None, add_time=True):
        Style._log("[*]",text,color,BG,style,add_time)
    @staticmethod
    def log_error(text, color='red', BG='default', style=None, add_time=True):
        Style._log("[!]",text,color,BG,style,add_time)
    @staticmethod
    def log_critical(text, color='red_1', BG='default', style='bold', add_time=True):
        Style._log("[!]",text,color,BG,style,add_time)
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
        self.__start = _time.time()
        self.laps = []
    def __call__(self):
        return f'Laps: {self.laps}'
    def __repr__(self):
        return f'Laps: {self.laps}'

    def lap(self, save=True, Round=15) -> float:
        '''
        Return time passed from creating time of self.
        (Read 'record' Doc String)
        If save is True, time will be added to self.laps
        '''
        lp = _time.time() - self.__start
        lp = round(lp,Round)
        if save:
            self.laps.append(lp)
        return lp

    def reset(self, reset_start=False):
        '''
        This will erase self.laps
        If reset_start is True, start time will reset too.
        '''
        self.laps = []
        if reset_start:
            self.__start = _time.time()

    def last_lap(self, save=True):
        '''
        Return time passed from last lap
        (If self.laps is False then from start_time)
        '''
        ret = (self.lap(False)-self.laps[-1]) if self.laps else self.lap(False)
        if save:
            self.laps.append(self.lap())
        return ret

    @staticmethod
    def timer(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            t1 = _time.time()
            result = function(*args, **kwargs)
            t2 = _time.time()
            print(f"{function.__name__} : {t2-t1}")
            return result
        return wrapper

    @staticmethod
    def timeit(code="pass",setup="pass",times=1_000_000,globals_=None):
        '''
        Run the 'code' for 'times' times and return time it needs (all, not once)
        (If you need any initialization for your 'code', put it in setup arg)
        '''
        import timeit
        return timeit.timeit(stmt=code,setup=setup,number=times,globals=globals_)
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

    def clear():
        clear()
terminal = Terminal



class Decorator:

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
         '''
         sig = signature(foo)
         print(str(sig))
         print(str(sig.parameters['b']))
         print(sig.parameters['b'].annotation)
         ####
         sig = signature(foo)
         for param in sig.parameters.values():
             if (param.kind == param.KEYWORD_ONLY and
                             param.default is param.empty):
                 print('Parameter:', param.annotation)
        '''
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

    decorator_all:Callable = None
    @staticmethod
    def attach_to_all(cls):
        import inspect
        for name, method in inspect.getmembers(cls):
            if (not inspect.ismethod(method) and
                not inspect.isfunction(method) ) or (
               inspect.isbuiltin(method)):
                continue
            #print("Decorating function %s" % name)
            setattr(cls, name, Decorator.decorator_all(method))
        return cls

    abstractmethod = _abc.abstractmethod

    _registered_functions = {}  #:Dict[str, Any]
    class _MultiMethod(object):
        def __init__(self, name):
            self.name = name
            self.typemap = {}
        def __call__(self, *args):
            types = tuple(arg.__class__ for arg in args)
            function = self.typemap.get(types)
            if function is None:
                raise TypeError("no match: ",types)
            return function(*args)
        def register(self, types, function):
            self.typemap[types] = function
    def overload(*types):
        def register(function):
            name = function.__name__
            mm = decorator._registered_functions.get(name)
            if mm is None:
                mm = decorator._registered_functions[name] = Decorator._MultiMethod(name)
            mm.register(types, function)
            return mm
        return register
decorator  = Decorator
Check_Type = Decorator.Check_Type
overload   = Decorator.overload



class IO:

    @staticmethod
    def wait_for_input(prompt=""):
        answer= ''
        while not answer:
            answer = input(prompt).strip()
        return answer

    @staticmethod
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

    @staticmethod
    def yesno_input(prompt,default=None):
        error= "Invalid Input" if bool(default) else ""
        def action(inp):
            if inp.lower() in ("yes","y"):
                return True
            elif inp.lower() in ("no","n"):
                return False
        return IO.selective_input(prompt,['y','yes','n','no'],default,True,error,action)

    @staticmethod
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

    @staticmethod
    def getpass(prompt:str="Password: "):
        '''
        Prompt for a password, with echo turned off.
        '''
        import getpass
        return getpass.getpass(prompt=prompt)

    @staticmethod
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
io = IO
Input   = default_input  = io.Input
getpass = password_input = io.getpass



class Internet:

    @staticmethod
    def is_connected(website='http://x.com/'):
        '''
        Check for internet connection with trying to connect to web-site
         ( Maybe you want to know why i used http://x.com/ as default web-site
           The reason is there's no extra code to load
           (compare x.com and google.com html source code)
           And this make it a lot faster for checking.
          )
        '''
        try:
            _urllib.request.urlopen(website)
            return True
        except:
            return False

    @staticmethod
    def connection_checker(func):
        """Decaorator Which Checks Internet Connection before calling a function

        Parameters
        ----------
        func : Function
            function which you are going to check if
             there is internet connection before call it
        """
        def inside(*args,**kwargs):
            if not internet.is_connected():
                raise ConnectionError('No internet connection') from None
            return func(*args,**kwargs)
        return inside


    ip_global = system.ip_global

    @staticmethod
    def ip_local() -> str:
        """
        Return local ip of computer in windows by _socket. module
        and in linux with hostname command in shell.
        """
        #return [l for l in ([ip for ip in _socket.gethostbyname_ex(_socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [_socket._socket.(_socket.AF_INET, _socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
        '''
        s = _socket._socket.(_socket.AF_INET, _socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP
        '''
        import platform
        class NetworkError(Exception):
            def __init__(self, message): super().__init__(message)
        try:
            ip = _socket.gethostbyname(_socket.gethostname())
            if ip and ip not in ("127.0.1.1","127.0.0.1"):
                return ip
            elif platform.system() != "Windows":
                command = _subprocess.Popen(["hostname", "-I"],stdout=_subprocess.PIPE,stderr=_subprocess.PIPE,stdin=_subprocess.PIPE,shell=False)
                response = list(command.communicate())
                if len(response[0]) > 0:
                    return str(response[0])[2:-4]
                raise NetworkError('No Network Connection')
            raise NetworkError('No Network Connection')
        except:
            raise

    @staticmethod
    def url_exists(URL) -> bool:
        '''
        check if url exists (with 'requests' module)
        (NEED HTTP[S])
        '''
        import requests as _requests
        _ReqConErr = _requests.exceptions.ConnectionError
        try:
            request = _requests.get(URL)
        except _ReqConErr:
            raise ConnectionError('No internet connection') from None
        #print(response.status_code < 400)
        if request.status_code == 200:
            return True
        else:
            return False

    @staticmethod
    def ip_website(URL) -> str:
        '''
        get IP address of Web Site\n
        (Without http[s])
        '''
        try:
            return _socket.gethostbyname(URL)
        except _socket.gaierror:
            if internet.is_connected():
                class NotExistsError(Exception):
                    def __init__(self):
                        super().__init__('URL Does Not Exists')
                raise NotExistsError from None
            else:
                raise ConnectionError from None

    @staticmethod
    def url_links(URL) -> list:
        '''
        Get all links that are used in a specifiec url
        (All "a" tags from html source)
        (Needs 'http[s]')
        ''' #html.parser
        import requests as _requests
        _ReqConErr = _requests.exceptions.ConnectionError
        try:
            from bs4 import BeautifulSoup
            soup= BeautifulSoup(_requests.get(URL).text,features="lxml")
            LINKS= []
            for link in soup.find_all('a'):
                LINKS.append(link.get('href'))
            return LINKS
        except _ReqConErr:
            raise ConnectionError('No internet connection') from None

    @staticmethod
    def find_urls(string) -> list:
        '''
        find all urls in a string and returns list of them
         (urls should start with http[s])
        '''
        url = _re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
        return url

    @staticmethod
    def is_url(URL) -> bool:
        '''
        check if a string is url (WITH HTTP[S])
        '''
        search= _re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', URL)
        '(http[s]?://)?([Ww]{3}\.)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        if search and len(search.group())==len(URL):
            return True
        else:
            return False

    @staticmethod
    def open_browser(url,new_tab=True):
        import webbrowser
        if new_tab:
            webbrowser.open_new_tab(url)
        else:
            webbrowser.open(url)

    """
    @staticmethod
    def whois(URL):
        '''
         return whois lookup of a website
         (WITHOUT HTTPS)
        '''
        try:
            import whois
            WHO = whois.query(URL)
            WHOIS = WHO.dict
            return {i:WHOIS[i] for i in WHOIS}
        except _socket.gaierror:
            raise ConnectionError('No internet connection') from None
    """
internet = Internet



class DateTime:

    _NOW=        0
    _NOW_YEAR=   0
    _NOW_MONTH=  0
    _NOW_DAY=    0
    _NOW_HOUR=   -1
    _NOW_MINUTE= -1
    _NOW_SECOND= -1
    def NOW():
        _NOW= _time.localtime()
        _NOW_YEAR= _NOW.tm_year
        _NOW_MONTH= _NOW.tm_mon
        _NOW_DAY= _NOW.tm_mday
        _NOW_HOUR= _NOW.tm_hour
        _NOW_MINUTE= _NOW.tm_min
        _NOW_SECOND= _NOW.tm_sec
        return _datetime.datetime(_NOW_YEAR,_NOW_MONTH,_NOW_DAY,_NOW_HOUR,_NOW_MINUTE,_NOW_SECOND)
    now = NOW
    def normalize(date=[],time=[]):
        now = date_time.NOW()
        try:
            if not date[0]:  date[0]= now.year
            if type(date[1]) == str:
                try:
                    date[1]= date_time.month_dic[date[1].lower()]
                except KeyError:
                    raise ValueError("Wrong Month Name") from None
            if not date[1]:  date[1]= now.month
            if not date[2]:  date[2]= now.day
        except IndexError:
            pass
        try:
            if time[0]<0: now.hour
            if time[1]<0: now.minute
            if time[2]<0: now.second
        except IndexError:
            pass
        return [date,time]
    Weekday_Names= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    month_lst= ['january','february','march','april','may','june',
                'july','august','september','october','november','december']
    month_dic= {month:month_nom for month in month_lst for month_nom in range(1,13)}

    def __init__(self,year=_NOW_YEAR,month=_NOW_MONTH,day=_NOW_DAY,hour=_NOW_HOUR,minute=_NOW_MINUTE,second=_NOW_SECOND,first_week_day=0):
        '''
        .: Working With Date and Time :.
        - Include Both Static Methods and Class Methods
        - Get NOW Time
        - Show in Calendar
        - Next and Previous Months in Calendar
        - Determine Time Passed From Specific Date
        - Calendar Supports Setting First Day of the Week
        '''

        """
        Now = date_time.NOW()
         if not year :  year=Now.year
         if not month:  month=Now.month
         if not day  :  day=Now.day
         if hour<0   :  hour=Now.hour
         if minute<0 :  minute=Now.minute
         if second<0 :  second=Now.second
         """
        _norm = date_time.normalize([year,month,day],[hour,minute,second])
        year,month,day = _norm[0]
        hour,minute,second = _norm[1]

        if type(month)==str:
            try:
                month= date_time.month_dic[month.lower()]
            except KeyError:
                raise ValueError("Wrong Month Name") from None

        self.date= _datetime.date(year,month,day)
        self.year=year; self.month=month; self.day=day
        self.time= (hour,minute,second)
        self.hour=hour; self.minute=minute; self.second=second

        self.weekday= date_time.get_weekday(self.year,self.month,self.day)
        self.weekday_name= date_time.get_weekday(self.year,self.month,self.day,True)
        self.week_nom= date_time.get_weeknom(self.year,self.month,self.day)

        #self.first_week_day= first_week_day
        _calendar.setfirstweekday(first_week_day)
        self.calendar= str(_calendar.month(year, month)).replace(str(day),style(str(day),'green').styled)
        self.calendar_month= str(_calendar.month(year, month))
        self.calendar_year_all=str(_calendar.calendar(year))
        self.calendar_year= [_calendar.month(year,i) for i in range(1,13)]
        self.calendar_next_all= [_calendar.month(year,i) for i in range(self.month+1,13)]
        self.calendar_prev_all= [_calendar.month(year,i) for i in range(1,self.month)]
        self.calendar_position_next_year= str(_calendar.month(year+1, month)).replace(str(day),style(str(day),'green').styled)
        self.calendar_position_prev_year= str(_calendar.month(year-1, month)).replace(str(day),style(str(day),'green').styled)

    def setfirstweekday(self,day):
        if type(day)==int and day<7:
            date_time.Weekday_Names= date_time.Weekday_Names[day:]+date_time.Weekday_Names[:day]
        elif type(day)==str:
            day= date_time.Weekday_Names.index(day)
            date_time.Weekday_Names= date_time.Weekday_Names[day:]+date_time.Weekday_Names[:day]
        else:
            if type(day)==int:
                raise ValueError('Invalid Nomber. Day number should be in range(7)')
            else:
                raise TypeError(f"Inappropriate Type For 'day'.  day can be 'str' or 'int' not {type(day)}")
        _calendar.setfirstweekday(day)
        self.calendar= str(_calendar.month(self.year, self.month)).replace(str(day),style(str(day),'green').styled)
        self.calendar_month= str(_calendar.month(self.year, self.month))
        self.calendar_year_all=str(_calendar.calendar(self.year))
        self.calendar_year= [_calendar.month(self.year,i) for i in range(1,13)]
        self.calendar_next_all= [_calendar.month(self.year,i) for i in range(self.month+1,13)]
        self.calendar_prev_all= [_calendar.month(self.year,i) for i in range(1,self.month)]
        self.calendar_position_next_year= str(_calendar.month(self.year+1, self.month)).replace(str(day),style(str(day),'green').styled)
        self.calendar_position_prev_year= str(_calendar.month(self.year-1, self.month)).replace(str(day),style(str(day),'green').styled)

        self.weekday= date_time.get_weekday(self.year,self.month,self.day)
        self.weekday_name= date_time.get_weekday(self.year,self.month,self.day,True)
        self.week_nom= date_time.get_weeknom(self.year,self.month,self.day)

    @staticmethod
    def today():
        dt = date_time.NOW()
        return (dt.year,dt.month,dt.day)
    @staticmethod
    def calender_year(year=_NOW_YEAR):
        if not year: year=date_time.NOW().year
        return [_calendar.month(year,i) for i in range(1,13)]
    @staticmethod
    def calendar_month_st(month=_NOW_MONTH,year=_NOW_YEAR,day=0):
        year,month = date_time.normalize([year,month])[0]

        if not day:
            return str(_calendar.month(year, month))
        else:
            return str(_calendar.month(year, month)).replace(str(day),style(str(day),'green').styled)
    @staticmethod
    def passed_date(f_date,l_date=_NOW,return_time='day'):
        if not l_date: l_date=date_time.NOW()
        f_date = _datetime.datetime(*f_date)
        return_time= return_time.lower()
        if return_time in ('day','month','year','hour','minute','second'):
            DELTA=  l_date - f_date
            if return_time == 'year':
                try:
                    _return = _re.search(r'(?P<X>(-)?\w+) day',str(DELTA/365)).group('X')
                except:
                    _return = None
                #_return = str(DELTA/365)
            elif return_time == 'month':
                _return = _re.search(r'\w+',str(DELTA/30)).group()
            elif return_time == 'day':
                _return = str(DELTA)[:-14]
            elif return_time =='hour':
                _return = str(DELTA*24)[:-14]
            elif return_time == 'minute':
                _return = str(DELTA*1440)[:-14]
            elif return_time == 'second':
                _return = str(DELTA*3600)[:-14]

            if _return:  return _return
            else: return 0
        else:
            raise ValueError("return_time should be in  ('year', 'month', 'day', 'hour', 'minute', 'second')")
    passed_time = passed_date
    '''@staticmethod
     def passed_time(year=1970,month=1,day=1,hour=0,minute=0,second=0,return_time='second'):
        pass'''
    @staticmethod
    def convert_epoch_to_local(second=_time.time()):
        return _time.ctime(second)
    @staticmethod
    def get_weekday(year=_NOW_YEAR,month=_NOW_MONTH,day=_NOW_DAY,return_name=False):
        """
        First day is Monday and the numbers starts from 0
        """
        year,month,day = date_time.normalize([year,month,day])[0]
        if return_name:
            return date_time.Weekday_Names[_datetime.date(year,month,day).weekday()]
        else:
            return _datetime.date(year,month,day).weekday()
    @staticmethod
    def get_weeknom(year=_NOW_YEAR,month=_NOW_MONTH,day=_NOW_DAY):
        """
        Returns 53 if First week is from last year
        """
        year,month,day = date_time.normalize([year,month,day])[0]
        return _datetime.date(year,month,day).isocalendar()[1]
    @staticmethod
    def calendar_show_week(week_nom,year=_NOW_YEAR):
        year = date_time.normalize([year])[0][0]
        week= week_nom
        for i in list(range(1,8))[::-1]:
            if date_time.get_weeknom(year,1,i)==1:
                FIRST_WEEK_DAYS= len(list(range(i)))
                break

        day= (week-1)*7 - (6-FIRST_WEEK_DAYS)
        mnth= 1
        true=False
        while not true:
            try:
                if _calendar.monthrange(year,mnth)[1]<day:
                    mnth+=1
                    day-= _calendar.monthrange(year,mnth)[1]
                else:
                    true= True
            except _calendar.IllegalMonthError:
                class BadWeekNumber(Exception):
                    def __init__(self, message='Week Number is Higher Than Year Weeks.'): super().__init__(message)
                raise BadWeekNumber from None
        new= date_time(year,mnth,day)

        cal= new.calendar_month.splitlines()
        for item in cal:
            if str(new.day) in item and item != cal[0]:
                INDEX= cal.index(item);COLORED_WEEK= style(item,'green');break

        WEEK_WITH_COLOR= '\n'.join(cal[:INDEX]+[str(COLORED_WEEK)]+cal[INDEX+1:])
        return WEEK_WITH_COLOR
    @staticmethod
    def get_year():
        return _time.localtime().tm_year
    @staticmethod
    def get_month():
        return _time.localtime().tm_mon
    @staticmethod
    def get_day_of_month():
        return _time.localtime().tm_mday
    @staticmethod
    def get_day_of_week():
        return _time.localtime().tm_wday
    @staticmethod
    def get_day_of_year():
        return _time.localtime().tm_yday
    @staticmethod
    def get_hour():
        return _time.localtime().tm_hour
    @staticmethod
    def get_minute():
        return _time.localtime().tm_min
    @staticmethod
    def get_second():
        return _time.localtime().tm_sec
date_time = datetime = DateTime



'''
class Developer:

    @staticmethod
    def reload(module):
        import importlib
        importlib.reload(module)
    @staticmethod
    def add_module_dir(path:str):
        _sys.path.append(path)
    @staticmethod
    def path():
        return _sys.path
    @staticmethod
    def python_version(sep=False):
        if sep:
            return _platform.python_version_tuple()
        return _platform.python_version()
    def run_path(path):
        import runpy
        return runpy.runpath(path)

'''
#END
