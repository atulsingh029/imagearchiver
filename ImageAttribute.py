#  Author : Atul Singh
#  Email    : atulsingh29@protonmail.com
#  Github  : https://github.com/atulsingh029

import os
from datetime import datetime


def attributebasedtimestamp(imagePath):
    data = os.stat(imagePath)
    timestamp = [data.st_ctime , data.st_mtime , data.st_atime]
    if timestamp[0] is not None:
        timestamp = datetime.utcfromtimestamp(timestamp[0])
    elif timestamp[1] is not None:
        timestamp = datetime.utcfromtimestamp(timestamp[1])
    else:
        timestamp = datetime.utcfromtimestamp(timestamp[2])

    return timestamp
