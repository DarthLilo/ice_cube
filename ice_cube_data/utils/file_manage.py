import bpy
import os
import shutil
import json

def getFiles(path): #returns a list of files in a specified dir
    dir = os.path.realpath(path);
    
    if os.path.exists(dir):
        dirs = [];

        for i in os.listdir(dir):
            dirs.append(i);

        return dirs;

def unpack_img(img): #unpacks a specified image
    if img.packed_files:
        if bpy.data.is_saved:
            return img.unpack()
        else:
            return img.unpack(method='USE_ORIGINAL')

def ClearDirectory(dir = ""): #completely clears a folder
    for folder in os.listdir(dir):
        filepath = os.path.join(dir, folder)
        filepath = os.path.normpath(filepath)
        shutil.rmtree(filepath)

def ClearDirectoryOfFiles(dir = ""): #completely clears a folder
    for folder in os.listdir(dir):
        filepath = os.path.join(dir, folder)
        filepath = os.path.normpath(filepath)
        try:
            if os.path.isfile(filepath) or os.path.islink(filepath):
                os.unlink(filepath)
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (filepath, e))

def GetRootFolder(path, folder_up): #Get a str to the root folder
    path = os.path.normpath(os.path.realpath(__file__))
    if path.__contains__("\\"):
        path = path.replace("\\","/")
    path = path.split("/")
    path.remove(path[len(path)-1])
    for i in range(folder_up):
        path.remove(path[len(path)-1])

    return path

def open_json(path):
    with open(path, 'r') as json_opener:
        json_data = json_opener.read()
    json_data = json.loads(json_data)

    return json_data


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