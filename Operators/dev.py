import bpy, os

from ..constants import ICE_CUBE_DEFAULT, ICE_CUBE_14PX, ICE_CUBE_10PX

class ICECUBE_DEVupdateIceCube(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.dev_update_ice_cube'
    bl_label = "DEV ONLY Update Ice Cube"

    def execute(self, context):
        bpy.ops.wm.save_as_mainfile(filepath=ICE_CUBE_DEFAULT,copy=True)
        blend1 = ICE_CUBE_DEFAULT + "1"
        if os.path.exists(blend1):
            os.remove(blend1)
        
        return {'FINISHED'}

class ICECUBE_DEVupdateIceCube14px(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.dev_update_ice_cube_14px'
    bl_label = "DEV ONLY Update Ice Cube 14PX"

    def execute(self, context):
        bpy.ops.wm.save_as_mainfile(filepath=ICE_CUBE_14PX,copy=True)
        blend1 = ICE_CUBE_14PX + "1"
        if os.path.exists(blend1):
            os.remove(blend1)
        
        return {'FINISHED'}

class ICECUBE_DEVupdateIceCube10px(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.dev_update_ice_cube_10px'
    bl_label = "DEV ONLY Update Ice Cube 10PX"

    def execute(self, context):
        bpy.ops.wm.save_as_mainfile(filepath=ICE_CUBE_10PX,copy=True)
        blend1 = ICE_CUBE_10PX + "1"
        if os.path.exists(blend1):
            os.remove(blend1)
        
        return {'FINISHED'}