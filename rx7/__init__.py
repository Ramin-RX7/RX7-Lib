"""
This Module is One to Make Your Code Shorter.

High API Will Make You Feel You're Ordering And Machine Is Doing!

Also There is Collection of most usefull function and methods from popular modules of python.
(Read Help of Functions)

Official documentation in https://github.com/Ramin-RX7/RX7-Lib
"""
'''
Written By RX
Last Update: 05-02-2022
'''
__version__ = '3.3.0'


"""
< Release Changes >

"""


#START

from .functions import *



from . import random
Random = random

from . import files
Files = files
write = files.write
read  = files.read

from . import system
System = system


from . import style
Style = style


from .record import Record
record = Record


from . import terminal
Terminal = terminal


from . import decorator
Decorator  = decorator
Check_Type = Decorator.Check_Type
overload   = Decorator.overload


from . import io
IO = io
Input   = default_input  = io.Input
getpass = password_input = io.getpass


from . import internet
Internet = internet


from . import datetime
date_time = DateTime =  datetime

#END
