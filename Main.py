#  Author : Atul Singh
#  Email  : atulsingh29@protonmail.com
#  Github : https://github.com/atulsingh029
import shutil
import ImageExif
import os
directoryLocation = input("Input the complete path of directory : ")
filesandfolders = os.listdir(directoryLocation)
images = []
for ff in filesandfolders:
    if os.path.isfile(directoryLocation+'/'+ff):
        if (ff.endswith('.jpg') or ff.endswith('.jpeg') or ff.endswith('.JPG') or ff.endswith('.JPEG')
            or ff.endswith('.png') or ff.endswith('.PNG')):
            images.append(ff)
print(str(len(images)) + " Images Found!")
print('To export the archive at an existing archive location please input complete path of existing archive'
      ' i.e. location ending with "/archive"')
exportLocation = input("Input the complete path where you want to export the archive *{ To export the archive at default location input 'DEFAULT' }: ")
if exportLocation == 'DEFAULT':
    exportLocation = os.getcwd()
count = 0
os.makedirs(exportLocation+'\\'+'archive',exist_ok=True)
for image in images:
    buildpath = directoryLocation+'\\'+image
    imgobj = ImageExif.getimageobj(buildpath,image)
    count = count+1
    os.makedirs(exportLocation+'\\archive'+imgobj.folder(),exist_ok=True)
    try:
        shutil.copy(src=buildpath, dst=exportLocation + '\\archive' + imgobj.folder())
    except:
        pass
if count == len(images):
    print('success!')