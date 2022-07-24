#Libraries
import datetime
import bpy
import os
from sys import platform
import pathlib
from bpy.props import EnumProperty
from ....ice_cube import print_informatin


from ice_cube import root_folder, dlc_id,dlc_type,dlc_author,dlc_date,dlc_enum_data

from ice_cube_data.utils.file_manage import getFiles


import ice_cube

if print_informatin:
    print(ice_cube.dlc_enum_data)


#creating backups list
backup_items = []
backups_folder = root_folder+"/backups"
backup_folder_scan = os.listdir(backups_folder)

if len(backup_folder_scan) >= 1:
    for backup in getFiles(backups_folder):
        backup_layout = (backup, backup, 'backup')
        if backup_items.__contains__(backup_layout) is False:
            backup_items.append(backup_layout)

bpy.types.Object.backups_list = EnumProperty(
    name = "Backup List",
    items = backup_items
)
bpy.types.Object.dlc_list = EnumProperty(
    name = "DLC List",
    items = dlc_enum_data
)

def downloads_UI(self, context, layout, obj):
    backups_folder = root_folder+"/backups"
    backup_folder_scan = os.listdir(backups_folder)
    box = layout.box()
    if platform == "darwin":
        b = box.row(align=True)
        b.label(text= "DOWNLOAD PANEL NOT SUPPORTED ON MAC OS!", icon='ERROR')
    else:
        virtual_ice_cube = root_folder+""
        virtual_ice_cube = os.path.normpath(virtual_ice_cube)
        if os.path.exists(backups_folder):
            pass
        else:
            os.mkdir(backups_folder)
            if print_informatin:
                print("Created Backups Folder")

        b = box.row(align=True)
        b.label(text= "Update Manager", icon='FILE_REFRESH')
        b = box.row(align=True)
        b.label(text="Do NOT close Blender while installing")
        b = box.row(align=True)
        if ice_cube.update_available == True:
            b.operator("install.update", text="Install Update", icon='MOD_WAVE')
        else:
            b.operator("check.updates", text="Check for Updates", icon='IMPORT')
        box = layout.box()
        b = box.row(align=True)
        b.label(text = "Backup Manager", icon='FILE_BACKUP')
        b = box.row(align=True)
        b.prop(obj, "backup_name", text="Backup Name", icon='FILE_BACKUP')
        b = box.row(align=True)
        if len(backup_folder_scan) >= 1:
            b.prop(obj, "backups_list",text="")
            b.operator("update.backups", text="",icon='FILE_REFRESH')
        b = box.row(align=True)
        bcreate = b.row(align=True)
        if len(backup_folder_scan) >= 1:
            bload = b.row(align=True)
            bdelete = b.row(align=True)
        bcreate.operator("create.backup", text="Create Backup")
        if len(backup_folder_scan) >= 1:
            bload.operator("load.backup", text="Load Backup")
            bdelete.operator("delete.backup", text="Delete Backup")
        b = box.row(align=True)
        if len(backup_folder_scan) >= 1:
            box = b.box()
            b1 = box.row(align=True)
            b1.label(text = "Selected Backup:")
            selected_backup = getattr(obj,"backups_list")
            creation_date = pathlib.Path(f"{backups_folder}/{selected_backup}").stat().st_mtime
            creation_date = str(datetime.datetime.fromtimestamp(creation_date)).split(" ")[0]
            b1 = box.row(align=True)
            b1.label(text = selected_backup, icon = 'FILE_BACKUP')
            b1.label(text = f"Created:  [{creation_date}]")




        #end of box
        


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
