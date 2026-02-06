import bpy

from ..ice_cube_selectors import GetBone, GetBoneCollection

class IK_FK_Operations():
    def SNAP_IK_TO_FK(IK_CONTROL,IK_TARGET,IK_POLE,IK_POLE_TARGET):
        IK_CONTROL.matrix = IK_TARGET.matrix.copy()
        bpy.context.view_layer.update()

        IK_POLE.matrix = IK_POLE_TARGET.matrix.copy()
        bpy.context.view_layer.update()
    
    def SNAP_FK_TO_IK(IK_UPPER,IK_LOWER,IK_CONTROL,FK_UPPER,FK_LOWER,FK_ANKLE,EndLock):
        FK_UPPER.matrix = IK_UPPER.matrix.copy()
        bpy.context.view_layer.update()

        FK_LOWER.matrix = IK_LOWER.matrix.copy()
        bpy.context.view_layer.update()
        
        if EndLock:
            FK_ANKLE.matrix = IK_CONTROL.matrix.copy()
            bpy.context.view_layer.update()
    
    def UpdateBoneLayer(collections, bone_layer_id,state):
        bone_layer = GetBoneCollection(collections,bone_layer_id)
        bone_layer.is_visible = state
    
    def CreateKeyframe(bone, frame):
        bone.keyframe_insert("location",frame=frame)
        bone.keyframe_insert("rotation_quaternion",frame=frame)
        bone.keyframe_insert("scale",frame=frame)
        print(f"Created keyframe for bone {bone.name} at frame {frame}")
    
    def CreatePropertyKeyframe(rig,property,frame):
        rig.keyframe_insert(property,frame=frame)
    
    def CreateKeyframeGroup(bones,frame):
        for bone in bones:
            IK_FK_Operations.CreateKeyframe(bone,frame)

class ICECUBE_Convert_FK_TO_IK_LEG_L(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.leg_l_ik_to_fk'
    bl_label = "Convert to IK (Leg L)"

    def execute(self, context):

        rig = context.object
        scene_frame = context.scene.frame_current

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Left Leg Upper FK'),
                    GetBone(rig,'Left Leg Lower FK'),
                    GetBone(rig,'Left Leg Ankle Control'),
                    GetBone(rig,'Left Leg IK'),
                    GetBone(rig,'Left Leg IK Pole'),
                    GetBone(rig,'Left Leg Upper IK Parent')
                ],
                scene_frame-1
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"left_leg_ik",scene_frame-1)

        bones = [
            GetBone(rig,'Left Leg IK'),
            GetBone(rig,'Left Leg IK Target'),
            GetBone(rig,'Left Leg IK Pole'),
            GetBone(rig,'Left Leg IK Pole Target')
        ]
        
        #Brings the IK bones to FK and disables IK
        IK_FK_Operations.SNAP_IK_TO_FK(*bones)
        rig.left_leg_ik = 1
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.left_leg_ik",True)
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.left_leg_fk",False)

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Left Leg Upper FK'),
                    GetBone(rig,'Left Leg Lower FK'),
                    GetBone(rig,'Left Leg Ankle Control'),
                    GetBone(rig,'Left Leg IK'),
                    GetBone(rig,'Left Leg IK Pole'),
                    GetBone(rig,'Left Leg Upper IK Parent')
                ],
                scene_frame
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"left_leg_ik",scene_frame)

        return {'FINISHED'}

class ICECUBE_Convert_IK_TO_FK_LEG_L(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.leg_l_fk_to_ik'
    bl_label = "Convert to FK (Leg L)"

    def execute(self, context):

        rig = context.object
        scene_frame = context.scene.frame_current

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Left Leg Upper FK'),
                    GetBone(rig,'Left Leg Lower FK'),
                    GetBone(rig,'Left Leg Ankle Control'),
                    GetBone(rig,'Left Leg IK'),
                    GetBone(rig,'Left Leg IK Pole'),
                    GetBone(rig,'Left Leg Upper IK Parent')
                ],
                scene_frame-1
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"left_leg_ik",scene_frame-1)

        bones = [
            GetBone(rig,'Left Leg Upper IK'),
            GetBone(rig,'Left Leg Lower IK'),
            GetBone(rig,'Left Leg Inner IK'),
            GetBone(rig,'Left Leg Upper FK'),
            GetBone(rig,'Left Leg Lower FK'),
            GetBone(rig,'Left Leg Ankle Control')
        ]
        
        #Brings the FK bones to IK and disables IK
        IK_FK_Operations.SNAP_FK_TO_IK(*bones,rig.left_leg_ankle_lock)
        rig.left_leg_ik = 0
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.left_leg_ik",False)
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.left_leg_fk",True)

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Left Leg Upper FK'),
                    GetBone(rig,'Left Leg Lower FK'),
                    GetBone(rig,'Left Leg Ankle Control'),
                    GetBone(rig,'Left Leg IK'),
                    GetBone(rig,'Left Leg IK Pole'),
                    GetBone(rig,'Left Leg Upper IK Parent')
                ],
                scene_frame
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"left_leg_ik",scene_frame)

        return {'FINISHED'}

class ICECUBE_Convert_FK_TO_IK_LEG_R(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.leg_r_ik_to_fk'
    bl_label = "Convert to IK (Leg R)"

    def execute(self, context):

        rig = context.object
        scene_frame = context.scene.frame_current

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Right Leg Upper FK'),
                    GetBone(rig,'Right Leg Lower FK'),
                    GetBone(rig,'Right Leg Ankle Control'),
                    GetBone(rig,'Right Leg IK'),
                    GetBone(rig,'Right Leg IK Pole'),
                    GetBone(rig,'Right Leg Upper IK Parent')
                ],
                scene_frame-1
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"right_leg_ik",scene_frame-1)

        bones = [
            GetBone(rig,'Right Leg IK'),
            GetBone(rig,'Right Leg IK Target'),
            GetBone(rig,'Right Leg IK Pole'),
            GetBone(rig,'Right Leg IK Pole Target')
        ]
        
        #Brings the IK bones to FK and disables IK
        IK_FK_Operations.SNAP_IK_TO_FK(*bones)
        rig.right_leg_ik = 1
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.right_leg_ik",True)
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.right_leg_fk",False)

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Right Leg Upper FK'),
                    GetBone(rig,'Right Leg Lower FK'),
                    GetBone(rig,'Right Leg Ankle Control'),
                    GetBone(rig,'Right Leg IK'),
                    GetBone(rig,'Right Leg IK Pole'),
                    GetBone(rig,'Right Leg Upper IK Parent')
                ],
                scene_frame
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"right_leg_ik",scene_frame)

        return {'FINISHED'}

class ICECUBE_Convert_IK_TO_FK_LEG_R(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.leg_r_fk_to_ik'
    bl_label = "Convert to FK (Leg R)"

    def execute(self, context):

        rig = context.object
        scene_frame = context.scene.frame_current

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Right Leg Upper FK'),
                    GetBone(rig,'Right Leg Lower FK'),
                    GetBone(rig,'Right Leg Ankle Control'),
                    GetBone(rig,'Right Leg IK'),
                    GetBone(rig,'Right Leg IK Pole'),
                    GetBone(rig,'Right Leg Upper IK Parent')
                ],
                scene_frame-1
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"right_leg_ik",scene_frame-1)

        bones = [
            GetBone(rig,'Right Leg Upper IK'),
            GetBone(rig,'Right Leg Lower IK'),
            GetBone(rig,'Right Leg Inner IK'),
            GetBone(rig,'Right Leg Upper FK'),
            GetBone(rig,'Right Leg Lower FK'),
            GetBone(rig,'Right Leg Ankle Control')
        ]
        
        #Brings the FK bones to IK and disables IK
        IK_FK_Operations.SNAP_FK_TO_IK(*bones,rig.right_leg_ankle_lock)
        rig.right_leg_ik = 0
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.right_leg_ik",False)
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.right_leg_fk",True)

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Right Leg Upper FK'),
                    GetBone(rig,'Right Leg Lower FK'),
                    GetBone(rig,'Right Leg Ankle Control'),
                    GetBone(rig,'Right Leg IK'),
                    GetBone(rig,'Right Leg IK Pole'),
                    GetBone(rig,'Right Leg Upper IK Parent')
                ],
                scene_frame
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"right_leg_ik",scene_frame)

        return {'FINISHED'}

class ICECUBE_Convert_FK_TO_IK_ARM_L(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.arm_l_ik_to_fk'
    bl_label = "Convert to IK (Arm L)"

    def execute(self, context):

        rig = context.object
        scene_frame = context.scene.frame_current

        bones = [
            GetBone(rig,'Left Arm IK'),
            GetBone(rig,'Left Arm IK Target'),
            GetBone(rig,'Left Arm IK Pole'),
            GetBone(rig,'Left Arm IK Pole Target')
        ]

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Left Arm Upper FK'),
                    GetBone(rig,'Left Arm Lower FK'),
                    GetBone(rig,'Left Arm Wrist Control'),
                    GetBone(rig,'Left Arm IK'),
                    GetBone(rig,'Left Arm IK Pole'),
                    GetBone(rig,'Left Arm Upper IK Parent')
                ],
                scene_frame-1
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"left_arm_ik",scene_frame-1)
        
        #Brings the IK bones to FK and disables IK
        IK_FK_Operations.SNAP_IK_TO_FK(*bones)
        rig.left_arm_ik = 1
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.left_arm_ik",True)
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.left_arm_fk",False)

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Left Arm Upper FK'),
                    GetBone(rig,'Left Arm Lower FK'),
                    GetBone(rig,'Left Arm Wrist Control'),
                    GetBone(rig,'Left Arm IK'),
                    GetBone(rig,'Left Arm IK Pole'),
                    GetBone(rig,'Left Arm Upper IK Parent')
                ],
                scene_frame
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"left_arm_ik",scene_frame)


        return {'FINISHED'}

class ICECUBE_Convert_IK_TO_FK_ARM_L(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.arm_l_fk_to_ik'
    bl_label = "Convert to FK (Arm L)"

    def execute(self, context):

        rig = context.object
        scene_frame = context.scene.frame_current

        bones = [
            GetBone(rig,'Left Arm Upper IK'),
            GetBone(rig,'Left Arm Lower IK'),
            GetBone(rig,'Left Arm IK Inner'),
            GetBone(rig,'Left Arm Upper FK'),
            GetBone(rig,'Left Arm Lower FK'),
            GetBone(rig,'Left Arm Wrist Control')
        ]

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Left Arm Upper FK'),
                    GetBone(rig,'Left Arm Lower FK'),
                    GetBone(rig,'Left Arm Wrist Control'),
                    GetBone(rig,'Left Arm IK'),
                    GetBone(rig,'Left Arm IK Pole'),
                ],
                scene_frame-1
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"left_arm_ik",scene_frame-1)
        
        #Brings the FK bones to IK and disables IK
        IK_FK_Operations.SNAP_FK_TO_IK(*bones,rig.left_arm_wrist_lock)
        rig.left_arm_ik = 0
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.left_arm_ik",False)
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.left_arm_fk",True)

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Left Arm Upper FK'),
                    GetBone(rig,'Left Arm Lower FK'),
                    GetBone(rig,'Left Arm Wrist Control'),
                    GetBone(rig,'Left Arm IK'),
                    GetBone(rig,'Left Arm IK Pole'),
                ],
                scene_frame
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"left_arm_ik",scene_frame)

        return {'FINISHED'}

class ICECUBE_Convert_FK_TO_IK_ARM_R(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.arm_r_ik_to_fk'
    bl_label = "Convert to IK (Arm R)"

    def execute(self, context):

        rig = context.object
        scene_frame = context.scene.frame_current

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Right Arm Upper FK'),
                    GetBone(rig,'Right Arm Lower FK'),
                    GetBone(rig,'Right Arm Wrist Control'),
                    GetBone(rig,'Right Arm IK'),
                    GetBone(rig,'Right Arm IK Pole'),
                    GetBone(rig,'Right Arm Upper IK Parent')
                ],
                scene_frame-1
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"right_arm_ik",scene_frame-1)

        bones = [
            GetBone(rig,'Right Arm IK'),
            GetBone(rig,'Right Arm IK Target'),
            GetBone(rig,'Right Arm IK Pole'),
            GetBone(rig,'Right Arm IK Pole Target')
        ]
        
        #Brings the IK bones to FK and disables IK
        IK_FK_Operations.SNAP_IK_TO_FK(*bones)
        rig.right_arm_ik = 1
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.right_arm_ik",True)
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.right_arm_fk",False)

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Right Arm Upper FK'),
                    GetBone(rig,'Right Arm Lower FK'),
                    GetBone(rig,'Right Arm Wrist Control'),
                    GetBone(rig,'Right Arm IK'),
                    GetBone(rig,'Right Arm IK Pole'),
                ],
                scene_frame
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"right_arm_ik",scene_frame)

        return {'FINISHED'}

class ICECUBE_Convert_IK_TO_FK_ARM_R(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.arm_r_fk_to_ik'
    bl_label = "Convert to FK (Arm R)"

    def execute(self, context):

        rig = context.object

        scene_frame = context.scene.frame_current

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Right Arm Upper FK'),
                    GetBone(rig,'Right Arm Lower FK'),
                    GetBone(rig,'Right Arm Wrist Control'),
                    GetBone(rig,'Right Arm IK'),
                    GetBone(rig,'Right Arm IK Pole'),
                    GetBone(rig,'Right Arm Upper IK Parent')
                ],
                scene_frame-1
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"right_arm_ik",scene_frame-1)

        bones = [
            GetBone(rig,'Right Arm Upper IK'),
            GetBone(rig,'Right Arm Lower IK'),
            GetBone(rig,'Right Arm IK Inner'),
            GetBone(rig,'Right Arm Upper FK'),
            GetBone(rig,'Right Arm Lower FK'),
            GetBone(rig,'Right Arm Wrist Control')
        ]
        
        #Brings the FK bones to IK and disables IK
        IK_FK_Operations.SNAP_FK_TO_IK(*bones,rig.right_arm_wrist_lock)
        rig.right_arm_ik = 0
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.right_arm_ik",False)
        IK_FK_Operations.UpdateBoneLayer(context.active_object.data.collections_all,"ice_cube.right_arm_fk",True)

        if rig.ik_fk_keyframe:
            IK_FK_Operations.CreateKeyframeGroup(
                [
                    GetBone(rig,'Right Arm Upper FK'),
                    GetBone(rig,'Right Arm Lower FK'),
                    GetBone(rig,'Right Arm Wrist Control'),
                    GetBone(rig,'Right Arm IK'),
                    GetBone(rig,'Right Arm IK Pole'),
                ],
                scene_frame
            )
            IK_FK_Operations.CreatePropertyKeyframe(rig,"right_arm_ik",scene_frame)

        return {'FINISHED'}