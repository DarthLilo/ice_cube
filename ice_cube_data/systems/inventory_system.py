#Libraries
import bpy
import os
from bpy.props import EnumProperty

#Custom Libraries
from ice_cube import root_folder
from ice_cube_data.utils.ui_tools import CustomErrorBox
from ice_cube_data.utils.file_manage import getFiles

#File Variables
asset_pack_list = []
asset_pack_names = []

#File Definition
internalfiles = os.path.join(root_folder, "ice_cube_data/internal_files/user_packs/inventory")
user_packs = os.path.normpath(internalfiles)

def RefreshInvList():
    items = []
    items = asset_pack_list
    return items

bpy.types.Scene.selected_inv_asset = EnumProperty(
        name = "Selected Pack",
        items = [('NONE', 'REFRESH','REFRESH')]
        )

#Gets a list of assets in the "inventory" folder
class refresh_inventory_list(bpy.types.Operator):
    bl_idname = "refresh.inv_list"
    bl_label = "refresh inv list"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):
        #Clearing the old lists
        asset_pack_list.clear()
        asset_pack_names.clear()
        
        #variables
        count = 1

        #Updating the list of installed packs
        for file in getFiles(user_packs):
            description = f"Asset ID: {count}"
            item_descriptor = (file, file, description)
            asset_pack_list.append(item_descriptor)
            asset_pack_names.append(file)
            count += 1
        
        
        #Drawing the custom property
        bpy.types.Scene.selected_inv_asset = EnumProperty(
        name = "Selected Pack",
        items = RefreshInvList()
        )

        try:
            context.scene.selected_inv_asset = asset_pack_names[0]
        except:
            pass

        return{'FINISHED'}

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
            selected_file = context.scene.selected_inv_asset
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




classes = [
    refresh_inventory_list,
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