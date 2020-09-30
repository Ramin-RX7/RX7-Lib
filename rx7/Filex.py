'''
Filex Module is Sub-Module of rx7 library.
It contains 2 classes:  
1- files: Static method
2- File: create File object and use its methods.  
(If you are using rx7 module, don't use this and directly use rx7.files and rx7.File)
(Usually I use first one when I need a file only one time in my code  
and use 2nd one when i'm working with a file more than 1 time.)

'''

import os,shutil,subprocess
from typing import Union

class files:
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
                                   '(Use force=True as an argument of remove function to remove non-empty directories.)')               
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
        '''
        if mode:
            os.system("attrib -h "+path)
        else:
            subprocess.check_call(["attrib","+H",path])
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
        op= open(path,mode='r')
        FileR= op.read()
        op.close()
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

