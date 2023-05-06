"""
Recording time of operations using `Record` class
"""
import time as _time
from functools import wraps as _wraps



class Record:
    '''
    Use this method to record an action time in second.

    Usage:
        >>> timer = record()
        >>> #Some codes here...
        >>> Finnish = timer.lap()
        >>> print(Finnish)           ==>  0.25486741
        >>> #Some more codes here...
        >>> Finnish = timer.lap()    ==>  0.4502586
        >>> timer.laps               ==>  [0.25486741, 0.4502586]
    '''
    def __init__(self):
        self.__start = _time.time()
        self.laps = []
    def __str__(self):
        return f'Laps: {self.laps}'

    def lap(self, save=True, round:int=15) -> float:
        '''
        Returns time passed from creation of Record object.
        If save is True, time will be added to self.laps
        '''
        lp = _time.time() - self.__start
        lp = round(lp,round)
        if save:
            self.laps.append(lp)
        return lp

    def reset(self, reset_start=False):
        '''
        This will clears self.laps
        If reset_start is True, start time will reset too.
        '''
        self.laps = []
        if reset_start:
            self.__start = _time.time()

    def last_lap(self, save=True):
        '''
        Return time passed from last lap
        (If self.laps is empty then from start_time)
        '''
        ret = (self.lap(False)-self.laps[-1]) if self.laps else self.lap(False)
        if save:
            self.laps.append(self.lap())
        return ret


    @staticmethod
    def timer(function):
        """Decorator to display function call duration"""
        @_wraps(function)
        def wrapper(*args, **kwargs):
            t1 = _time.time()
            result = function(*args, **kwargs)
            t2 = _time.time()
            print(f"{function.__name__} : {t2-t1}")
            return result
        return wrapper


    @staticmethod
    def timeit(code:str="pass", setup:str="pass", times:int=1_000_000, globals_=None):
        '''
        Run the 'code' for 'times' times and return time it needs (all, not once)
        (If you need any initialization for your 'code', put it in setup arg)
        '''
        import timeit
        return timeit.timeit(stmt=code,setup=setup,number=times,globals=globals_)
