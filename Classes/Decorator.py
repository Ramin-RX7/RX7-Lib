import abc as _abc
from typing import Callable


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
