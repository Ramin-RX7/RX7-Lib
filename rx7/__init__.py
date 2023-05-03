"""
This Module is One to Make Your Code Shorter.

Collection of most usefull function and methods from popular modules of python.

Official documentation in https://github.com/Ramin-RX7/RX7-Lib
"""
'''
Written By RX
Last Update: 05-03-2022
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

from . import io
IO = io

from . import internet
Internet = internet

from . import datetime
date_time = DateTime =  datetime


"""
write = files.write
read  = files.read
Check_Type = Decorator.Check_Type
overload   = Decorator.overload
Input   = default_input  = io.Input
getpass = password_input = io.getpass
"""
#END
