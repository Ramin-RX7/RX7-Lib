'''
This Module is One to Make Your Code Shorter.
High API Will Make You Feel You're Ordering And Machine Is Doing!
Also There is Collection of most usefull function and methods from popular modules of python.
(Read Help of Functions)
Official Documention Will Be Added Soon.
'''
'''
Written By RX
Last Update: 12-01-2020
'''
__version__ = '2.9.0'


# Decorator.attach_to_all in doc!!!  ---  sys.argv  ---  -record.EndError
# (ABC/ABCMeta)?   ---   overload (decorator.overload)

'''
TODO:
 - socket.socket()
 - Error in MEMBERS.all_all_*
 - Screen recorder
 - Make Sound
 - tuple.pop()
 - Tuple methods shouldnt be defined twice
 - style.log_ add time and prefix
 - mp3 tags                                   (v 3.0)
 - registery editor                           (v 3.0)
 - re module                                  (v 3.0)
 - Import of modules startswith _             (v 3.0)
 - Developer:: reload_module -- Check_Type -- add_module_dir
 - Record: save last lap
 - Create Local Server
 - Threading
 - ( win32api.LoadLibrary() - ctypes.PyDLL() )

 - Check 3rd-party modules imports
 - pip install update
 - Open Video
 - Open Audio

 - Ready-obj module
 - !No_Error func
 - !style.COLOR
 - !style defaults
 - {!}time.process_time()
'''




#START

import os
import time
import sys
import subprocess
import abc
import shutil
import random as _RANDOM
import typing as _typing
from typing import Any,Iterable,Optional,Callable,List,Union

import psutil



argv    = sys.argv
ABC     = abc.ABC
ABCMeta = abc.ABCMeta





#######       8888888888                         888    d8b                                  ####### 
####          888                                888    Y8P                                     #### 
####          888                                888                                            #### 
####          8888888 888  888 88888b.   .d8888b 888888 888  .d88b.  88888b.  .d8888b           #### 
####          888     888  888 888 "88b d88P"    888    888 d88""88b 888 "88b 88K               #### 
####          888     888  888 888  888 888      888    888 888  888 888  888 "Y8888b.          #### 
####          888     Y88b 888 888  888 Y88b.    Y88b.  888 Y88..88P 888  888      X88          #### 
#######       888      "Y88888 888  888  "Y8888P  "Y888 888  "Y88P"  888  888  88888P'       ####### 


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
    If You Want to Wait For the User to Press a Key (Keyboard/Mouse)
     Use This Function.
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
    (This function uses threading module so be careful about 
     how, when, and on what object you are going to operate on)
    '''
    import threading
    thread = threading.Thread(target=lambda: (sleep(delay), function(*args)))
    thread.start()
    #keyboard.call_later(function, args, delay)

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

_MOUSE_X = 0
_MOUSE_Y = 0
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

def getpass(prompt):
    '''
    Prompt for a password, with echo turned off.
    '''
    import getpass as Getpass
    return Getpass.getpass(prompt=prompt)
password_input = getpass

def import_module(path):
    '''
    Import modules from files even if they are not .py
    path is path to file to import it
    return module
    '''
    import importlib.machinery
    import importlib.util
    loader = importlib.machinery.SourceFileLoader('MOD', path)
    spec = importlib.util.spec_from_loader(loader.name, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod



######################
#     TUPLE FUNC     #
######################
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

def replace(tpl: tuple, ind, var: Any) -> tuple:
    '''
    (TUPLE FUNCTION)
    Replace tpl[ind] with var
    '''
    tpl=list(tpl)
    if type(ind) == str:
        ind= tpl.index(ind)
    tpl[ind]=var
    return tuple(tpl)

def insert(tpl: tuple, ind, var: Any) -> tuple:
    '''
    (TUPLE FUNCTION)
    Exactly like tpl[ind]=var in lists but for tuples.
    '''
    tpl=list(tpl)
    if type(ind) == str:
        ind= tpl.index(ind)
    tpl.insert(ind,var)
    return tuple(tpl)   

def pop(tuple,index=-1):
    '''
    (TUPLE FUNCTION)
    pop method that is used in lists but for tuples
    '''
    return tuple(list(tuple).pop(index))


"""
 def screen_recorder():
    from screen_recorder_sdk import screen_recorder
    #screen_recorder.enable_dev_log ()
    screen_recorder.disable_log()
    pid = 2456
    screen_recorder.init_resources(pid)
    screen_recorder.start_video_recording ('video1.mp4', 30, 8000000, True)
    time.sleep(10)
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


#from .Filex import *
#from .Tuple_tools import *
#from .RX_obj import *
#from .System import *
#from .Date_Time import *
#from .Lang import Lang as _Lang


class Random:
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
random = Random


class Files:
    '''
    (STATIC METHODS)\n
    Actions and information about files.\n
    (READ FUNCTIONS DOCSTRING)

    GET INFORMATION:
      - exists()
      - size()
      - abspath()
      - mdftime()
      - acstime()
      - content (read function)()
      - is file()
      - is dir()
      - is readonly()
      - is hidden()

    ACTIONS:
      - remove()
      - rename()
      - move()
      - copy()
      - hide()
      - read only()
      - write()
    '''
    @staticmethod
    def size(path):
        '''
        return size of the file in byte(s).
        Also work on directories.
        '''
        return os.path.getsize(path)
        #rooye pooshe emtehan she
    @staticmethod
    def remove(path,force=False):
        '''
        Use this to delete a file or a directory.
        If force is True it will delete non-empty directories.
        '''
        if os.path.isfile(path):
            os.remove(path)
        else:
            if force: 
                shutil.rmtree(path)
            else:
                try:
                    os.rmdir(path)
                except OSError:
                    raise OSError(f"[WinError 145] The directory is not empty: '{path}'" + '\n' + ' '*23 + 
                                   '(Use force=True as an argument of remove function to remove non-empty directories.)') from None
    @staticmethod
    def rename(old_name,new_name):
        '''Rename files with this function.'''
        os.rename(old_name,new_name)
    @staticmethod
    def abspath(path):
        '''
        return absolute path of given path.
        '''
        return os.path.abspath(path)
    @staticmethod
    def exists(path):
        '''
        Search for the file And Returns a boolean.
        if file exists: True
        else: False
        '''
        return os.path.exists(path)
    @staticmethod
    def mdftime(path):
        '''
        Get last modify time of the path.
        '''
        return os.path.getmtime(path)
    @staticmethod
    def acstime(path):    
        '''
        Get last access time of the path.
        '''
        return os.path.getatime(path)
        # change to date bayad biad
    @staticmethod
    def move(src,dst):
        '''
        Move (cut) file/directory from crs to dst.
        '''
        shutil.move(src,dst)
        #live_path= dst
        #Baraye folder hast ya na?
    @staticmethod
    def copy(src,dest,preserve_metadata= True):
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
            shutil.copytree(src,dest)
        else:
            if preserve_metadata: shutil.copy2(src,dest)
            else: shutil.copy(src,dest)

    @staticmethod
    def hide(path,mode=True):
        '''
        Hide file or folder.
        If mode==False: makes 'not hide'
        (ONLY WINDOWS)
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
    def read_only(path,mode=True):
        '''
        Make file attribute read_only.
        If mode==False: makes 'not read_only'
        '''
        if type(mode)==bool:
            from stat import S_IREAD,S_IWUSR
            if mode==True:
                os.chmod(path, S_IREAD)
            elif mode==False:
                os.chmod(path, S_IWUSR)
        else:
            raise Exception('Second argumant (mode) should be boolean.')
    @staticmethod
    def read(path):
        '''
        This can help you to read your file faster.
        Example:
            read('C:\\users\\Jack\\test.txt')
            ==> "Content of 'test.txt' will be shown."
        '''
        with open(path) as f:
            FileR= f.read()
        return FileR
    @staticmethod
    def write(file_path,text=None,mode='replace',start=''):
        '''
        With this method you can change content of the file.  
        file:   File you want to change its content.
        content:   Content you want to add to file.
        mode:   Type of writing method.
             'a' or 'continue' for add content to end of the file. 
             'w' or 'replace'  for overwriting to file content.
        start: I use this when I use mode='continue'
        '''  
        if mode=='replace':
            op= open(file_path,mode='w')
            if text==None:
                text= input('Type what you want.\n\n')
            op.write(text)
            op.close()
        elif mode=='continue':
            '''opr= open(file,mode='r')
            FileR= opr.read()
            op= open(file,mode='w')'''
            op=open(file_path,'a')
            if text==None:
                text= input('Type what you want to add in the end of the file.\n\n')
            op.write(start+text)
            op.close() 
        else:
            raise ValueError('mode can only be: replace(default) or continue Not "{0}"'.format(mode))
    @staticmethod
    def isdir(path):
        return os.path.isdir(path)
    @staticmethod
    def isfile(path):
        return os.path.isfile(path)
    @staticmethod
    def is_readonly(path):
        '''
        Return True if path is readonly else False.
        (May Not Work in Linux)
        '''
        return subprocess.getoutput(f'dir /ar {path} >nul 2>nul && echo True || echo False')
    @staticmethod
    def is_hidden(path):
        """
        Check whether a file is presumed hidden, either because
        the pathname starts with dot or because the platform
        indicates such.
        Return True if File or Directory is hidden.
        (Work on both Linux and Windows)
        """
        import platform
        full_path = os.path.abspath(path)
        name = os.path.basename(full_path)
        def no(path): return False
        platform_hidden = globals().get('is_hidden_' + platform.system(), no)
        return name.startswith('.') or platform_hidden(full_path)
    @staticmethod
    def is_hidden_Windows(path):
        import ctypes
        res = ctypes.windll.kernel32.GetFileAttributesW(path)
        assert res != -1
        return bool(res & 2)
    @staticmethod
    def search_file(pattern, path='.\\',return_mode: Union['list','generator']= 'list'):
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
        import glob
        if str(return_mode).lower() in ('list','generator'):
            if return_mode=='list': return glob.glob(pattern, recursive=True)
            else: return glob.iglob(pattern, recursive=True)
        else:
            if type(return_mode)==str:
                raise ValueError(f"return_mode van be  'list'  or  'generator'  not {return_mode}")
            else:
                raise TypeError(f"return_mode type should be str and it should be in ['list', 'generator']")
    @staticmethod
    def search_content(path,word):
        ALL= [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(path)] for val in sublist]
        '''lst=[]
        for file in ALL:
            if word in rx.read(file):
                lst.append(file)
        return lst'''
        return [file for file in ALL if word in open(file).read()]
    @staticmethod
    def mkdir(path):
        path = os.path.normpath(path)
        NEW= ''
        for FILE in path.split('\\'):
            NEW+= FILE+'\\'
            try: os.mkdir(NEW)
            except (FileExistsError,FileNotFoundError): pass
    @staticmethod
    def generate_tree(dir_path, level: int=-1, limit_to_directories: bool=False,
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
        for line in islice(iterator, length_limit): RETURN+=line+'\n'
        if next(iterator, None): RETURN+=f'... length_limit, {length_limit}, reached, counted:'
        if print_info: RETURN+=f'\n{directories} directories' + (f', {files} files' if files else '')
        return RETURN

    class MEMBERS:
        @staticmethod
        def all_exactdir(dir):
            return os.listdir(dir)
        @staticmethod
        def all_all_sep(dir):
            return [i for i in os.walk(dir)]
        @staticmethod
        def files_exactdir(dir):
            return [i for i in os.walk(dir)][0][2]
        @staticmethod
        def files_all(dir):
            return [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(dir)] for val in sublist]
        @staticmethod
        def files_all_sep(dir):
            return [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(dir)]
        @staticmethod
        def dirs_exactdir(dir):
            return sorted([i for i in os.listdir(dir) if i not in [i for i in os.walk(dir)][0][2]])
        @staticmethod
        def dirs_all(dir):
            return [TPL[0] for TPL in [i for i in os.walk(dir)]]
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
    def accname():
        '''
        return account username you have logged in.
        '''
        return os.getlogin()
    @staticmethod
    def pid():
        '''
        Get pid number of terminal and return it.
        '''
        return os.getpid()
    '''@staticmethod
    def disk_usage(path):
        ####
        return shutil.disk_usage(path)'''
    @staticmethod
    def chdir(path):
        '''
        Change directory of terminal.
        '''
        os.chdir(path)
    @staticmethod
    def SHUT_DOWN():
        '''
        Shut down the PC. (WINDOWS)
        '''
        os.system("shutdown /s /t 1")
    @staticmethod
    def RESTART():
        '''
        Restart the PC. (WINDOWS)
        '''
        os.system("shutdown /r /t 1")
    @staticmethod
    def terminal_size() -> tuple:
        '''
        Return terminal size in tuple (columns,rows)
        '''
        size= os.get_terminal_size()
        return (size.columns,size.lines)
    @staticmethod
    def cwd():
        '''
        Return a unicode string representing the current working directory.
        '''
        return os.getcwd()
    @staticmethod
    def ip_global():
        """
        Return ip with by http://ipinfo.io/ip api.
        returns global ip as string
        """
        try:
            import requests
            new_session = requests.session()
            response = new_session.get("http://ipinfo.io/ip")
            import re
            ip_list = re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", response.text)
            new_session.close()
            return ip_list[0]
        except:
            class ConnectionError(requests.exceptions.ConnectionError):
                def __init__(self, message): super().__init__(message)
            raise ConnectionError('No Internet Connection')
    """ip_global= internet.ip_global"""
    @staticmethod
    def ip_local():
        """
        Return local ip of computer in windows by socket module
        and in unix with hostname command in shell.
        """
        #return [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
        '''
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
            import socket
            ip = socket.gethostbyname(socket.gethostname())
            if ip and ip != "127.0.1.1":
                return ip
            elif platform.system() != "Windows":
                import subprocess
                command = subprocess.Popen(["hostname", "-I"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=False)
                response = list(command.communicate())
                if len(response[0]) > 0:
                    return str(response[0])[2:-4]
                raise NetworkError('No Network Connection')
            raise NetworkError('No Network Connection')
        except:
            raise  
    """ip_local= internet.ip_local"""
    @staticmethod
    def ram_total(convert=True):
        """
        Return total ram of board as string
        parameter convert: flag for convert mode (using of convert_byte function)
        """
        response = list(psutil.virtual_memory())
        if convert:
            return convert_bytes(int(response[0]))
        return str(response[0])
    @staticmethod
    def ram_used(convert=True):
        """
        Return how much ram is using.
        parameter convert: flag for convert mode (convert with convert_byte function)
        """
        response = list(psutil.virtual_memory())
        if convert:
            return convert_bytes(int(response[3]))
        return str(response[3])
    @staticmethod
    def ram_free(convert=True):
        """
        Return how much ram is available.
        parameter convert: flag for convert mode (convert with convert_byte function)
        """
        response = list(psutil.virtual_memory())
        if convert:
            return convert_bytes(int(response[1]))
        return str(response[1])
    @staticmethod
    def ram_percent(ONLY_NOM=False):
        """
        Return available ram percentage as an integer if ONLY_NOM, as string with % if not ONLY_NOM
        Parameter ONLY_NOM: flag for return type and value.
        """
        response = list(psutil.virtual_memory())
        if ONLY_NOM:
            return response[2]    
        return str(response[2]) + " %"
    @staticmethod
    def boot_time():
        '''
        Return the system boot time expressed in seconds since the epoch.
        '''
        return psutil.boot_time()
    @staticmethod
    def device_name():
        import socket
        return socket.gethostname()
    @staticmethod
    def ip_website(url):
        '''get IP address of Web Site'''
        import socket
        return socket.gethostbyname(url)
    """ip_webs= internet.ip_website"""
    @staticmethod
    def win10_notification(title,message,icon=None, duration=5) -> None:
        '''
        (THIS ONLY WORKS FOR "WINDOWS 10")\n
        Display Notification with title, message and icon for speciefic time.
        '''
        try:
            from win10toast import ToastNotifier
            ToastNotifier().show_toast(title,message,duration=duration)
        except:
            raise ImportError('Use "pip install win10toast" to install required module')
    @staticmethod
    def cpu_count(logical=True):
        '''
        Return the number of logical CPUs in the system
         (same as os.cpu_count() in Python 3.4).
        If *logical* is False return the number of physical cores only
         (e.g. hyper thread CPUs are excluded).
        Return None if undetermined.
        '''
        return psutil.cpu_count(logical)
    @staticmethod
    def pyshell_execute_bit():
        '''to determine whether a Python shell is executing in 32bit or 64bit'''
        #return platform.architecture()[0][:2]     # SLOW
        #return ctypes.sizeof(ctypes.c_voidp)*8
        import struct
        return struct.calcsize("P") * 8
    @staticmethod
    def pids() -> list:
        '''Return a list of current running PIDs'''
        return psutil.pids()
    @staticmethod
    def cpu_percent() -> float:
        '''
        Return a float representing the current system-wide CPU utilization as a percentage.'''
        return psutil.cpu_percent()
    @staticmethod
    def pid_exists(pid) -> bool:
        return psutil.pid_exists(pid)
system = System

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
    '''
    def __mul__(self, nom):
        return self.content*nom
    def __getitem__(self, index):
        return f'{fg(self.color)}{bg(self.BG)}{self.text}'+self.content[index]+attr(0)
    '''

    @staticmethod
    def print(text='', color='default', BG='default', style=None, end='\n'):
        '''
        text(text='Hello World',color='red',BG='white')
        output ==> 'Hello World' (With red color and white BG)
        Styles: bold - underline - reverse - hidden
         *bold and underline may not work. (Depends on terminal and OS)
        '''
        try:
            color = color.lower()
            BG = BG.lower()
            style = style.lower()  if style and type(style)==str  else 0
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
    reset = switch_default

    @staticmethod
    def log_success(text, color='green', BG='default', style=None):
        globals()['style'].print(text, color, BG, style=style)
    @staticmethod
    def log_info(text, color='grey_93', BG='default', style=None):
        globals()['style'].print(text, color, BG, style=style)
    @staticmethod
    def log_warning(text, color='gold_3a', BG='default', style=None):
        globals()['style'].print(text, color, BG, style=style)
    @staticmethod
    def log_error(text, color='red', BG='default', style=None):
        globals()['style'].print(text, color, BG, style=style)
    @staticmethod
    def log_critical(text, color='red_1', BG='default', style='bold'):
        globals()['style'].print(text, color, BG, style=style)
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
        self.laps = []
    def __call__(self):
        return f'Laps: {self.laps}'
    def __repr__(self):
        return f'Laps: {self.laps}'

    def lap(self, save=True, Round=15):
        '''
        Return time passed from creating time of self.
        (Read 'record' Doc String)
        If save is True, time will be added to self.laps
        '''        
        lp = time.time() - self.__start
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
            self.__start = time.time()
    def last_lap(self, save=True):
        ret = (self.lap(False)-self.laps[-1]) if self.laps else self.lap(False)
        if save:
            self.laps.append(self.lap())
        return ret
    @staticmethod
    def timit(code,setup,timer,number,globals_):
        import timeit
        return timeit.timeit(code,setup,timer,number,globals_)
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
    
    abstractclassmethod = abc.abstractclassmethod
    abstractmethod = abc.abstractmethod
    abstractstaticmethod = abc.abstractstaticmethod

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


class io:
    
    @staticmethod
    def wait_for_input(prompt,SS:list=[], ignore_case=False):
        answer= ''
        try:
            while not answer:
                answer = input(prompt).strip()
                if ignore_case:
                    answer = answer.lower()
                if answer and SS:
                    if not (answer in (SS if not ignore_case else [item.lower() for item in SS])):
                        style.print('Invalid Input','red')
                        answer = ''
        except (EOFError,KeyboardInterrupt):
            style.print('EXITING...','red')
            exit()
        return answer

    @staticmethod
    def selective_input(prompt,choices,default=None,error=False):
        while True:
            inp = input(prompt)
            if not inp  or  inp not in choices:
                if error:
                    style.print('Invalid input', 'red')
                else:
                    inp = default
                    break
            else:
                break
        return inp
    @staticmethod
    def yesno_input(prompt,default=None):
        error= not bool(default)
        return io.selective_input(prompt,['y','yes','n','no'],default,error)
IO = io


class Types:
    Any         =  _typing.Any
    Callable    =  _typing.Callable
    Container   =  _typing.Container
    Dict        =  _typing.Dict
    Generator   =  _typing.Generator
    Iterable    =  _typing.Iterable
    Iterator    =  _typing.Iterator
    List        =  _typing.List
    Mapping     =  _typing.Mapping
    NamedTuple  =  _typing.NamedTuple
    NoReturn    =  _typing.NoReturn
    Optional    =  _typing.Optional
    OrderedDict =  _typing.OrderedDict
    Set         =  _typing.Set
    Text        =  _typing.Text
    Tuple       =  _typing.Tuple
    Type        =  _typing.Type
types = Types
    
class Tuple:
    '''
    (Note That This is tuple of RX7 Module So it Has More Features!)\n
    (This is Not Built-in immutable sequence.)\n
    If no argument is given, the constructor returns an empty tuple.\n
    There is *var argumant that you can add object as much as you need.\n
    Any Built-in object is accepted. (Not tested on third-party objects.)\n
    Beside built-in features of tuple, this supports:
    + You Can Add objects to your tuple now.
    + Also You Can Delete Them.
    + Replace Them.
    + Like lists, Tuple supports item assigning. ( tpl[2]='hello' )
    (Tuple Unpacking is Supported.)
    '''
    #############################
    def __init__(self,*var: Any, one_item=False):
        if not one_item:
            self.__content= tuple(var)
        else:
            self.__content=[]
            for item in var:
                for member in item:
                    self.__content.append(member)
            self.__content= tuple(self.__content)
    def __str__(self):
        return str(self.__content)
    def __repr__(self):
        return str(self.__content)
    #############################
    #############################
    def add(self,*var: Any):
        '''
        This will add var(s) to self.
        '''
        self.__content= tuple(list(self.__content)+[v for v in var])
        #force= lambda tpl,*var: tuple(list(tpl)+[v for v in var])
    force= add
    def remove(self,*var: Any):
        '''
        It will remove var(s) from self.
        '''
        #lstv= [v for v in var if v in tpl]
        lstt= list(self.__content)
        for th in [v for v in var if v in self.__content]:
            lstt.remove(th)
        self.__content= tuple(lstt)
    erase= remove
    def pop(self,index):
        return pop(self.__content)
    #############################
    #############################
    def replace(self, ind: Union[int,Any], var: Any):
        '''
        Replace self[ind] with var.
        '''
        tpl=list(self.__content)
        if type(ind) == str:
            ind= tpl.index(ind)
        tpl[ind]=var
        self.__content= tuple(tpl)
    def __setitem__(self,index,value,replace=False):
        if not replace:
            tpl=list(self.__content)
            if type(index) == str:
                ind= tpl.index(ind)
            tpl.insert(index,value)
            self.__content= tuple(tpl)            
        else:
            self.replace(index,value)
    def __getitem__(self,index):
        return self.__content[index]
    #############################
    def __add__(self,other):
        return self.__content + other
    def __contains__(self,var):
        return var in self.__content
    #############################
    #############################
    def __bool__(self):
        return bool(len(self.__content))
    def __hash__(self):
        return hash(self.__content)
    def __len__(self):
        return len(self.__content)
    #############################
    #############################


class _Lang:

    class Constant:
        def __new__(cls,*args,array=True):
            cls._init = False
            return super(_Lang.Constant, cls).__new__(cls)
        def __init__(self,*args,array=True):
            '''
            if array:
                self.__members =  args
            else:
                if len(args) > 1:
                    raise ValueError
                self.__members = args[0]
            '''
            self.__members = args
            self._init = True

        def __str__(self):
            #if len(self.__members) > 1:
                return '<'+str(self.__members)[1:-1]+'>'  #‹›
            #return self.__members
        def __repr__(self):
            return '<'+str(self.__members)[1:-1]+'>'

        def __setattr__(self,attr,value):
            if self._init:
                raise AttributeError(f"'Constant' object does not support item assignment")
            else:
                super(_Lang.Constant,self).__setattr__(attr,value)

        def __getitem__(self,index):
            return self.__members[index]
        def __contains__(self,obj):
            return obj in self.__members
        def __bool__(self):
            return bool(len(self.__members))
        '''
        def __hash__(self):
            return hash(self.__members)
        '''
        def __len__(self):
            #if type(self.__members) == tuple:
                return len(self.__members)

        def _dict_getter(self):
            raise AttributeError("Conatant object has no attribute '__dict__'")
            #return {}
        __dict__ = property(_dict_getter)

        def __dir__(self):
            ret = list(super().__dir__())#[:-2]
            ret.remove('_init')
            ret.remove('_dict_getter')
            return ret
    const = Const = constant = Constant


    class Array:
        
        # Sized Array

        __Type_Error = "Array of type '{}' does not accept object with type '{}'"

        def __init__(self,TYPE,*args):
            self.__members = []
            self.__TYPE = TYPE
            self.__TYPE_NAME  = self.__TYPE.__name__
            for obj in args:
                if type(obj) == TYPE:
                    self.__members.append(obj)
                else:
                    raise ValueError(_Lang.Array.__Type_Error.format(self.__TYPE_NAME,type(obj).__name__))
        def __str__(self):
            return '{'+str(self.__members)[1:-1]+'}'  #‹›
        def __repr__(self):
            return '{'+str(self.__members)[1:-1]+'}'


        def __getitem__(self,index):
            return self.__members[index]

        def __contains__(self,obj):
            return obj in self.__members
        def __bool__(self):
            return bool(len(self.__members))

        def __len__(self):
            return len(self.__members)

        def __setitem__(self,index,obj):
            if type(obj) == self.__TYPE:
                self.__members.insert(index,obj)
                return
            raise ValueError(_Lang.Array.__Type_Error.format(self.__TYPE_NAME,type(obj).__name__))
        def insert(self,index,obj):
            if type(obj) == self.__TYPE:
                self.__members.insert(index,obj)
                return
            raise ValueError(_Lang.Array.__Type_Error.format(self.__TYPE_NAME,type(obj).__name__))
        def append(self,obj):
            if type(obj) == self.__TYPE:
                self.__members.append(obj)
                return
            raise ValueError(_Lang.Array.__Type_Error.format(self.__TYPE_NAME,type(obj).__name__))
        add = append
        def remove(self,obj):
            self.__members.remove(obj)
        def pop(self,index=-1):
            self.__members.pop(index)    
    array = Array


#END
