#Libraries
import bpy
import os
from bpy.props import EnumProperty

#Custom Libraries
from ice_cube import root_folder
from ice_cube_data.utils.ui_tools import CustomErrorBox
from ice_cube_data.utils.file_manage import getFiles

#File Variables
inventory_list = []
inv_files_list = []
count = 0

#File Definition
internalfiles = os.path.join(root_folder, "ice_cube_data/internal_files/user_packs/inventory")
user_packs = os.path.normpath(internalfiles)
get_test_files = getFiles(user_packs)

#Gets a list of assets in the "inventory" folder
for file in get_test_files:
    count += 1
    addition_map = ["asset_", str(count)]
    ID = "".join(addition_map)
    description = "Asset ID Number: " + ID
    test_thing = (ID, file, description)
    inventory_list.append(test_thing)
    inv_files_list.append(file)

#Append Asset Class
class append_asset(bpy.types.Operator):
    bl_idname = "append.asset"
    bl_label = "append asset"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):
        assets = {};
        obj = context.object

        #Tries to get a list of all files in [SELECTED ASSET PACK], if none is found it defaults to a backup.
        try:
            selected_file = inv_files_list[context.scene.get("selected_inv_asset")]
            asset_directory = root_folder+"/ice_cube_data/internal_files/user_packs/inventory/"+selected_file+"/assets"
            thumbnails_directory = root_folder+"/ice_cube_data/internal_files/user_packs/inventory/"+selected_file+"/thumbnails"
        except:
            selected_file = "important"
            asset_directory = root_folder+"/ice_cube_data/internal_files/"+selected_file+"/assets"
            thumbnails_directory = root_folder+"/ice_cube_data/internal_files/"+selected_file+"/thumbnails"
        asset_directory = os.path.normpath(asset_directory)
        thumbnails_directory = os.path.normpath(thumbnails_directory)

        dirs = getFiles(asset_directory)

        try:
            for dir in dirs:
                newDir = os.path.join(asset_directory, dir);

                for file in os.listdir(newDir):
                
                    newFile = os.path.join(newDir, file)
                    assets[dir] = newFile;
        except:
            CustomErrorBox(message="Unknown Error", title="Append Exception", icon='ERROR')

        #Gets the thumbnail data
        thumbnail = bpy.data.window_managers["WinMan"].inventory_preview
        thumbnailnopng = thumbnail.split(".")[0]
        
        #Sets up appending variables
        blendfile = f"{asset_directory}/{thumbnailnopng}/{thumbnailnopng}.blend"
        blendfile_name = thumbnailnopng+".blend"
        section = "Collection"
        obj = thumbnailnopng
        



        #Appends the rig using established variables before, if failed, give a custom error message
        try:
            filepath  = os.path.join(blendfile,section,obj)
            directory = os.path.join(blendfile,section)
            filename  = obj
            bpy.ops.wm.append(filepath=filepath,filename=filename,directory=directory,link=False,active_collection=True)
            CustomErrorBox("Appended \""+thumbnailnopng+"\" from \""+blendfile_name+"\" in \""+selected_file+"\"", "Operation Completed", 'CHECKMARK')
        except:
            CustomErrorBox("An unknown error has occured.", "Unknown Error", 'ERROR')

        return{'FINISHED'}


#Attempts to create the enumerator property, if it fails it goes to a backup version.
try:
    bpy.types.Scene.selected_inv_asset = EnumProperty(
        name = "Selected Pack",
        default = 'asset_1',
        items = inventory_list
    )
except:
    bpy.types.Scene.selected_inv_asset = EnumProperty(
        name = "Selected Pack",
        default = 'asset_1',
        items = [('asset_1', "NO ASSETS FOUND", 'Please install or create an asset!')]
    )



classes = [
    append_asset,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__=="__main__":
    register()