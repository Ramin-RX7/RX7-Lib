import re as _re
import time as _time
import calendar as _calendar
import datetime as _datetime

from .style import Styled



class DateTime:

    _NOW=        0
    _NOW_YEAR=   0
    _NOW_MONTH=  0
    _NOW_DAY=    0
    _NOW_HOUR=   -1
    _NOW_MINUTE= -1
    _NOW_SECOND= -1
    def NOW():
        _NOW= _time.localtime()
        _NOW_YEAR= _NOW.tm_year
        _NOW_MONTH= _NOW.tm_mon
        _NOW_DAY= _NOW.tm_mday
        _NOW_HOUR= _NOW.tm_hour
        _NOW_MINUTE= _NOW.tm_min
        _NOW_SECOND= _NOW.tm_sec
        return _datetime.datetime(_NOW_YEAR,_NOW_MONTH,_NOW_DAY,_NOW_HOUR,_NOW_MINUTE,_NOW_SECOND)
    now = NOW
    def normalize(date=[],time=[]):
        now = date_time.NOW()
        try:
            if not date[0]:  date[0]= now.year
            if type(date[1]) == str:
                try:
                    date[1]= date_time.month_dic[date[1].lower()]
                except KeyError:
                    raise ValueError("Wrong Month Name") from None
            if not date[1]:  date[1]= now.month
            if not date[2]:  date[2]= now.day
        except IndexError:
            pass
        try:
            if time[0]<0: now.hour
            if time[1]<0: now.minute
            if time[2]<0: now.second
        except IndexError:
            pass
        return [date,time]
    Weekday_Names= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    month_lst= ['january','february','march','april','may','june',
                'july','august','september','october','november','december']
    month_dic= {month:month_nom for month in month_lst for month_nom in range(1,13)}

    def __init__(self,year=_NOW_YEAR,month=_NOW_MONTH,day=_NOW_DAY,hour=_NOW_HOUR,minute=_NOW_MINUTE,second=_NOW_SECOND,first_week_day=0):
        '''
        .: Working With Date and Time :.
        - Include Both Static Methods and Class Methods
        - Get NOW Time
        - Show in Calendar
        - Next and Previous Months in Calendar
        - Determine Time Passed From Specific Date
        - Calendar Supports Setting First Day of the Week
        '''

        """
        Now = date_time.NOW()
         if not year :  year=Now.year
         if not month:  month=Now.month
         if not day  :  day=Now.day
         if hour<0   :  hour=Now.hour
         if minute<0 :  minute=Now.minute
         if second<0 :  second=Now.second
         """
        _norm = date_time.normalize([year,month,day],[hour,minute,second])
        year,month,day = _norm[0]
        hour,minute,second = _norm[1]

        if type(month)==str:
            try:
                month= date_time.month_dic[month.lower()]
            except KeyError:
                raise ValueError("Wrong Month Name") from None

        self.date= _datetime.date(year,month,day)
        self.year=year; self.month=month; self.day=day
        self.time= (hour,minute,second)
        self.hour=hour; self.minute=minute; self.second=second

        self.weekday= date_time.get_weekday(self.year,self.month,self.day)
        self.weekday_name= date_time.get_weekday(self.year,self.month,self.day,True)
        self.week_nom= date_time.get_weeknom(self.year,self.month,self.day)

        #self.first_week_day= first_week_day
        _calendar.setfirstweekday(first_week_day)
        self.calendar= str(_calendar.month(year, month)).replace(str(day),Styled(str(day),'green').styled)
        self.calendar_month= str(_calendar.month(year, month))
        self.calendar_year_all=str(_calendar.calendar(year))
        self.calendar_year= [_calendar.month(year,i) for i in range(1,13)]
        self.calendar_next_all= [_calendar.month(year,i) for i in range(self.month+1,13)]
        self.calendar_prev_all= [_calendar.month(year,i) for i in range(1,self.month)]
        self.calendar_position_next_year= str(_calendar.month(year+1, month)).replace(str(day),Styled(str(day),'green').styled)
        self.calendar_position_prev_year= str(_calendar.month(year-1, month)).replace(str(day),Styled(str(day),'green').styled)

    def setfirstweekday(self,day):
        if type(day)==int and day<7:
            date_time.Weekday_Names= date_time.Weekday_Names[day:]+date_time.Weekday_Names[:day]
        elif type(day)==str:
            day= date_time.Weekday_Names.index(day)
            date_time.Weekday_Names= date_time.Weekday_Names[day:]+date_time.Weekday_Names[:day]
        else:
            if type(day)==int:
                raise ValueError('Invalid Nomber. Day number should be in range(7)')
            else:
                raise TypeError(f"Inappropriate Type For 'day'.  day can be 'str' or 'int' not {type(day)}")
        _calendar.setfirstweekday(day)
        self.calendar= str(_calendar.month(self.year, self.month)).replace(str(day),Styled(str(day),'green').styled)
        self.calendar_month= str(_calendar.month(self.year, self.month))
        self.calendar_year_all=str(_calendar.calendar(self.year))
        self.calendar_year= [_calendar.month(self.year,i) for i in range(1,13)]
        self.calendar_next_all= [_calendar.month(self.year,i) for i in range(self.month+1,13)]
        self.calendar_prev_all= [_calendar.month(self.year,i) for i in range(1,self.month)]
        self.calendar_position_next_year= str(_calendar.month(self.year+1, self.month)).replace(str(day),Styled(str(day),'green').styled)
        self.calendar_position_prev_year= str(_calendar.month(self.year-1, self.month)).replace(str(day),Styled(str(day),'green').styled)

        self.weekday= date_time.get_weekday(self.year,self.month,self.day)
        self.weekday_name= date_time.get_weekday(self.year,self.month,self.day,True)
        self.week_nom= date_time.get_weeknom(self.year,self.month,self.day)

    @staticmethod
    def today():
        dt = date_time.NOW()
        return (dt.year,dt.month,dt.day)
    @staticmethod
    def calender_year(year=_NOW_YEAR):
        if not year: year=date_time.NOW().year
        return [_calendar.month(year,i) for i in range(1,13)]
    @staticmethod
    def calendar_month_st(month=_NOW_MONTH,year=_NOW_YEAR,day=0):
        year,month = date_time.normalize([year,month])[0]

        if not day:
            return str(_calendar.month(year, month))
        else:
            return str(_calendar.month(year, month)).replace(str(day),Styled(str(day),'green').styled)
    @staticmethod
    def passed_date(f_date,l_date=_NOW,return_time='day'):
        if not l_date: l_date=date_time.NOW()
        f_date = _datetime.datetime(*f_date)
        return_time= return_time.lower()
        if return_time in ('day','month','year','hour','minute','second'):
            DELTA=  l_date - f_date
            if return_time == 'year':
                try:
                    _return = _re.search(r'(?P<X>(-)?\w+) day',str(DELTA/365)).group('X')
                except:
                    _return = None
                #_return = str(DELTA/365)
            elif return_time == 'month':
                _return = _re.search(r'\w+',str(DELTA/30)).group()
            elif return_time == 'day':
                _return = str(DELTA)[:-14]
            elif return_time =='hour':
                _return = str(DELTA*24)[:-14]
            elif return_time == 'minute':
                _return = str(DELTA*1440)[:-14]
            elif return_time == 'second':
                _return = str(DELTA*3600)[:-14]

            if _return:  return _return
            else: return 0
        else:
            raise ValueError("return_time should be in  ('year', 'month', 'day', 'hour', 'minute', 'second')")
    passed_time = passed_date
    '''@staticmethod
     def passed_time(year=1970,month=1,day=1,hour=0,minute=0,second=0,return_time='second'):
        pass'''
    @staticmethod
    def convert_epoch_to_local(second=_time.time()):
        return _time.ctime(second)
    @staticmethod
    def get_weekday(year=_NOW_YEAR,month=_NOW_MONTH,day=_NOW_DAY,return_name=False):
        """
        First day is Monday and the numbers starts from 0
        """
        year,month,day = date_time.normalize([year,month,day])[0]
        if return_name:
            return date_time.Weekday_Names[_datetime.date(year,month,day).weekday()]
        else:
            return _datetime.date(year,month,day).weekday()
    @staticmethod
    def get_weeknom(year=_NOW_YEAR,month=_NOW_MONTH,day=_NOW_DAY):
        """
        Returns 53 if First week is from last year
        """
        year,month,day = date_time.normalize([year,month,day])[0]
        return _datetime.date(year,month,day).isocalendar()[1]
    @staticmethod
    def calendar_show_week(week_nom,year=_NOW_YEAR):
        year = date_time.normalize([year])[0][0]
        week= week_nom
        for i in list(range(1,8))[::-1]:
            if date_time.get_weeknom(year,1,i)==1:
                FIRST_WEEK_DAYS= len(list(range(i)))
                break

        day= (week-1)*7 - (6-FIRST_WEEK_DAYS)
        mnth= 1
        true=False
        while not true:
            try:
                if _calendar.monthrange(year,mnth)[1]<day:
                    mnth+=1
                    day-= _calendar.monthrange(year,mnth)[1]
                else:
                    true= True
            except _calendar.IllegalMonthError:
                class BadWeekNumber(Exception):
                    def __init__(self, message='Week Number is Higher Than Year Weeks.'): super().__init__(message)
                raise BadWeekNumber from None
        new= date_time(year,mnth,day)

        cal= new.calendar_month.splitlines()
        for item in cal:
            if str(new.day) in item and item != cal[0]:
                INDEX= cal.index(item);COLORED_WEEK= Styled(item,'green');break

        WEEK_WITH_COLOR= '\n'.join(cal[:INDEX]+[str(COLORED_WEEK)]+cal[INDEX+1:])
        return WEEK_WITH_COLOR
    @staticmethod
    def get_year():
        return _time.localtime().tm_year
    @staticmethod
    def get_month():
        return _time.localtime().tm_mon
    @staticmethod
    def get_day_of_month():
        return _time.localtime().tm_mday
    @staticmethod
    def get_day_of_week():
        return _time.localtime().tm_wday
    @staticmethod
    def get_day_of_year():
        return _time.localtime().tm_yday
    @staticmethod
    def get_hour():
        return _time.localtime().tm_hour
    @staticmethod
    def get_minute():
        return _time.localtime().tm_min
    @staticmethod
    def get_second():
        return _time.localtime().tm_sec
date_time = datetime = DateTime
