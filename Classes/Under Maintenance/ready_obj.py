from abc import abstractmethod,ABC

import typing as _typing
import types  as _types
def _f(): yield 1
class Types:
    Str         =  str
    Int         =  int
    Float       =  float
    Set         =  set
    Tuple       =  tuple
    Dict        =  dict
    List        =  list
    Bool        =  bool
    Bytes       =  bytes


    Class       =  type
    Type        =  type
    Object      =  object


    Lambda      =  type(lambda: None)
    Function    =  Lambda #type(lambda: None)

    #Constant   =  type(Constant(1))
    #Array      =  type(Array(1,1))

    Any         =  type#_typing.Any
    Callable    =  _typing.Callable
    Container   =  _typing.Container
    Generator   =  type(_f) #Not Built-in(s)   #_types.GeneratorType   #_typing.Generator
    Iterable    =  _typing.Iterable
    Iterator    =  _typing.Iterator
    Mapping     =  _typing.Mapping
    NoReturn    =  _typing.NoReturn
    Optional    =  _typing.Optional
    OrderedDict =  _typing.OrderedDict
    Text        =  str
    BuiltinFunction = type(len)
    BuiltinMethod = type([].append)
    Module = _types.ModuleType
    Method = _types.MethodType
    #Union  = _typing.Union
    #_types.AsyncGeneratorType

MyList = ['Any','Str']
for Type in MyList:
    globals()[Type] = Types.__dict__[Type]



import zipimport,cmd,code,pyperclip,inspect,itertools
#keyword.iskeyword()
#zipimport.zipimporter()
#code.interact('RX',exitmsg='EXITING')
#cmd.Cmd().









