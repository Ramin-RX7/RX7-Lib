_Auto = 0
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

        def __setattr__(self,_attr,value):
            if self._init:
                raise AttributeError(f"'Constant' object does not support item assignment")
            else:
                super(_Lang.Constant,self).__setattr__(_attr,value)

        def __getitem__(self,index):
            return self.__members[index]
        def __contains__(self,obj):
            return obj in self.__members
        def __bool__(self):
            return bool(len(self.__members))
        #'''
        def __hash__(self):
            return hash(tuple(['Constant',len(self)]+list(self.__members)))
        #'''
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

        def __init__(self,*args,type_=_Auto,size=_Auto):
            self.__members = []
            if type_:
                self.__TYPE = type_
            else:
                self.__TYPE = type(args[0])
            self.__TYPE_NAME  = self.__TYPE.__name__
            if size:
                self.__SIZE = size
            else:
                self.__SIZE = len(args)

            for obj in args:
                if type(obj) == self.__TYPE:
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

        #Constant   =  type(_Lang.Constant(1))
        #Array      =  type(_Lang.Array(1,1))

        Any         =   type#_typing.Any
        Callable    =  _typing.Callable
        Container   =  _typing.Container
        Generator   =   Lambda #type(_f) #Not Built-in(s)   #_types.GeneratorType || _typing.Generator
        Iterable    =  _typing.Iterable
        Iterator    =  _typing.Iterator
        NoReturn    =  _typing.NoReturn
        Optional    =  _typing.Optional
        BuiltinFunction = type(len)
        BuiltinMethod   = type([].append)
        Module = type(_typing)
        Method = type(globals()['Record']().lap)
        #Mapping     =  _typing.Mapping
        #OrderedDict =  _typing.OrderedDict
        #Text        =  str
        #Union  = _typing.Union
        #_types.AsyncGeneratorType
    types = Types
#setattr(_Lang,'Const',type(_Lang.Constant(1)))
#setattr(_Lang,'Array',type(_Lang.Array(1,1)))
