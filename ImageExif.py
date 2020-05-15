#  Author : Atul Singh
#  Email  : atulsingh29@protonmail.com
#  Github : https://github.com/atulsingh029

from PIL import Image
import ImageObj
import ImageAttribute

def getimageobj(imagePath,name):
    img = Image.open(imagePath,mode='r')
    data = img.getexif()
    img.close()
    timestamp = data.get(36867)
    if timestamp is None or timestamp == "":
        timestamp = data.get(306)
    if timestamp is None or timestamp == "":
        timestamp = ImageAttribute.attributebasedtimestamp(imagePath)
    processedimage = ImageObj.ImageObj(name,timestamp)
    return processedimage
