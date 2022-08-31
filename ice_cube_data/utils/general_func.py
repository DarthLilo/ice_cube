import imghdr
import struct
import json
from urllib import request
import bpy

from ice_cube import github_url

def isOldSkin(skin): #Checks if the specified skin is up to date (checks if image is 64x64 or 64x32)

    with open(skin, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(skin) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
    if height == 64:
        return False
    else:
        return True

def GetListIndex(strV = "", indexlist = []): #Gets the index of an item in a list
    indexlist_new = []
    for item in indexlist:
        string_item = str(item)
        string_item = (string_item.split(".")[0])
        indexlist_new.append(string_item)
    index = indexlist_new.index(strV)

    return index

def IsVersionUpdated(current): #Checks if the current version of Ice Cube is up to date
    cv = str(current)
    repo = json.loads(request.urlopen(github_url).read().decode())
    github_latest_vers = repo['tag_name']
    current_vers = str(cv.replace("(", ""))
    current_vers = str(current_vers.replace(")", ""))
    current_vers = str(current_vers.replace(",", ""))
    current_vers = int(current_vers.replace(" ", ""))
    latest_vers = int(github_latest_vers.replace(".", ""))
    if current_vers >= latest_vers:
        return True
    else:
        return False

def getIndexCustom(strV = "", indexlist = []):
        indexlist_new = []
        for item in indexlist:
            string_item = str(item)
            indexlist_new.append(string_item)
        index = indexlist_new.index(strV)

        return index

def BlenderVersConvert(version, has_v = False):
    new_version = []
    for number in version:
        new_version.append(str(number))

    new_version = ".".join(new_version)

    if has_v is True:
        new_version = f"v{new_version}"


    return new_version


classes = [
           ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__=="__main__":
    register()