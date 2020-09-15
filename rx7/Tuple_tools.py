'''
This Module includes Tuple object and tuple functions. 
All of the functions are in rx7 module so I recommend to use  rx7.FUNCTION  
instead of  rx7.tuple_obj.FUNCTION  to ease.
'''


from typing import Any
from typing import Union

######################
#     FUNCSTIONS     #
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

def replace(tpl: tuple, ind: Union[int,str], var: Any) -> tuple:
    '''
    (TUPLE FUNCTION)
    Replace tpl[ind] with var
    '''
    tpl=list(tpl)
    if type(ind) == str:
        ind= tpl.index(ind)
    tpl[ind]=var
    return tuple(tpl)

def insert(tpl: tuple, ind: Union[int,str], var: Any) -> tuple:
    '''
    (TUPLE FUNCTION)
    Exactly like tpl[ind]=var in lists but for tuples.
    '''
    tpl=list(tpl)
    if type(ind) == str:
        ind= tpl.index(ind)
    tpl.insert(ind,var)
    return tuple(tpl)   



##################
#     OBJECT     #
##################
    
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
    #############################
    #############################
    def __bool__(self):
        return bool(len(self.__content))
    '''def __contains__(self,obj):
        return bool(obj in self.__content)'''
    def __hash__(self):
        return hash(self.__content)
    def __len__(self):
        return len(self.__content)
    #############################
    #############################
