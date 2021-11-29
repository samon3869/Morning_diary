import datetime
import pandas as pd
import calendar

# common function
def add_days(source_date, count): 
    target_date = source_date + datetime.timedelta(days = count) 
    return target_date

def date_range(start, end):
    start = datetime.datetime(start.year, start.month, start.day)
    end = datetime.datetime(end.year, end.month, end.day)
    dates = [date.strftime("%m/%d/%Y") for date in pd.date_range(start, periods=(end-start).days+1)]
    return dates

# week function
def get_weeks_first_date(source_date): 
    temporaryDate = datetime.datetime(source_date.year, source_date.month, source_date.day) 
    weekDayCount = temporaryDate.weekday() 
    target_date = add_days(temporaryDate, -weekDayCount)
    return target_date

def get_week_days(source_date):
    first_date = get_weeks_first_date(source_date)
    end_date = add_days(first_date, 6)
    week_days = date_range(first_date, end_date)
    return week_days

# month function
def get_month_days(source_date):
    first_date = datetime.datetime(source_date.year, source_date.month, 1)
    end_date = datetime.datetime(
        source_date.year, 
        source_date.month, 
        calendar.monthrange(source_date.year, source_date.month)[1]
    )
    month_days = date_range(first_date, end_date)
    return month_days

