import bpy
from mathutils import Vector, Quaternion

from ..ice_cube_selectors import GetBoneCollection

class CustomDefaultOperator():
    def SetDefaultPose(self, context):

        rig = context.object
        original_mode = bpy.context.mode

        for bone in rig.pose.bones:
            
            if "ice_cube_override_bone" in bone:
                continue

            loc = bone.location
            rot = bone.rotation_quaternion
            scale = bone.scale

            reset_loc = False
            reset_rot = False
            reset_scale = False

            if loc != Vector((0,0,0)):
                reset_loc = True
            if rot != Quaternion((1,0,0,0)):
                reset_rot = True
            if scale != Vector((1,1,1)):
                reset_scale = True

            if not any([reset_loc, reset_rot, reset_scale]):
                continue
            
            if not bpy.context.mode == "EDIT_ARMATURE":
                bpy.ops.object.mode_set(mode='EDIT')
            
            edit_bone = rig.data.edit_bones.get(bone.name)
            new_bone_name = CustomDefaultOperator.duplicate_bone(rig,edit_bone,bone)

            bpy.ops.object.mode_set(mode='POSE')
            new_bone = rig.pose.bones[new_bone_name]
            new_bone.matrix_basis = bone.matrix_basis.copy()

            bone.location = (0,0,0)
            bone.rotation_quaternion = Quaternion((1,0,0,0))
            bone.scale = (1,1,1)
            bone["ice_cube_override_bone"] = new_bone_name
            new_bone["ice_cube_override_bone"] = "ice_cube_override_bone"

            if reset_scale:
                CustomDefaultOperator.new_copy_scale(bone,rig,new_bone,f"{bone.name}_{new_bone_name}_SCALE")
            
            if reset_rot:
                CustomDefaultOperator.new_copy_rotation(bone,rig,new_bone,f"{bone.name}_{new_bone_name}_ROTATION")
            
            if reset_loc:
                CustomDefaultOperator.new_copy_location(bone,rig,new_bone,f"{bone.name}_{new_bone_name}_LOCATION")
            
            collections = rig.data.collections_all
            custom_default = GetBoneCollection(collections,'ice_cube.custom_default')
            custom_default.assign(new_bone)

            print(f"Created override bone for {bone.name}")
        
        if original_mode == "POSE":
            bpy.ops.object.mode_set(mode='POSE')
        else:
            bpy.ops.object.mode_set(mode='OBJECT')





        return {'FINISHED'}
    
    def ResetDefaultPose(self, context):
        rig = context.object
        original_mode = bpy.context.mode

        for bone in rig.pose.bones:

            if not "ice_cube_override_bone" in bone:
                continue
            override_data = bone['ice_cube_override_bone']
            if override_data == "ice_cube_override_bone":
                continue

            location_constraint = bone.constraints.get(f"{bone.name}_{override_data}_LOCATION")
            rotation_constraint = bone.constraints.get(f"{bone.name}_{override_data}_ROTATION")
            scale_constraint = bone.constraints.get(f"{bone.name}_{override_data}_SCALE")

            for constraint in [location_constraint, rotation_constraint, scale_constraint]:
                if not constraint:
                    continue
                context_override = {'active_pose_bone':bone}
                with context.temp_override(**context_override):
                    bpy.ops.constraint.apply(constraint=constraint.name, owner='BONE')
            
            del bone["ice_cube_override_bone"]
        
        for bone in rig.pose.bones:
            if not 'ice_cube_override_bone' in bone:
                continue
            override_data = bone['ice_cube_override_bone']

            if not bpy.context.mode == 'EDIT_ARMATURE':
                bpy.ops.object.mode_set(mode='EDIT')
            
            if override_data == 'ice_cube_override_bone':
                edit_bone = rig.data.edit_bones.get(bone.name)
                if edit_bone: rig.data.edit_bones.remove(edit_bone)
        
        if original_mode == "POSE":
            bpy.ops.object.mode_set(mode='POSE')
        else:
            bpy.ops.object.mode_set(mode='OBJECT')

        return {'FINISHED'}

    def duplicate_bone(rig, edit_bone, bone):
        new_bone = rig.data.edit_bones.new(f"{bone.name}_override_bone")
        new_bone.head = edit_bone.head
        new_bone.tail = edit_bone.tail
        new_bone.roll = edit_bone.roll
        return new_bone.name
    
    def new_copy_location(source, target, subtarget, name):
        copy_location = source.constraints.new('COPY_LOCATION')
        copy_location.name = name
        copy_location.target = target
        copy_location.subtarget = subtarget.name
        copy_location.target_space = 'LOCAL'
        copy_location.owner_space = 'LOCAL'
        copy_location.use_offset = True
        context_override = {'active_pose_bone':source}
        with bpy.context.temp_override(**context_override):
            bpy.ops.constraint.move_to_index(constraint=copy_location.name,owner='BONE',index=0)
    
    def new_copy_rotation(source, target, subtarget, name):
        copy_rotation = source.constraints.new('COPY_ROTATION')
        copy_rotation.name = name
        copy_rotation.target = target
        copy_rotation.subtarget = subtarget.name
        copy_rotation.target_space = 'LOCAL'
        copy_rotation.owner_space = 'LOCAL'
        copy_rotation.mix_mode = 'BEFORE'
        context_override = {'active_pose_bone':source}
        with bpy.context.temp_override(**context_override):
            bpy.ops.constraint.move_to_index(constraint=copy_rotation.name,owner='BONE',index=0)
    
    def new_copy_scale(source, target, subtarget, name):
        copy_scale = source.constraints.new('COPY_SCALE')
        copy_scale.name = name
        copy_scale.target = target
        copy_scale.subtarget = subtarget.name
        copy_scale.target_space = 'LOCAL'
        copy_scale.owner_space = 'LOCAL'
        copy_scale.use_offset = True
        context_override = {'active_pose_bone':source}
        with bpy.context.temp_override(**context_override):
            bpy.ops.constraint.move_to_index(constraint=copy_scale.name,owner='BONE',index=0)

class ICECUBE_SET_CUSTOM_DEFAULT(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.set_custom_default_pose'
    bl_label = "Update Rest Pose"

    def execute(self, context):

        CustomDefaultOperator.ResetDefaultPose(self,context)
        CustomDefaultOperator.SetDefaultPose(self,context)

        return {'FINISHED'}

class ICECUBE_RESET_CUSTOM_DEFAULT(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.reset_custom_default_pose'
    bl_label = "Reset Rest Pose"

    def execute(self, context):

        CustomDefaultOperator.ResetDefaultPose(self,context)

        return {'FINISHED'}
