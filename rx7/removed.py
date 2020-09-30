

class File:
    '''
    (CLASS METHODS)
    Actions and Information about files and directories.
    (READ METHODS DOCSTRING)
     if path exists:
         --  self.size - self.abspath - self.acstime - self.mdftime
     if path type is file:
         --  self.content
     if path type is directory:
         --  self.MEMBERS.LIST group (7 Attributes)  with high API (self.MEMBERS.TYPE_PATH)

     METHODS: 
     - copy
     - move
     - rename
     - hide
     - delete
     - read_only
    '''
    def __init__(self,path):
        self.path=    path
        self.live_path= path
        self.size=    None
        self.abspath= None
        self.acstime= None
        self.mdftime= None
        #self.content= None
        if files.exists(path):
            self.size= files.size(path)
            self.abspath= files.abspath(path)
            self.acstime= files.acstime(path)
            self.mdftime= files.mdftime(path)
            #if __import__('platform').system()=='Windows':
            self.hidden= files.is_hidden(path)
            if os.path.isfile(path):
                self.type= 'file'
                self.content= files.read(path)
                if __import__('platform').system()=='Windows':
                 self.readonly= files.is_readonly(path)
                else: self.readonly= 'UNKNOWN'
                self.basename= os.path.basename(path).split('.')
                try: self.ext= self.basename[1]
                except: self.ext= None
             
            if os.path.isdir(path):
                self.type='dir'                
                #walk= os.walk(path)

                class __MMEMBERS:
                    def __init__(self,all_exactdir,all_all_sep,files_exactdir,files_all,files_all_sep,dirs_exactdir,dirs_all):
                        self.all_exactdir= all_exactdir
                        self.all_all_sep= all_all_sep
                        self.files_exactdir= files_exactdir
                        self.files_all= files_all
                        self.files_all_sep= files_all_sep
                        self.dirs_exactdir= dirs_exactdir
                        self.dirs_all= dirs_all

                self.MEMBERS= __MMEMBERS(
                    os.listdir(path),
                    [i for i in os.walk(path)],                 
                    [i for i in os.walk(path)][0][2],
                    [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(path)] for val in sublist],
                    [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(path)],
                    sorted([i for i in os.listdir(path) if i not in [i for i in os.walk(path)][0][2]]),
                    [TPL[0] for TPL in [i for i in os.walk(path)]])

                self.tree= File.__tree2(self.path)
                self.tree_dirs= File.__tree2(self.path,limit_to_directories=True)

             
    def delete(self):
        '''
        Use this to delete  self.
        '''
        files.remove(self.path)
    def rename(self,new_name):
        '''
        Rename self with this function.
        '''
        os.rename(self.path,new_name)
    def move(self,dst):
        '''
        Move (cut) self from crs to dst.
        '''
        shutil.move(self.path,dst)
        self.live_path= dst
        #Baraye folder hast ya na?
    def copy(self,dst):
        '''
        Copy the file from src to destination.
        (You can use it instead of rename too.
         e.g:
            copy('D:\\Test.py','E:\\New.py')
            (It copies Test.py to E drive and renames it to New.py)
         )
        '''
        files.copy(self.path,dst)
    def hide(self,mode=True):
        '''
        Hide file or folder.
        If mode==False: makes 'not hide'
        '''
        files.hide(self.path,mode)
    def read_only(self,mode=True):
        '''
        Make file attribute read_only.
        If mode==False: makes 'not read_only'
        '''
        files.read_only(self.path,mode)

    @staticmethod
    def __tree2(path, level: int=-1, limit_to_directories: bool=False,
            length_limit: int=1000, print_info: bool=True):
        """Given a directory Path object print a visual tree structure"""
        from pathlib import Path
        from itertools import islice
        space =  '    '; branch = '│   '; tee =    '├── '; last =   '└── '
        #dir_path= self.path
        dir_path= path
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

# file table html
'''
 <h3>&nbsp; &nbsp; object File:<strong>&nbsp;</strong><em>Actions and information about files.</em></h3>
 <table style="height: 653px; margin-left: 45px;" width="545" cellpadding="5px">
 <tbody>
 <tr>
 <td style="width: 193px;">__init__(self,path)</td>
 <td style="width: 357px;">Creating file object.</td>
 </tr>
 <tr>
 <td style="width: 193px;">self.size</td>
 <td style="width: 357px;">
 <div>
 <div>size&nbsp;of&nbsp;the&nbsp;file&nbsp;in&nbsp;byte(s).&nbsp;Also&nbsp;work&nbsp;on&nbsp;directories.</div>
 </div>
 </td>
 </tr>
 <tr>
 <td style="width: 193px;">self.abspath</td>
 <td style="width: 357px;">
 <div>
 <div>Return&nbsp;absolute&nbsp;path&nbsp;of&nbsp;given&nbsp;path.</div>
 </div>
 </td>
 </tr>
 <tr>
 <td style="width: 193px;">self.exists</td>
 <td style="width: 357px;">Return Boolean. If exists True, else: False</td>
 </tr>
 <tr>
 <td style="width: 193px;">self.mdftime</td>
 <td style="width: 357px;">
 <div>
 <div>Get&nbsp;last&nbsp;modify&nbsp;time&nbsp;of&nbsp;the&nbsp;file.</div>
 </div>
 </td>
 </tr>
 <tr>
 <td style="width: 193px;">self.acstime</td>
 <td style="width: 357px;">
 <div>
 <div>Get&nbsp;last&nbsp;access&nbsp;time&nbsp;of&nbsp;the&nbsp;file.</div>
 </div>
 </td>
 </tr>
 <tr>
 <td style="width: 193px;">self.type</td>
 <td style="width: 357px;">
 <div>
 <div>'file' for files and 'dir' for directories.</div>
 </div>
 </td>
 </tr>
 <tr>
 <td style="width: 193px;">self.delete()</td>
 <td style="width: 357px;">
 <div>
 <div>Use&nbsp;this&nbsp;to&nbsp;delete file or folder.</div>
 </div>
 </td>
 </tr>
 <tr>
 <td style="width: 193px;">self.rename(new_name)</td>
 <td style="width: 357px;">
 <div>
 <div>Rename&nbsp;file with&nbsp;this&nbsp;method.</div>
 </div>
 </td>
 </tr>
 <tr>
 <td style="width: 193px;">self.move(dst)</td>
 <td style="width: 357px;">Move file from path to dst. (Read Doc String of copy func)</td>
 </tr>
 <tr>
 <td style="width: 193px;">self.copy(dst)</td>
 <td style="width: 357px;">Copy file from self.path to dst. (Also you can use it as rename)</td>
 </tr>
 <tr>
 <td style="width: 193px;">self.hide(path)</td>
 <td style="width: 357px;">Hide given path. (It can be file or directory.)</td>
 </tr>
 <tr>
 <td style="width: 193px;">self.read_only(mode=True)</td>
 <td style="width: 357px;">Make file or folder read-only. (Read Doc String)</td>
 </tr>
 <tr>
 <td style="width: 193px;">self.content&nbsp;&nbsp;(only for files)</td>
 <td style="width: 357px;">If self.type=='file': content is files.read(self.path)</td>
 </tr>
 <tr>
 <td style="width: 193px;">self.basename&nbsp;&nbsp;(only for files)</td>
 <td style="width: 357px;">Basename of file (e.g: C:/Users/file.txt ==&gt; file.txt)&nbsp;</td>
 </tr>
 <tr>
 <td style="width: 193px;">self.ext&nbsp;&nbsp;(only for files)</td>
 <td style="width: 357px;">Returns File extension if it has else None</td>
 </tr>
 <tr>
 <td style="width: 193px;">&nbsp;</td>
 <td style="width: 357px;">&nbsp;</td>
 </tr>
 <tr>
 <td style="width: 193px;">&nbsp; &nbsp;&nbsp;<strong>if self.path is dir</strong></td>
 <td style="width: 357px;">&nbsp;</td>
 </tr>
 <tr>
 <td style="width: 193px;">self.tree</td>
 <td style="width: 357px;">String which presents visual tree from path to the end.</td>
 </tr>
 <tr>
 <td style="width: 193px;">self.tree_dirs</td>
 <td style="width: 357px;">String which presents visual tree from path to the end. (Only directories)</td>
 </tr>
 <tr>
 <td style="width: 193px;">self.MEMBERS.
 <div>
 <div><strong>all</strong>_<strong>exactdir</strong></div>
 </div>
 </td>
 <td style="width: 357px;">List of <strong>all</strong>&nbsp;things those are in <strong>exact directory</strong></td>
 </tr>
 <tr>
 <td style="width: 193px;">
 <div>
 <div>self.MEMBERS.<strong>files</strong>_<strong>exactdir</strong></div>
 </div>
 </td>
 <td style="width: 357px;">List of <strong>files</strong> which are in <strong>exact directory</strong></td>
 </tr>
 <tr>
 <td style="width: 193px;">
 <div>
 <div>
 <div>
 <div>self.MEMBERS.<strong>dirs</strong>_<strong>exactdir</strong></div>
 </div>
 </div>
 </div>
 </td>
 <td style="width: 357px;">List of <strong>dirs</strong>&nbsp; which are in <strong>exact directory</strong></td>
 </tr>
 <tr>
 <td style="width: 193px;">self.MEMBERS.<strong>files</strong>_<strong>all</strong></td>
 <td style="width: 357px;">List of <strong>files</strong>&nbsp;which are in <strong>exact directory </strong>and<strong> all sub-directories</strong></td>
 </tr>
 <tr>
 <td style="width: 193px;">
 <div>
 <div>
 <div>
 <div>self.MEMBERS.
 <div>
 <div><strong>files</strong>_<strong>all</strong>_<strong>sep</strong></div>
 </div>
 </div>
 </div>
 </div>
 </div>
 </td>
 <td style="width: 357px;">List of <strong>files</strong>&nbsp;which are in <strong>exact directory </strong>and<strong> all sub-directories&nbsp;</strong>seprated by their directories</td>
 </tr>
 <tr>
 <td style="width: 193px;">
 <div>
 <div>
 <div>
 <div>self.MEMBERS.<strong>dirs</strong>_<strong>all</strong></div>
 </div>
 </div>
 </div>
 </td>
 <td style="width: 357px;">List of&nbsp;<strong>directories</strong> (<strong>Exact dir</strong> and <strong>all sub-dirs</strong>)&nbsp;</td>
 </tr>
 <tr>
 <td style="width: 193px;">self.MEMBERS.<strong>all_all_sep</strong></td>
 <td style="width: 357px;">List&nbsp; of <strong>all</strong> things in path (<strong>exact dir &amp; sub-dirs</strong>)</td>
 </tr>
 </tbody>
 </table>
 <p>&nbsp;</p>
'''



'''
This Module includes rx7_object.
This object exists in rx7 module so I recommend to use  rx7.RX7_obj  
instead of  rx7.rx_obj.RX7_obj  to ease.
'''
############################################
#############  RX7 OBJECT  #################
############################################
class RX7_obj:
    '''
    This class creates an Iterable that can only contains string.  
    You Can Lock this object (with self.lock() method) 
    which means you can not add remove or set item to it 
    (Usually we use these things in game developing).  
    When Object is locked you can not delete it.  
    Using forbidden methods when object is locked cause LockError 
    and you need to use self.unlock() to unlock.  
    Also RX7_obj include other iterable features like __add__,__sub__,__getitem__,__setitem__,etc.  
    + Custom Representing.
    '''
 #######################
 #####  Existence  #####
 #######################
    def __init__(self,*var):
        for item in var:
            if type(item)!=str:
                raise TypeError
        self.name= self
        self.__MAIN=list(var)
        self.ND= set(var)
        self.__LOCK= False
        self.lock_error= True
        #import sys
        #self.__size= sys.getsizeof(self)
    def __str__(self):
        return '<'+','.join(self.__MAIN)+'>'
    def __repr__ (self):
        #if not self.__LOCK:
            return '<'+','.join(self.__MAIN)+'>'
        #else:
        #    raise self.LockError('Object is Locked. Content Is Protected.')
 ########################
 ########  LOCK  ########
 ########################
    class LockError(Exception):
        def __init__(self, message='Object is Locked. Use Object.unlock() to unlock it.'):
            super().__init__(message)
    def lock(self):
        '''Lock the object.  
        In Locked mode you can not add,remove or delete object.'''
        self.__LOCK= True
    def unlock(self):
        '''Unlock the object so you can add or remove sth and delete the object'''
        self.__LOCK= False
 ######  LUCKABLE  ######
    def add(self,var):
        '''Add var to the object.  
        raise LockError if object is locked.'''
        if not self.__LOCK:
            self.__MAIN.append(var)
            self.ND= set(self.__MAIN)
        else:
            if self.lock_error:
                raise self.LockError
    def remove(self,*var,warning=False,raise_error=False):
        '''Removes var from the object.  
        raise LockError if object is locked.'''
        if not self.__LOCK:
            if raise_error:
                for th in [v for v in var]:
                    if th in self.__MAIN:
                        self.__MAIN.remove(th)
                    else:
                        raise ValueError
            elif warning:
                for th in [v for v in var]:
                    if th in self.__MAIN:
                        self.__MAIN.remove(th)
                    else:
                        print(f'WARNING:  {th} Not in {self}')
            else:
                for th in [v for v in var if v in self.__MAIN]:
                    self.__MAIN.remove(th)
            self.ND= set(self.__MAIN)
        else:
            if self.lock_error:
                raise self.LockError

    def __setitem__(self,index,value):
        if not self.__LOCK:
            if type(value)==str:
                self.__MAIN[index]=value
                self.ND= set(self.__MAIN)
            else:
                raise TypeError
        else:
            if self.lock_error:
                raise self.LockError
    
    def __del__(self):
        '''This will raise LockError if object is locked.
           EVEN IF lock_error IS FALSE'''
        if self.__LOCK:
            raise self.LockError        
 ######################
 ######################
    def __add__(self,other,duplicate=True):
        if not self.__LOCK:
            NEW= RX7_obj(self.__MAIN[0]) 
            for item in self.__MAIN[1:len(self.__MAIN)]:
                NEW.add(item)
            for item in other.__MAIN:
                NEW.add(item)
            if not duplicate:
                NEW.__MAIN=list(set(NEW.__MAIN))
            return NEW
        else:
            if self.lock_error:
                raise self.LockError            
    def __sub__(self,other):
        if not self.__LOCK:
            for item in self.__MAIN:
                if item not in other.__MAIN:
                    NEW= RX7_obj(item)
                    break
            for item in self.__MAIN:
                if item not in other.__MAIN:
                    NEW.add(item)
            NEW.remove(NEW[0])
            return NEW
        else:
            if self.lock_error:
                raise self.LockError
    def __len__(self):
        return len(self.__MAIN)
    def __getitem__(self,index):
        return self.__MAIN[index]
    def __bool__(self):
        bool(len(self.__MAIN))
    '''def __call__(self):
        if not self.__LOCK:'''
    def __sizeof__(self):
        return (self.__MAIN.__sizeof__(),self.ND.__sizeof__()) #self.__size,

# rxobj table html
'''
 <h3>&nbsp; &nbsp; &nbsp;object RX_obj:<strong>&nbsp;</strong><em>It's an object with so many featues. (More features in upcoming updates!)</em></h3>
 <h4>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Description:</h4>
 <p><em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</em>It's a kind of object that I will improve it in upcoming updates (If only you guys like it).</p>
 <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;You can use: <strong><em>MyCustomName= rx.RX_obj</em>&nbsp;&nbsp;</strong>so you can access it easier.</p>
 <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;One special feature it has is 'lock'. When you lock the object you can't add or remove anything to it. Also You can not delete it! Doing these will raise LockError.</p>
 <p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;using <em><strong>self.lock_error= False</strong>&nbsp;</em> can stop raising error when adding or removing (Not deleting) (But it doesn't mean it will add things to it. It just ignores errors)</p>
 <h4>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Supports:<em>&nbsp; &nbsp;indexing - len - hash&nbsp; - bool - __add__ - __sub__ - <span style="text-decoration: underline;">lock</span>&nbsp;</em></h4>
 <table style="margin-left: 50px;">
 <tbody>
 <tr>
 <td><strong>RX_obj(*var,one=False)</strong></td>
 <td><strong>Create RX_obj object with *var members</strong></td>
 </tr>
 <tr>
 <td>self.ND</td>
 <td>self members without duplicate. (set of self members)</td>
 </tr>
 <tr>
 <td>self.lock()</td>
 <td>Make self locked (You can not add or remove. You can't delete self)</td>
 </tr>
 <tr>
 <td>self.unlock()</td>
 <td>Unlock self</td>
 </tr>
 <tr>
 <td>self.lock_error= True</td>
 <td>(boolean) If self.lock_error is False, It doesn't raise error when adding or removing things to self.</td>
 </tr>
 <tr>
 <td>self.add(*vars)</td>
 <td>Add *vars to self</td>
 </tr>
 <tr>
 <td>self.remove(*vars)</td>
 <td>Remove *vars from self (Ignore it if it's not in self).</td>
 </tr>
 <tr>
 <td>self.replace(ind,var)</td>
 <td>Replace self[index] with var. (index can be int or anything thats in self</td>
 </tr>
 <tr>
 <td>self[index]=var</td>
 <td>Set self[index] to var. (Like lists) (it does not replace)</td>
 </tr>
 <tr>
 <td>self.</td>
 <td>&nbsp;</td>
 </tr>
 </tbody>
 </table>
 <p>&nbsp;</p>
 <p>&nbsp;</p>
 <p>&nbsp;</p>

'''




def _Check_Imports(module):
    try:
        if module == 'keyboard':
            import keyboard
            Module = keyboard
        if module == 'pyautogui':
            import pyautogui
            Module = pyautogui
        if module == 'psutil':
            import psutil
            Module = psutil
        if module == 'colored':
            import colored
            Module = colored
        if module == 'requests':
            import requests
            Module = requests
        if module == 'mouse':
            import mouse
            Module = mouse
        if module == 'whois':
            import whois
            Module = whois
        if module == 'win10toast':
            import win10toast
            Module = win10toast
        return Module
    except:
        raise ImportError(f"Package '{module}' is not installed (use 'pip install {module}')")




