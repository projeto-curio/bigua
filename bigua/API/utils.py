import datetime

def to_date(string, formats):

    if string is None:
        return None
    elif len(string) > 0:
        return datetime.datetime.strptime(string, formats)
    else:
        return None

def tryit(value, key):

    try:
        return value[key]
    except KeyError:
        return None

def force_list(obj):
    
    if not isinstance(obj, list):
        return [obj]
    else:
        return obj

def force_datetime(string):
    
    if string is None:
        return None
    elif len(string) <= 10:
        string = string + ' 00:00:00'
    
    return to_date(string, '%d/%m/%Y %H:%M:%S')