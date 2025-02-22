import bpy, os

from ..constants import ICE_CUBE_DEFAULT, ICE_CUBE_10PX, ICE_CUBE_14PX

class ICECUBE_AppendIceCube(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.append_ice_cube'
    bl_label = "Add Ice Cube"

    def execute(self, context):
        section = "Collection"
        obj = "Ice Cube"
        
        directory = os.path.join(ICE_CUBE_DEFAULT,section)
        filepath = os.path.join(directory,obj)
        bpy.ops.wm.append(filepath=filepath,filename=obj,directory=directory,link=False,active_collection=True)

        return {'FINISHED'}

class ICECUBE_AppendIceCube10PX(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.append_ice_cube_10px'
    bl_label = "Add Ice Cube"

    def execute(self, context):
        section = "Collection"
        obj = "Ice Cube"
        
        directory = os.path.join(ICE_CUBE_10PX,section)
        filepath = os.path.join(directory,obj)
        bpy.ops.wm.append(filepath=filepath,filename=obj,directory=directory,link=False,active_collection=True)

        return {'FINISHED'}

class ICECUBE_AppendIceCube14PX(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.append_ice_cube_14px'
    bl_label = "Add Ice Cube"

    def execute(self, context):
        section = "Collection"
        obj = "Ice Cube"
        
        directory = os.path.join(ICE_CUBE_14PX,section)
        filepath = os.path.join(directory,obj)
        bpy.ops.wm.append(filepath=filepath,filename=obj,directory=directory,link=False,active_collection=True)

        return {'FINISHED'}