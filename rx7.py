'''
This Module is one to make your code shorter.
Collection of most usefull function and methods from popular modules of python.
'''
'''
FEATURES:
  Functions:
   - print   ==>                           p
   - re(Function_Name,Times) :             "repeat a function for certain times"
   - a[::-1] ==>                           rev(a)       (you can also use integers: 158 ==> 851)
   - read(file_path) :                     return content of the file
   - write(file_path) :                    write things you want in file you want. (Read Help)
   - time.sleep(seconds) ==>               wait(sec)
   - cls() :                               function to clear the console and terminal.
   - progressbar() :                       function for creating in-app progressbar. (Read Help)
   - string(First_Letter,Last_Letter) :    return a string from first argumant until second argumant (Only integer or letter). 
  
  Classes:
   - CLASS rand:                           1- item(population) :        "random item from population."
                                           2- integer(First,Last) :     "random integer between First and Last"
                                           3- O1(decimal_number=17) :   "random float between 0 and 1. Default rounding is 17"
                                           4- number(First,Last):       "random number(integer or float) between First and Last"
                                           
   - CLASS system:                         1- accname()                 "User account name."
                                           2- pid() :                   "PID of the terminal."
                                           3- chdir :                   "Change directory of terminal."
                                           4- #####disk_usage:          ""
   - CLASS file:
                                         


Written By RX
Last Update: 3-1-2020
'''



#START
import os,shutil,random,time,os


def p(text='',rep=None):
    '''
    p is print!
    But because we use it a lot, we\'ve decided to make it one letter.
    Example:
        p('Hello World')
        ==>Hello World
    Example:
        p('Hello <>.','World')
        ==>Hello World.
    '''
    Ex=text
    if rep!=None:
        Ex= text.replace('<>',rep)
    print(Ex)


def re(Function_name,Times):
    '''
    re is for repeating a function.
    for more info see the example below.
    Example:
        re(Func_Name, 3)
        ==> "function Func_Name will launch 3 times."
    '''
    i=1
    while i <= Times:
        i+=1
        Function_name() 


def rev(ex):
    '''
    This function is for reversing Strings, Lists, Tuples And also Integers.
    Example:
        b= rev('Football')
        print(b)
        ==> llabtooF
    '''
    ret=ex
    if type(ret)==int or type(ret)==float:
        ret= str(ret)
        ret= ret[::-1]
        if type(ex)==int:
            ret= int(ret)
        else:
            ret=float(ret)
    else:
        #global ex
        ret= ret[::-1]
        #print(ex)
    return ret


def read(file):
    '''
    This can help you to read your file faster.
    Example:
        read_file('C:\\users\\Jack\\test.txt')
        ==> "Content of 'test.txt' will be shown."
    '''
    op= open(file,mode='r')
    FileR= op.read()
    op.close()
    return FileR
    #print(FileR)
    


def write(file,mode='replace',text=None):
    if mode=='replace':
        op= open(file,mode='w')
        if text==None:
            text= input('Type what you want.\n\n')
        op.write(text)
        #print('File has been created/changed.')
        op.close()
    elif mode=='continue':
        opr= open(file,mode='r')
        FileR= opr.read()
        op= open(file,mode='w')
        if text==None:
            text= input('Type what you want to add in the end of the file.\n\n')
        #op.write(FileR+'\n'+text)
        op.write(FileR+text)
        #print('File has been created/changed.')
        op.close() 
    else:   
        print('Error\nmode can only be: 1-replace(default)  2-continue\nNot "{0}"'.format(mode)) 


def wait(seconds):
    '''
    Use this if you want your program wait for a certain time.
    Example:
        wait(3)
        ==> "Nothing happen and there will be no calculation for 3 seconds"
    '''
    import time
    time.sleep(seconds)

__SQ_= 'powernrxbetfromporto'
def cls():
    '''
    You can use this function if you want to clear the environment.
    '''
    os.system('cls')


def progressbar(Total=100,Dashes_Nom=100,Time=1,Dashes_Shape='-',Complete_Shape='#',Pre_Text='Loading: '):
    '''
    Use this function to make a custom in-app progress bar.
    Example:
        progressbar(Total=100,Dashes_Nom=100,Time=1,Dashes_Shape='-',Complete_Shape='#', Pre_Text='Loading')
        ==>   Loading: [####------] 40/100
    '''
    import sys
    def Progressbar(it, prefix="", size=60, file=sys.stdout):
        count = len(it)
        def show(j):
            x = int(size*j/count)
            file.write("%s[%s%s] %i/%i\r" % (prefix, Complete_Shape*x, Dashes_Shape*(size-x), j, count))
            file.flush()        
        show(0)
        for i, item in enumerate(it):
            yield item
            show(i+1)
        file.write("\n")
        file.flush()
    for i in Progressbar(range(Total), Pre_Text, Dashes_Nom):
        time.sleep(Time)


def string(First_Letter='a',Last_Letter='z'):
    if type(First_Letter)==type(Last_Letter):
        if type(First_Letter)==str:
            Alfa='abcdefghijklmnopqrstuvwxyz'
            for i in range(26):
                if Alfa[i] == First_Letter:
                    fi= i
                if Alfa[i] == Last_Letter:
                    li= i+1
            strin= Alfa[fi:li]
            return strin
        elif type(First_Letter)==int:
            strin=''
            i=First_Letter
            for i in range(First_Letter,Last_Letter+1):
                strin= strin+str(i)
            return strin
        elif type(First_Letter)!=int and type(First_Letter)!=str:
            print('Invalid input for argumant(s).\n{0}&{1} are {2}.\nBut Valid input should have "str" or "int" type.'.format(First_Letter,Last_Letter,type(First_Letter)))
    else:
        print('Invalid input.\nFirst argumant is {0} And Second argumant is {1} \nArgumants should have the same type.'.format(type(First_Letter),type(Last_Letter)))


"""
def START():
    '''
    You have to use this function with FINNISH function.
    With these two functions, you can calculate a process time.
    e.g:
        Start= START()
        #some codes...
        End= FINNISH(Start)
        #End is time passed between Start vaiable and End Variable.
    (Remember that argumant of FINNISH function should be variable of START function.)
    '''
    return time.time()
def FINNISH(start_name):
    '''
    You have to use this function with START function.
    With these two functions, you can calculate a process time.
    e.g:
        Start= START()
        #some codes...
        End= FINNISH(Start)
        #End is time passed between Start vaiable and End Variable.
    (Remember that argumant of FINNISH function should be variable of START function.)    
    '''
    return time.time()-start_name
"""


def force(tpl,*var):  
    '''
    It returns tpl with adding var(s) to it.
    '''
    return tuple(list(tpl)+[v for v in var])
#force= lambda tpl,*var: tuple(list(tpl)+[v for v in var])

def erase(tpl,*var):
    '''
    It returns tpl with removing var(s) to it.
    '''
    #lstv= [v for v in var if v in tpl]
    lstt= list(tpl)
    for th in [v for v in var if v in tpl]:
        lstt.remove(th)
    return lstt









######################
     ############
######################
        

class rand:
    '''
    Random Variable Generator Class.
    '''
    def choice(item):
        '''
        Return a random element from a non-empty sequence.
        '''
        return random.choice(item)
    def integer(first_number,last_number):
        '''
        Return random integer in range [a, b], including both end points.
        '''
        return random.randint(first_number,last_number)
    def O1(decimal_number=17):
        '''
        return x in the interval [0, 1)
        '''
        return round(random.random(),decimal_number)
    def number(first_number,last_number):
        '''
        return x in the interval [F, L]
        '''
        return random.uniform(first_number,last_number)        


'''
class Math:
    def sqrt(number):
        import math
        return math.sqrt(number)
'''


class system:
    def accname():
        '''
        return account username you have logged in.
        '''
        return os.getlogin()
    def pid():
        '''
        Get pid number of terminal and return it.
        '''
        return os.getpid()
    def disk_usage(path):
        ####
        return shutil.disk_usage(path)
    def chdir(path):
        '''
        Change directory of terminal.
        '''
        os.chdir(path)
    def SHUT_DOWN():
        os.system("shutdown /s /t 1")
    def RESTART():
        os.system("shutdown /r /t 1")


class file:
    def __init__(self,path):
        self.path= path
    def size(self):
        '''
        return size of the file in byte(s).
        Also work on directories.
        '''
        return os.path.getsize(self.path)
        #rooye pooshe emtehan she
    def delete(path):
        '''
        Use this to delete a file (Not folder).
        '''
        os.remove(path)
    def delete_dir(path):
        '''
        Use this to delete folders.
        '''
        shutil.rmtree(path)
    def rename(old_name,new_name):
        'Rename files with this function.'
        os.rename(old_name,new_name)
    def abspath(path):
        '''
        return absolute path of given path.
        '''
        return os.path.abspath(path)
    def exists(path):
        '''
        Search for the file And Returns a boolean.
        if file exists: True
        else: False
        '''
        return os.path.exists(path)
    def mdftime(path):
        '''
        Get last modify time of the file.
        '''
        return os.path.getmtime(path)
    def acstime(path):    
        '''
        Get last access time of the file.
        '''
        return os.path.getatime(path)
        # change to date bayad biad
    def move(src,dst):
        '''
        Move (cut) file from crs to dst.
        '''
        shutil.move(src,dst)
        #Baraye folder hast ya na?
    def copy(src,dst):
        '''
        Copy the file (Not folder)from src to destination.
        (You can use it instead of rename too.
         e.g:
            copy('D:\\Test.py','E:\\Ali.py')
            (It copies Test.py to E drive and renames it to Ali.py)
         )
        (Use copydir function to copy directory.)
        '''
        shutil.copy(src,dst)
    def copydir(src,dst):
        '''
        Same as copy function except that it\'s for folders.
        '''
        shutil.copytree(src,dst)
    #Make readonly & hidden & shortcut (+bool)
    def hide(path):
        try:
            os.system( "attrib -h "+path)
        except:
            import subprocess
            subprocess.check_call(["attrib","+H",path])
    def read_only(path,mode=True):
        if type(mode)==bool:
            from stat import S_IREAD,S_IWUSR
            if mode==True:
                os.chmod(path, S_IREAD)
            elif mode==False:
                os.chmod(path, S_IWUSR)
        else:
            raise Exception('Second argumant (mode) should be boolean.')



class style:
    def text(text='',color='default',BG='black',style='None'):
        from colored import fg,bg,attr
        if color=='default':
            color=7 #188
        if style=='None':
            style=0
        pass
        if text=='':
            print('%s%s%s' % (attr(style),bg(BG),fg(color)),end='')
        else:
            print('%s%s%s%s%s' % (attr(style),bg(BG),fg(color),text,attr(0)))

    def switch(color='default',BG='black',style='None'):
        from colored import fg,bg,attr
        print('%s%s%s' % (attr(style),bg(BG),fg(color)),end='')


class record:
    def __init__(self):
        self.start= time.time()
    #def START(self):
    #    return time.time()
    def Stop(self):
        return time.time()-self.start


class style:
    def text(text='',color='default',BG='black',style='None'):
        from colored import fg,bg,attr
        if color=='default':
            color=7 #188
        if style=='None':
            style=0
        print('%s%s%s%s%s' % (attr(style),bg(BG),fg(color),text,attr(0)))


#END