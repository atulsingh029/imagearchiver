# IMAGEARCHIVER #

**Tool to archive all the image files (jgp,jpeg,png) into date of creation based directory structure.**
### Dependency
*Python should be installed on the system*
* Pillow

### Installation
```
git clone https://github.com/atulsingh029/imagearchiver.git
```
```
cd imagearchiver
```
```
pip install -r requirements.txt
```

### Usage
###### All directory input should consist of complete path of the directory
* If all the files are in one source directory.
```
python imagearchiver.py source_directory destination_directory
```
* If files are in multiple directories create a text file (e.g. files.txt) and add all directories' complete path in that file.
```
python imagearchiver.py files.txt destination_directory
```
Text file example :
*suppose files are in 'D:\\folder1' and 'G:\\folder2'* 
 
 files.txt
```
D:\\folder1
G:\\folder2
```
