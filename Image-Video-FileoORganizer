import time
import datetime
import os


# find the year of modificaition
def mtime(_path):
    return str(datetime.datetime.fromtimestamp(os.path.getmtime(_path)).year)

# define the file kindness from the filepath
def filekind(_path):
    filename=os.path.basename(_path)
    
    if "." not in filename:
        return "none"
    
    temp=filename.split(".")[-1]
    temp=temp.lower()

    if temp=="jpg" or temp=="jpeg" or temp=="png":
        return "image"
        
    elif temp=="mp4" or temp=="avi" or temp=="3gp" or temp=="mpeg" or temp=="mkv" or temp=="wmv" or temp=="mov":
        return "film"
        
    else:
        return "none"
        
#return the files of  specific dir in fullpath form
def filefulllist(_path):
    temp=[]
    adresses=list(os.walk(_path))
    for item in adresses:
        for files in item[2]:
            temp.append(os.path.normpath("/".join([item[0],files])))
            pass
        pass   
        
    return temp



import sys
src=sys.argv[1]
dist=sys.argv[2]

if not os.path.isdir(dist):
    os.mkdir(dist)
    pass
listfile=filefulllist(src)
for file in listfile:
    # check file kind
    kind=filekind(file)
    if kind!="none":
        _time=mtime(file)
        if not os.path.isdir(dist+"/%s"%_time):
            os.mkdir(dist+"/%s"%_time)
            pass
        if kind=="image":
            if not os.path.isdir(dist+"/%s"%_time+"/photos"):
                os.mkdir(dist+"/%s"%_time+"/photos")
            pass
            with open(file, 'rb') as a:
                data = a.read()
                with open(dist+"/%s"%_time+"/photos/"+os.path.basename(file), 'wb') as b:
                    b.write(data)

           
        else:
            if not os.path.isdir(dist+"/%s"%_time+"/videos"):
                os.mkdir(dist+"/%s"%_time+"/videos")
            pass
            with open(file, 'rb') as a:
                data = a.read()
                with open(dist+"/%s"%_time+"/videos/"+os.path.basename(file), 'wb') as b:
                    b.write(data)

        pass
    pass


    
