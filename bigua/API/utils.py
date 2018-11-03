import datetime

def to_date(string, formats):
    if string is not None:
        return datetime.datetime.strptime(string, formats)
    else:
        return None

def force_list(obj):
    
    if not isinstance(obj, list):
        return [obj]
    else:
        return obj