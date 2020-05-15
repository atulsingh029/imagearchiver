#  Author : Atul Singh
#  Email  : atulsingh29@protonmail.com
#  Github : https://github.com/atulsingh029

from datetime import datetime as dt

class ImageObj:
    month = ['dummy', 'january', 'february', 'march', 'april', 'may', 'june',
             'july', 'august', 'september', 'october', 'november', 'december']

    def __init__(self, name, timestamp):
        self.name = name
        self.timestamp = timestamp
        if type(timestamp) is list:
            self.timestamp= dt.utcnow().strftime('%Y %m')


    def folder(self):
        stamp=str(self.timestamp)
        date = stamp[0:10]
        year = "year_" + date[0:4]
        month = ImageObj.month[int(date[5:7])]
        return '\\'+year+'\\'+month

