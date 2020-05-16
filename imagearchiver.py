#  Author : Atul Singh
#  Email    : atulsingh29@protonmail.com
#  Github  : https://github.com/atulsingh029

import os,sys,Main

arguments = sys.argv
if arguments[1].endswith('.txt') and os.path.isfile(os.getcwd()+'/'+arguments[1]):
    files=open(os.getcwd()+'/'+arguments[1],'r')
    srclist = files.readlines()
    files.close()
    size = len(srclist)
    while(size != 0):
        src = srclist[size-1]
        src = src.replace('\n', '')
        print('Directory : ' + src)
        Main.main(src,arguments[2])
        size = size-1
else:
    Main.main(arguments[1],arguments[2])

