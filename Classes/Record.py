"""
Use this method to record an action time in second.
Usage:
    Start= record()
    #Some codes here...
    Finnish= Start.lap()
    print(Finnish) ==> 0.25486741
    #Some more codes here...
    Finnish= Start.lap() ==> 0.4502586
    Start.laps -->  [0.25486741, 0.4502586]
Use Start.stop() to finnish recording and save memory.
(after self.stop() using self.lap will cause error.)
"""
import time as _time



class Record:
    """
    Use this method to record an action time in second.
    Usage:
        Start= record()
        #Some codes here...
        Finnish= Start.lap()
        print(Finnish) ==> 0.25486741
        #Some more codes here...
        Finnish= Start.lap() ==> 0.4502586
        Start.laps -->  [0.25486741, 0.4502586]
    Use Start.stop() to finnish recording and save memory.
    (after self.stop() using self.lap will cause error.)
    """
    def __init__(self):
        self.__start = _time.time()
        self.laps = []
    def __call__(self):
        return f'Laps: {self.laps}'
    def __repr__(self):
        return f'Laps: {self.laps}'

    def lap(self, save=True, Round=15) -> float:
        '''
        Return time passed from creating time of self.
        (Read 'record' Doc String)
        If save is True, time will be added to self.laps
        '''
        lp = _time.time() - self.__start
        lp = round(lp,Round)
        if save:
            self.laps.append(lp)
        return lp

    def reset(self, reset_start=False):
        '''
        This will erase self.laps
        If reset_start is True, start time will reset too.
        '''
        self.laps = []
        if reset_start:
            self.__start = _time.time()

    def last_lap(self, save=True):
        '''
        Return time passed from last lap
        (If self.laps is False then from start_time)
        '''
        ret = (self.lap(False)-self.laps[-1]) if self.laps else self.lap(False)
        if save:
            self.laps.append(self.lap())
        return ret

    @staticmethod
    def timeit(code="pass",setup="pass",times=1_000_000,globals_=None):
        '''
        Run the 'code' for 'times' times and return time it needs (all, not once)
        (If you need any initialization for your 'code', put it in setup arg)
        '''
        import timeit
        return timeit.timeit(stmt=code,setup=setup,number=times,globals=globals_)
