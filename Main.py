#  Author : Atul Singh
#  Email  : atulsingh29@protonmail.com
#  Github : https://github.com/atulsingh029
import shutil
import ImageExif
import os


def main(src,dst):
    directoryLocation = src
    filesandfolders = os.listdir(directoryLocation)
    images = []
    for ff in filesandfolders:
        if os.path.isfile(directoryLocation + '/' + ff):
            if (ff.endswith('.jpg') or ff.endswith('.jpeg') or ff.endswith('.JPG') or ff.endswith('.JPEG')
                    or ff.endswith('.png') or ff.endswith('.PNG')):
                images.append(ff)
    print(str(len(images)) + " Images Found!")
    if len(images) == 0:
        exit()
    exportLocation = dst
    count = 0
    os.makedirs(exportLocation + '\\' + 'archive', exist_ok=True)
    for image in images:
        count = count + 1
        pcent = (count / len(images)) * 100
        output = 'Processing : [  ' + str(int(pcent)) + '% ]'
        print(output, end='')
        buildpath = directoryLocation + '\\' + image
        imgobj = ImageExif.getimageobj(buildpath, image)
        os.makedirs(exportLocation + '\\archive' + imgobj.folder(), exist_ok=True)
        try:
            if(os.path.exists(exportLocation+'\\archive'+imgobj.folder()+'\\'+image)):
                try:
                    print('\b' * len(output), end='')
                except:
                    pass
            else:
                shutil.copy(src=buildpath, dst=exportLocation + '\\archive' + imgobj.folder())
                try:
                    print('\b' * len(output), end='')
                except:
                    pass

        # If source and destination are same
        except shutil.SameFileError:
            print("Source and destination represents the same file.")

        # If there is any permission issue
        except PermissionError:
            print("Permission denied.")

        # Any other error


    if count == len(images):
        print('')
        print('success!')