#Libraries
import datetime
import bpy
import os
from sys import platform
import pathlib
from bpy.props import EnumProperty


from ice_cube import root_folder, dlc_id,dlc_type,dlc_author,dlc_date,dlc_enum_data

from ice_cube_data.utils.file_manage import getFiles
from ice_cube_data.utils.selectors import isRigSelected


import ice_cube


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

        b = box.row(align=True)
        b.label(text= "Update Manager", icon='FILE_REFRESH')
        b = box.row(align=True)
        b.label(text="Do NOT close Blender while installing")
        b = box.row(align=True)
        if ice_cube.update_available == True:
            b.operator("install.update", text="Install Update", icon='MOD_WAVE')
        else:
            b.operator("ice_cube_check.updates", text="Check for Updates", icon='IMPORT')
        
        box = layout.box()
        box.label(text = "Backup Manager", icon='FILE_FOLDER')
        rig = isRigSelected(context)
        b = box.row(align=True)
        b.prop(obj, "backup_name", text="Backup Name", icon='FILE_BACKUP')
        b = box.row(align=True)
        b.template_list("IC_backups_list_i", "", rig, "ic_backups_i", rig, "ic_backups_active_index")
        colb = b.column()
        colb.operator("create.backup", text="", icon='ADD')
        colb.operator("delete.backup", text="", icon='REMOVE')
        colb.operator("refresh.backup", text="", icon='FILE_REFRESH')
        colb.operator("load.backup", text="", icon='IMPORT')



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