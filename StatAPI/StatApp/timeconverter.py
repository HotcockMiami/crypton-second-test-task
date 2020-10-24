'''
Джанга наотрез отказывается нативно работать с UNIX датой,
поэтому я буду менять её на лету прямо тут
'''

from datetime import datetime

def ts_to_date(request_data):
    "Переводит юникс таймстамп в джангоугодный формат времени"
    try:
        request_data['timestamp'] = datetime.fromtimestamp(request_data['timestamp'])
        request_data['error_code'] = 0
    except KeyError:
        request_data['error_code'] = 1
    return request_data
