from datetime import datetime, timedelta

def datetime_to_str(dt):
    return dt.strftime('%Y-%m-%dT%H%M%S')

def getToday_date():
    return datetime.datetime.now()

def getToday_string():
    date = getToday_date()
    return date.strftime('%d')+'/'+date.strftime('%m')+'/'+date.strftime('%Y')

def getDateOffset_days(days):
    return getToday_date()+datetime.timedelta(days=days)

def getDateOffset_days_string(days):
    date_offset = getDateOffset_days(days)
    return date_offset.strftime('%d')+'/'+date_offset.strftime('%m')+'/'+date_offset.strftime('%Y')