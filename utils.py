import os 
import pathlib
from datetime import date, datetime

def get_datetime():
    now_date = str(date.today()).replace('-', '')
    now_time = str(datetime.now().time())[:8].replace(':', '')
    now_datetime = now_date + '_' + now_time
    
    return now_datetime


def file_rename(old_name):
    extension = pathlib.Path(old_name).suffix
    new_name = './static/uploads/' + get_datetime() + extension

    os.rename(old_name, new_name)
    
    return new_name



