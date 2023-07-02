'''
Actions and information about files.

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

import os as _os
import shutil as _shutil
from typing import Text,Literal,Generator



def size(path:str) -> int:
    '''return size of the file/directory in bytes.'''
    if isdir:
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


def remove(path:str,force:bool=False) -> None:
    '''
    This will delete both a file or directory.
    If `force` is True it will delete non-empty directories.
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


def rename(old_name:str, new_name:str) -> None:
    '''Rename files.'''
    _os.rename(old_name,new_name)


def abspath(path:str) -> str:
    '''return absolute path of given path.'''
    return _os.path.abspath(path)


def exists(path:str) -> bool:
    '''Test whether a path exists'''
    return _os.path.exists(path)


def mdftime(path:str) -> float:
    '''Get last modify time of the path.'''
    return _os.path.getmtime(path)


def acstime(path:str) -> float:
    '''Get last access time of the path.'''
    return _os.path.getatime(path)
    # change to date bayad biad


def move(src:str, dest:str) -> None:
    '''Moves (cuts) file/directory from src to dst.'''
    _shutil.move(src,dest)


def copy(src:str, dest:str, preserve_metadata:bool=True) -> None:
    '''
    Copy the file from src to destination.
    preserve_metadata is for preserving metadata of files when copying.
    '''
    if isdir(src):
        _shutil.copytree(src,dest)
    else:
        if preserve_metadata:
            _shutil.copy2(src,dest)
        else:
            _shutil.copy(src,dest)


def hide(path:str, mode:bool=True) -> None:
    '''
    (WINDOWS ONLY)
    Hide file/folder.
    If mode==False: unhides the file/folder
    '''
    try:
        import win32api, win32con
    except:
        raise ImportError('Please install pywin32 via pip')
    if mode:
        win32api.SetFileAttributes(path,win32con.FILE_ATTRIBUTE_HIDDEN)
    else:
        win32api.SetFileAttributes(path,win32con.FILE_ATTRIBUTE_NORMAL)


def read_only(path:str, mode:bool=True) -> None:
    '''
    Make the given path read_only.
    If mode==False: makes 'not read_only'
    '''
    from stat import S_IREAD,S_IWUSR
    if mode==True:
        _os.chmod(path, S_IREAD)
    elif mode==False:
        _os.chmod(path, S_IWUSR)


def read(file_path:str) -> str:
    '''
    Get content of a file.
    '''
    with open(file_path) as f:
        content = f.read()
    return content


def write(file_path:str, text:Text=None, mode='replace', start='') -> None:
    '''
    Modify content of the given file.
    file:   File you want to change its content.
    text:   Content you want to add to file.
    mode:   Type of writing method.
         'a' or 'continue' for add content to end of the file.
         'w' or 'replace'  for overwriting to file content.
    start: I use this when I use mode='continue'
    '''
    if mode in ("w",'replace'):
        with open(file_path, "w") as f:
            f.write(start+text)
    elif mode in ("a",'continue'):
        with open(file_path, "a") as f:
            f.write(start+text)
    else:
        raise ValueError('mode can only be: replace(default) or continue Not "{0}"'.format(mode))


def isdir(path:str) -> bool:
    """Return true if the pathname refers to an existing directory"""
    return _os.path.isdir(path)


def isfile(path:str):
    """Test whether a path is a regular file"""
    return _os.path.isfile(path)


def is_readonly(path:str):
    '''Return True if path is readonly else False. (May Not Work in Linux)'''
    return  not _os.access(path, _os.R_OK)


def is_hidden(path:str):
    """
    Check whether a file is presumed hidden, either because
    the pathname starts with dot or because the platform
    indicates such.
    Return True if File or Directory is hidden. (Work on both Linux and Windows)
    """
    import platform
    full_path = _os.path.abspath(path)
    name = _os.path.basename(full_path)
    def no(path):
        return False
    platform_hidden = globals().get('is_hidden_' + platform.system(), no)
    return name.startswith('.') or platform_hidden(full_path)


def is_hidden_Windows(path:str):
    """Detemines wether a file is hidden or not."""
    import ctypes
    res = ctypes.windll.kernel32.GetFileAttributesW(path)
    assert res != -1
    return bool(res & 2)


def search_file(pattern:str, path:str='./', return_mode:Literal[list,Generator]=list):
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
        raise ValueError(f"return_mode should be either 'list' or 'Generator'  not {return_mode}")
    import glob
    if return_mode=='list': return glob.glob(_os.path.join(path,pattern), recursive=True)
    else: return glob.iglob(_os.path.join(path,pattern), recursive=True)


def search_content(path:str,word:str):
    """returns list of files in path that includes the given text."""
    ALL= [val for sublist in [[_os.path.join(i[0], j) for j in i[2]] for i in _os.walk(path)] for val in sublist]
    return [file for file in ALL if word in open(file).read()]


def mkdir(path:str):
    """Make directory. Chained path is also accepted"""
    path = _os.path.normpath(path)
    NEW= ''
    for FILE in path.split('/'):
        NEW+= FILE+'/'
        try:
            _os.mkdir(NEW)
        except (FileExistsError,FileNotFoundError):
            pass

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


def get_drives() -> tuple:
    """(WINDOWS ONLY)
    Gets devices and drives in windows
    """
    return (drive for drive in "CDEFGHIJKLMNOPQRSTUVWXYZ" if exists(f"{drive}:/"))


def basename(path:str) -> str:
    """Returns the final component of a pathname"""
    return _os.path.basename(path)


def join_paths(path:str, *paths) -> str:
    """Joins all the given paths together"""
    return _os.path.join(path,*paths)


def dirname(path:str) -> str:
    """Returns the directory component of a pathname"""
    return _os.path.dirname(path)



class MEMBERS:

    def all_exactdir(dir:str):
        return _os.listdir(dir)

    def all_all_sep(dir:str):
        return [i for i in _os.walk(dir)]

    def files_exactdir(dir:str, abspath:bool=True):
        if abspath:
            return [dir+'/'+file_ for file_ in [i for i in _os.walk(dir)][0][2]]
        return [i for i in _os.walk(dir)][0][2]

    def files_all(dir:str):
        return [val for sublist in [[_os.path.join(i[0], j) for j in i[2]] for i in _os.walk(dir)] for val in sublist]

    def files_all_sep(dir:str):
        return [[_os.path.join(i[0], j) for j in i[2]] for i in _os.walk(dir)]

    def dirs_exactdir(dir:str, abspath:str=True):
        if dir.endswith('/'): dir=dir[:-1]
        elif dir.endswith('\\'): dir=dir[:-1]
        if abspath:
            return [dir+'/'+folder for folder in [i for i in _os.walk(dir)][0][1]]
        return [i for i in _os.walk(dir)][0][1]

    def dirs_all(dir:str):
        return [TPL[0] for TPL in [i for i in _os.walk(dir)]]
