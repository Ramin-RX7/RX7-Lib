import datetime as Datetime
import calendar,time

class date_time:
    NOW= time.localtime()
    NOW_YEAR= NOW.tm_year
    NOW_MONTH= NOW.tm_mon
    NOW_DAY= NOW.tm_mday
    NOW_HOUR= NOW.tm_hour
    NOW_MINUTE= NOW.tm_min
    NOW_SECOND= NOW.tm_sec
    TODAY= Datetime.date(NOW_YEAR,NOW_MONTH,NOW_DAY)
    Weekday_Names= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    month_lst= ['january','february','march','april','may','june',
                'july','august','september','october','november','december']    
    month_dic= {month:month_nom for month in month_lst for month_nom in range(1,13)}                
    def __init__(self,year=NOW_YEAR,month=NOW_MONTH,day=NOW_DAY,hour=NOW_HOUR,minute=NOW_MINUTE,second=NOW_SECOND,first_week_day=0):
        '''
        .: Working With Date and Time :.
        - Include Both Static Methods and Class Methods
        - Get Now Time
        - Show in Calendar
        - Next and Previous Months in Calendar
        - Determine Time Passed From Specific Date
        - Calendar Supports Setting First Day of the Week
        '''
        if type(month)==str:
            month= date_time.month_dic[month.lower()]
        self.date= Datetime.date(year,month,day)
        self.year=year; self.month=month; self.day=day
        self.time= (hour,minute,second)
        self.hour=self.time[0]; self.minute=self.time[1]; self.second=self.time[2]

        self.weekday= date_time.get_weekday(self.year,self.month,self.day)
        self.weekday_name= date_time.get_weekday(self.year,self.month,self.day,True)
        self.week_nom= date_time.get_weeknom(self.year,self.month,self.day)

        #self.first_week_day= first_week_day
        calendar.setfirstweekday(first_week_day)
        self.calendar= str(calendar.month(year, month)).replace(str(day),rx.style(str(day),'green').content)
        self.calendar_month= str(calendar.month(year, month))
        self.calendar_year_all=str(calendar.calendar(year))
        self.calendar_year= [calendar.month(year,i) for i in range(1,13)]
        self.calendar_next_all= [calendar.month(year,i) for i in range(self.month+1,13)]
        self.calendar_prev_all= [calendar.month(year,i) for i in range(1,self.month)]
        self.calendar_position_next_year= str(calendar.month(year+1, month)).replace(str(day),rx.style(str(day),'green').content)
        self.calendar_position_prev_year= str(calendar.month(year-1, month)).replace(str(day),rx.style(str(day),'green').content)
        
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
        calendar.setfirstweekday(day)
        self.calendar= str(calendar.month(self.year, self.month)).replace(str(day),rx.style(str(day),'green').content)
        self.calendar_month= str(calendar.month(self.year, self.month))
        self.calendar_year_all=str(calendar.calendar(self.year))
        self.calendar_year= [calendar.month(self.year,i) for i in range(1,13)]
        self.calendar_next_all= [calendar.month(self.year,i) for i in range(self.month+1,13)]
        self.calendar_prev_all= [calendar.month(self.year,i) for i in range(1,self.month)]
        self.calendar_position_next_year= str(calendar.month(self.year+1, self.month)).replace(str(day),rx.style(str(day),'green').content)
        self.calendar_position_prev_year= str(calendar.month(self.year-1, self.month)).replace(str(day),rx.style(str(day),'green').content)

        self.weekday= date_time.get_weekday(self.year,self.month,self.day)
        self.weekday_name= date_time.get_weekday(self.year,self.month,self.day,True)
        self.week_nom= date_time.get_weeknom(self.year,self.month,self.day)

    @staticmethod
    def Datetime_now():
        return str(Datetime.Datetime.today())[:19]
    @staticmethod
    def calender_year(year=NOW_YEAR):
        return [calendar.month(year,i) for i in range(1,13)]
    @staticmethod
    def calendar_month_st(month=NOW_MONTH,year=NOW_YEAR,day=0):
        if not day:
            return str(calendar.month(year, month))
        else:
            return str(calendar.month(year, month)).replace(str(day),rx.style(str(day),'green').content)
    @staticmethod
    def passed_date(f_date,l_date=TODAY,return_time='day'):
        f_date = Datetime.date(f_date[0], f_date[1], f_date[2])
        return_time= return_time.lower()
        if return_time in ('day','month','year','hour','minute','second'):
            DELTA=  l_date - f_date
            if return_time == 'year':
                return DELTA/365            
            elif return_time == 'month':
                return DELTA/30
            elif return_time == 'day':
                return DELTA
            elif return_time =='hour':
                return DELTA*24
            elif return_time == 'minute':
                return DELTA*1440
            elif return_time == 'second':
                return DELTA*86400
        else:
            raise ValueError("return_time should be in  ('year', 'month', 'day', 'hour', 'minute', 'second')")
    '''@staticmethod
     def passed_time(year=1970,month=1,day=1,hour=0,minute=0,second=0,return_time='second'):
        pass'''
    @staticmethod
    def convert_epoch_to_local(second=time.time()):
        return time.ctime(second)
    @staticmethod
    def get_weekday(year=NOW_YEAR,month=NOW_MONTH,day=NOW_DAY,return_name=False):
        if return_name:
            return date_time.Weekday_Names[Datetime.date(year,month,day).weekday()]
        else:
            return Datetime.date(year,month,day).weekday()
    @staticmethod
    def get_weeknom(year=NOW_YEAR,month=NOW_MONTH,day=NOW_DAY):
        return Datetime.date(year,month,day).isocalendar()[1]
    @staticmethod
    def calendar_show_week(week_nom,year=NOW_YEAR):
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
                if calendar.monthrange(year,mnth)[1]<day:
                    mnth+=1
                    day-= calendar.monthrange(year,mnth)[1]
                else:
                    true= True
            except calendar.IllegalMonthError:
                class BadWeekNumber(Exception):
                    def __init__(self, message='Week Number is Higher Than Year Weeks.'): super().__init__(message)
                raise BadWeekNumber from None
        new= date_time(year,mnth,day)

        cal= new.calendar_month.splitlines()
        for item in cal:
            if str(new.day) in item and item != cal[0]:
                INDEX= cal.index(item);COLORED_WEEK= rx.style(item,'green');break

        WEEK_WITH_COLOR= '\n'.join(cal[:INDEX]+[str(COLORED_WEEK)]+cal[INDEX+1:])
        return WEEK_WITH_COLOR
    @staticmethod
    def get_year():
        return time.localtime().tm_year
    @staticmethod
    def get_month():
        return time.localtime().tm_mon
    @staticmethod
    def get_day_of_month():
        return time.localtime().tm_mday
    @staticmethod
    def get_day_of_week():
        return time.localtime().tm_wday
    @staticmethod
    def get_day_of_year():
        return time.localtime().tm_yday
    @staticmethod
    def get_hour():
        return time.localtime().tm_hour
    @staticmethod
    def get_minute():
        return time.localtime().tm_min
    @staticmethod
    def get_second():
        return time.localtime().tm_sec
