import imghdr
import struct
import json
from urllib import request
import bpy
from mathutils import Matrix, Vector, Quaternion
import aud
import os

from ice_cube import github_url, root_folder, settings_file

from ice_cube_data.utils.selectors import isRigSelected, mat_holder_func, eye_mesh
from ice_cube_data.utils.ui_tools import CustomErrorBox
from ice_cube_data.utils.file_manage import open_json

def badToTheBone():
    try:
        bad_to_the_bone = f"{root_folder}/ice_cube_data/internal_files/bad_to_the_bone.mp3"
        sound = aud.Sound(bad_to_the_bone)
        device = aud.Device()
        handle = device.play(sound)
    except:
        pass

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

def IC_FKIK_Switch(context, type, limb):

    rig = isRigSelected(context)
    bones = rig.pose.bones

    #FK BONES
    FK_L_upper = bones["Arm Upper L"]
    FK_L_lower = bones["Arm Lower L"]
    FK_L_end   = bones["Arm IK (FK TRACKING) L"]
    FK_R_upper = bones["Arm Upper R"]
    FK_R_lower = bones["Arm Lower R"]
    FK_R_end   = bones["Arm IK (FK TRACKING) R"]

    Leg_FK_L_upper = bones["Leg Upper L"]
    Leg_FK_L_lower = bones["Leg Lower L"]
    Leg_FK_L_end   = bones["Leg IK (FK TRACKING) L"]
    Leg_FK_R_upper = bones["Leg Upper R"]
    Leg_FK_R_lower = bones["Leg Lower R"]
    Leg_FK_R_end   = bones["Leg IK (FK TRACKING) R"]

    #IK BONES
    IK_L_upper =bones["Arm Upper IK L"]
    IK_L_lower =bones["Arm Lower IK L"]
    IK_L_control =bones["Arm IK L"]
    IK_L_pole =bones["Arm IK Pole L"]
    IK_R_upper =bones["Arm Upper IK R"]
    IK_R_lower =bones["Arm Lower IK R"]
    IK_R_control =bones["Arm IK R"]
    IK_R_pole =bones["Arm IK Pole R"]

    Leg_IK_L_upper =bones["Leg Upper IK L"]
    Leg_IK_L_lower =bones["Leg Lower IK L"]
    Leg_IK_L_control =bones["Leg IK L"]
    Leg_IK_L_pole =bones["Leg IK Pole L"]
    Leg_IK_R_upper =bones["Leg Upper IK R"]
    Leg_IK_R_lower =bones["Leg Lower IK R"]
    Leg_IK_R_control =bones["Leg IK R"]
    Leg_IK_R_pole =bones["Leg IK Pole R"]

    if type == "IK_TO_FK":

        if limb == "ARM_R":
            FK_R_upper.matrix = IK_R_upper.matrix
            bpy.context.view_layer.update()

            FK_R_lower.matrix = IK_R_lower.matrix
            bpy.context.view_layer.update()

            context.object.r_arm_ik = False

        elif limb == "ARM_L":
            FK_L_upper.matrix = IK_L_upper.matrix
            bpy.context.view_layer.update()

            FK_L_lower.matrix = IK_L_lower.matrix
            bpy.context.view_layer.update()

            context.object.l_arm_ik = False
        
        elif limb == "LEG_R":
            Leg_FK_R_upper.matrix = Leg_IK_R_upper.matrix
            bpy.context.view_layer.update()

            Leg_FK_R_lower.matrix = Leg_IK_R_lower.matrix
            bpy.context.view_layer.update()

            context.object.r_leg_ik = False

        elif limb == "LEG_L":
            Leg_FK_L_upper.matrix = Leg_IK_L_upper.matrix
            bpy.context.view_layer.update()

            Leg_FK_L_lower.matrix = Leg_IK_L_lower.matrix
            bpy.context.view_layer.update()

            context.object.l_leg_ik = False

        

    elif type == "FK_TO_IK":
        if limb == "ARM_R":
            IK_relative_to_FK_R = FK_R_end.bone.matrix_local.inverted() @ IK_R_control.bone.matrix_local
            IK_R_control.matrix = FK_R_end.matrix @ IK_relative_to_FK_R
            bpy.context.view_layer.update()

            PV_normal_R = ((FK_R_lower.vector.normalized() + FK_R_upper.vector.normalized() * -1)).normalized()
            PV_matrix_loc_R = FK_R_lower.matrix.to_translation() + (PV_normal_R * -0.2)
            PV_matrix_R = Matrix.LocRotScale(PV_matrix_loc_R, IK_R_pole.matrix.to_quaternion(), None)
            IK_R_pole.matrix = PV_matrix_R

            context.object.r_arm_ik = True

            FK_R_upper.rotation_quaternion = [1,0,0,0]
            FK_R_lower.rotation_quaternion = [1,0,0,0]


        elif limb == "ARM_L":
            IK_relative_to_FK_L = FK_L_end.bone.matrix_local.inverted() @ IK_L_control.bone.matrix_local
            IK_L_control.matrix = FK_L_end.matrix @ IK_relative_to_FK_L
            bpy.context.view_layer.update()

            PV_normal_L = ((FK_L_lower.vector.normalized() + FK_L_upper.vector.normalized() * -1)).normalized()
            PV_matrix_loc_L = FK_L_lower.matrix.to_translation() + (PV_normal_L * -0.2)
            PV_matrix_L = Matrix.LocRotScale(PV_matrix_loc_L, IK_L_pole.matrix.to_quaternion(), None)
            IK_L_pole.matrix = PV_matrix_L

            context.object.l_arm_ik = True

            FK_L_upper.rotation_quaternion = [1,0,0,0]
            FK_L_lower.rotation_quaternion = [1,0,0,0]
        
        elif limb == "LEG_R":
            Leg_IK_relative_to_FK_R = Leg_FK_R_end.bone.matrix_local.inverted() @ Leg_IK_R_control.bone.matrix_local
            Leg_IK_R_control.matrix = Leg_FK_R_end.matrix @ Leg_IK_relative_to_FK_R
            bpy.context.view_layer.update()

            Leg_PV_normal_R = ((Leg_FK_R_lower.vector.normalized() + Leg_FK_R_upper.vector.normalized() * -1)).normalized()
            Leg_PV_matrix_loc_R = Leg_FK_R_lower.matrix.to_translation() + (Leg_PV_normal_R * -0.2)
            Leg_PV_matrix_R = Matrix.LocRotScale(Leg_PV_matrix_loc_R, Leg_IK_R_pole.matrix.to_quaternion(), None)
            Leg_IK_R_pole.matrix = Leg_PV_matrix_R

            context.object.r_leg_ik = True

            Leg_FK_R_upper.rotation_quaternion = [1,0,0,0]
            Leg_FK_R_lower.rotation_quaternion = [1,0,0,0]
        
        elif limb == "LEG_L":
            

            Leg_IK_relative_to_FK_L = Leg_FK_L_end.bone.matrix_local.inverted() @ Leg_IK_L_control.bone.matrix_local
            Leg_IK_L_control.matrix = Leg_FK_L_end.matrix @ Leg_IK_relative_to_FK_L
            bpy.context.view_layer.update()

            Leg_PV_normal_L = ((Leg_FK_L_lower.vector.normalized() + Leg_FK_L_upper.vector.normalized() * -1)).normalized()
            Leg_PV_matrix_loc_L = Leg_FK_L_lower.matrix.to_translation() + (Leg_PV_normal_L * -0.2)
            Leg_PV_matrix_L = Matrix.LocRotScale(Leg_PV_matrix_loc_L, Leg_IK_L_pole.matrix.to_quaternion(), None)
            Leg_IK_L_pole.matrix = Leg_PV_matrix_L

            context.object.l_leg_ik = True

            Leg_FK_L_upper.rotation_quaternion = [1,0,0,0]
            Leg_FK_L_lower.rotation_quaternion = [1,0,0,0]

def convertStringNumbers(list):
    s = [str(i) for i in list]
    res = int("".join(s))
    return(res)

def selectBoneCollection(collections,target):
    for collection in collections:
        try:
            layer_data = collection["layer"]
            if layer_data == target:
                return collection
        except:
            pass

cur_blender_version = convertStringNumbers(list(bpy.app.version))

def applyMod(mesh,modifier):

    c = {'object': mesh}

    try:
        if cur_blender_version >= 400:
            with bpy.context.temp_override(**c):
                bpy.ops.object.modifier_apply(modifier=modifier)
        else:
            bpy.ops.object.modifier_apply(c, modifier=modifier)
    except RuntimeError:
        print(f"Could not bake {mesh.name} due to it having shape keys")

def removeMod(mesh,modifier):
    try:
        mesh.modifiers.remove(mesh.modifiers[modifier])
    except KeyError:
        pass

def removeNode(node_tree,nodes):
    for node in nodes:
        node_tree.nodes.remove(node)

def bakeEyes(mesh,node_tree,mode,rig,res):
    eye_obj = mesh
    nodes = node_tree.nodes
    eyenode = node_tree.nodes['eyenode']
    bake_pass_filter = {'COLOR'}

    #cur_loc = os.path.dirname(bpy.data.filepath)
    #timestamp = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    #final_path = f"{cur_loc}\\ice_cube_bake_{timestamp}"
    #if not os.path.exists(final_path):
    #    os.mkdir(final_path)

    if mode == 0: #Color, Single Eye
        #creating image
        eye_texture = nodes.new('ShaderNodeTexImage')
        eye_texture.name = "eye_texture_bake"
        eye_texture.location = (eyenode.location[0]-400,eyenode.location[1]+100)
        eye_texture_image = bpy.data.images.new('Baked Eye Texture',width=res,height=res)
        eye_texture.image = eye_texture_image
        
        #selecting node
        for node in nodes:
            node.select = False
        eye_texture.select= True
        nodes.active = eye_texture

        bpy.ops.object.select_all(action='DESELECT')
        eye_obj.select_set(state=True)
        bpy.context.view_layer.objects.active = eye_obj
        bpy.ops.object.bake(type='DIFFUSE',pass_filter=bake_pass_filter)
        bpy.ops.object.select_all(action='DESELECT')

        eye_texture_image.pack()

        #img_loc = f"{final_path}\\eye_texture_single_color.png"
        #eye_texture_image.save_render(img_loc)
        #bpy.data.images.remove(eye_texture_image)
        #final_image = bpy.data.images.load(img_loc)
        #eye_texture.image = final_image

    elif mode == 1: #Color, Double Eye
        #creating image
        eye_texture_R = nodes.new('ShaderNodeTexImage')
        eye_texture_R.name = "r_eye_texture_bake"
        eye_texture_R.location = (eyenode.location[0]-600,eyenode.location[1]+200)
        eye_texture_R_image = bpy.data.images.new('Baked Right Eye Texture',width=res,height=res)
        eye_texture_R.image = eye_texture_R_image

        eye_texture_L = nodes.new('ShaderNodeTexImage')
        eye_texture_L.name = "l_eye_texture_bake"
        eye_texture_L.location = (eyenode.location[0]-600,eyenode.location[1]-100)
        eye_texture_L_image = bpy.data.images.new('Baked Left Eye Texture',width=res,height=res)
        eye_texture_L.image = eye_texture_L_image
        
        #selecting node
        for node in nodes:
            node.select = False
        eye_texture_R.select= True
        nodes.active = eye_texture_R

        eyenode.inputs[30].default_value = 1

        bpy.ops.object.select_all(action='DESELECT')
        eye_obj.select_set(state=True)
        bpy.context.view_layer.objects.active = eye_obj
        bpy.ops.object.bake(type='DIFFUSE',pass_filter=bake_pass_filter)

        for node in nodes:
            node.select = False
        eye_texture_L.select= True
        nodes.active = eye_texture_L

        eyenode.inputs[31].default_value = 1

        bpy.ops.object.bake(type='DIFFUSE',pass_filter=bake_pass_filter)
        
        eye_texture_R_image.pack()
        eye_texture_L_image.pack()
        #img_locR = f"{final_path}\\eye_texture_right_color.png"
        #img_locL = f"{final_path}\\eye_texture_left_color.png"
        #eye_texture_R_image.save_render(img_locR)
        #eye_texture_L_image.save_render(img_locL)
        #bpy.data.images.remove(eye_texture_R_image)
        #bpy.data.images.remove(eye_texture_L_image)
        #final_imageR = bpy.data.images.load(img_locR)
        #final_imageL = bpy.data.images.load(img_locL)
        #eye_texture_R.image = final_imageR
        #eye_texture_L.image = final_imageL
        

    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = rig
    rig.select_set(state=True)

def bakeIceCube(self,context,override=False):
    rig = isRigSelected(context)
    ice_cube_col = rig.users_collection
    col_children = ice_cube_col[0].children
    obj = context.object
    final_res = obj.eye_bake_resolution
    render_engine = context.scene.render.engine

    bpy.data.scenes["Scene"].render.engine

    if render_engine != 'CYCLES':
        context.scene.render.engine = 'CYCLES'

    if not override:
        if obj.confirm_rig_bake:
            pass
        else:
            CustomErrorBox("WARNING: THIS ACTION IS EXTREMELY DESTRUCTIVE AND MAY BREAK THE RIG\nPROCEED WITH CAUTION! CLICK THE ERROR ICON TO THE RIGHT TO CONFIRM BAKE THEN TRY AGAIN","Unconfirmed Bake!",'ERROR')
            return {'FINISHED'}
        
        if obj.baked_rig:
            CustomErrorBox("This rig has already been baked, action cancelled",'Already Baked','ERROR')
            return{'FINISHED'}

    vaild_collections = {}

    sub_valid_collections = {}
    try:
        for child1 in col_children:
            for child2 in child1.children:
                for key in ["Non Parent"]:
                    if str(child2).__contains__(key):
                        vaild_collections[key] = child2

        for col in vaild_collections:
            for child in vaild_collections[col].children:
                temp_col_thing = []
                for object in child.objects:
                    temp_col_thing.append(object)
                sub_valid_collections[child.name] = temp_col_thing
    except:
        CustomErrorBox("An Unknown Error Has Occurred",'Bake Error','ERROR')
        return {'CANCELLED'}

    #Clearing Objects

    if obj.armtype_enum == 'one':
        for mesh in sub_valid_collections['Alex']:
            bpy.data.objects.remove(mesh,do_unlink=True)
        for mesh in sub_valid_collections['Thin']:
            bpy.data.objects.remove(mesh,do_unlink=True)
    if obj.armtype_enum == 'two':
        for mesh in sub_valid_collections['Steve']:
            bpy.data.objects.remove(mesh,do_unlink=True)
        for mesh in sub_valid_collections['Thin']:
            bpy.data.objects.remove(mesh,do_unlink=True)
    if obj.armtype_enum == 'three':
        for mesh in sub_valid_collections['Alex']:
            bpy.data.objects.remove(mesh,do_unlink=True)
        for mesh in sub_valid_collections['Steve']:
            bpy.data.objects.remove(mesh,do_unlink=True)

    if obj.eyelashes == False:
        for mesh in sub_valid_collections['Eyelashes']:
            bpy.data.objects.remove(mesh,do_unlink=True)

    if obj.dynamichair == False:
        for mesh in sub_valid_collections['Dynamic Hair']:
            bpy.data.objects.remove(mesh,do_unlink=True)

    #Clearing Modifiers

    if obj.armtype_enum == 'one':
        col_to_search = sub_valid_collections['Steve']
    elif obj.armtype_enum == 'two':
        col_to_search = sub_valid_collections['Alex']
    elif obj.armtype_enum == 'three':
        col_to_search = sub_valid_collections['Thin']

    for mesh in col_to_search:
        modifier_to_apply = ["Arm Deform","Arm Bulge"]
        for mod in modifier_to_apply:
            applyMod(mesh,mod)
    
        if cur_blender_version >= 400:
            collections = rig.data.collections
            twist_collection = selectBoneCollection(collections,"Twist")
            twist_active = twist_collection.is_visible
            print(twist_active)
        else:
            twist_active = isRigSelected(context).data.layers[10]
        

        if obj.bake_all_unused_features:
            if twist_active == False:
                removeMod(mesh,"Arm Twist")
            if not obj.squish_arm_r or not obj.squish_arm_l:
                removeMod(mesh,"Arm Squish")
                setattr(rig,"baked_rig_squish",True)
            if not obj.squish_leg_r or not obj.squish_leg_l:
                removeMod(mesh,"Leg Squish")
                setattr(rig,"baked_rig_squish",True)
            setattr(rig,"baked_rig_unused_features",True)

    for mesh in sub_valid_collections['Misc']:
        modifier_to_apply = ["Chest Lattice","Chest Lattice 2","Body Deform","Rounded Top Deform","Body Bulge","Leg Deform","Leg Bulge","Teeth Curve"]
        for mod in modifier_to_apply:
            applyMod(mesh,mod)
        if obj.bake_all_unused_features:
            if not obj.squish_body:
                removeMod(mesh,"Body Stretch")
                setattr(rig,"baked_rig_squish",True)
            if not obj.squish_head:
                removeMod(mesh,"Head Squish")
                setattr(rig,"baked_rig_squish",True)
            if not obj.squish_leg_r or not obj.squish_leg_l:
                removeMod(mesh,"Leg Squish")
                setattr(rig,"baked_rig_squish",True)

    #Baking Eye Texture
    if obj.bake_eye_textures:

        try:

            material_list = {}
            rig = isRigSelected(context)
            mat_hold = mat_holder_func(rig)
            materials = mat_hold.data.materials
            eye_type = obj.gradient_color_eye
            
            for mat in materials:
                try:
                    if mat["ice_cube_material"]:
                        material_list[mat["ice_cube_material"]] = mat
                except KeyError:
                    pass
            if not eye_type == 'texture':
                if obj.split_eye_bakes:
                    if eye_type == 'color' or eye_type == 'gradient':
                        eye_obj = eye_mesh(rig)
                        node_tree = material_list['eyes'].node_tree
                        nodes = node_tree.nodes
                        links = node_tree.links

                        bakeEyes(eye_obj,node_tree,1,rig,final_res)

                        eye_texture_R = nodes['r_eye_texture_bake']
                        eye_texture_L = nodes['l_eye_texture_bake']

                        #reconnecting nodes
                        newBSDF = nodes.new('ShaderNodeBsdfPrincipled')
                        newBSDF.location = (eye_texture_R.location[0]+700,eye_texture_R.location[1]-200)

                        mixNode = nodes.new('ShaderNodeMix')
                        mixNode.data_type = 'RGBA'
                        mixNode.location = (newBSDF.location[0]-200,newBSDF.location[1])

                        attributeNode = nodes.new('ShaderNodeAttribute')
                        attributeNode.location = (mixNode.location[0]-200,mixNode.location[1]+100)
                        attributeNode.attribute_name = 'split'

                        links.new(attributeNode.outputs[0],mixNode.inputs[0])
                        links.new(eye_texture_R.outputs[0],mixNode.inputs[6])
                        links.new(eye_texture_L.outputs[0],mixNode.inputs[7])
                        links.new(mixNode.outputs[2],newBSDF.inputs[0])
                        links.new(newBSDF.outputs[0],nodes['Material Output'].inputs[0])
                        newBSDF.inputs[7].default_value = 0

                        #clearing old nodes
                        node_removal_list = [nodes['eyenode'],nodes['Gradient Right'],nodes['Gradient Left'],nodes['Gradient Texture'],nodes['Mapping'],nodes['Texture Coordinate'],nodes['image_eyes_overlay_1'],nodes['image_eyes_overlay_2'],nodes['image_eyes_overlay_mix'],nodes['Texture Split'],nodes['image_eyes']]
                        removeNode(node_tree,node_removal_list)
                else:
                    if eye_type == 'color' or eye_type == 'gradient':
                        eye_obj = eye_mesh(rig)
                        node_tree = material_list['eyes'].node_tree
                        nodes = node_tree.nodes
                        links = node_tree.links

                        bakeEyes(eye_obj,node_tree,0,rig,final_res)

                        eye_texture = nodes['eye_texture_bake']

                        #reconnecting nodes
                        newBSDF = nodes.new('ShaderNodeBsdfPrincipled')
                        newBSDF.location = (eye_texture.location[0]+400,eye_texture.location[1]-100)

                        links.new(eye_texture.outputs[0],newBSDF.inputs[0])
                        links.new(newBSDF.outputs[0],nodes['Material Output'].inputs[0])
                        newBSDF.inputs[7].default_value = 0

                        #clearing old nodes
                        node_removal_list = [nodes['eyenode'],nodes['Gradient Right'],nodes['Gradient Left'],nodes['Gradient Texture'],nodes['Mapping'],nodes['Texture Coordinate'],nodes['image_eyes_overlay_1'],nodes['image_eyes_overlay_2'],nodes['image_eyes_overlay_mix'],nodes['Texture Split'],nodes['image_eyes']]
                        removeNode(node_tree,node_removal_list)
            else:

                #reorganizing nodes
                node_tree = material_list['eyes'].node_tree
                nodes = node_tree.nodes
                links = node_tree.links

                eyenode = nodes['eyenode']

                newBSDF = nodes.new('ShaderNodeBsdfPrincipled')
                newBSDF.location = eyenode.location
                newBSDF.inputs[7].default_value = 0

                links.new(nodes['image_eyes_overlay_mix'].outputs[2],newBSDF.inputs[0])
                links.new(newBSDF.outputs[0],nodes['Material Output'].inputs[0])

                #clearing old nodes
                node_removal_list = [nodes['eyenode'],nodes['Gradient Right'],nodes['Gradient Left'],nodes['Gradient Texture'],nodes['Mapping'],nodes['Texture Coordinate']]
                removeNode(node_tree,node_removal_list)
            setattr(rig,"baked_rig_eyes",True)
        except:
            CustomErrorBox("An Unknown Error Has Occurred",'Bake Error','ERROR')
            return {'CANCELLED'}
        
    context.scene.render.engine = render_engine

    setattr(rig, 'baked_rig', True)

def duplicateBone(rig,edit_bone,bone):
    new_bone = rig.data.edit_bones.new(f"{bone.name}_OverrideBone")
    new_bone.head = edit_bone.head
    new_bone.tail = edit_bone.tail
    new_bone.roll = edit_bone.roll
    return new_bone.name

def newCopyRotation(source,target,subtarget,name):
    copy_rotation = source.constraints.new('COPY_ROTATION')
    copy_rotation.name = name
    copy_rotation.target = target
    copy_rotation.subtarget = subtarget.name
    copy_rotation.mix_mode = 'BEFORE'
    copy_rotation.target_space = 'LOCAL'
    copy_rotation.owner_space = 'LOCAL'
    context_override = {'active_pose_bone' : source}
    if cur_blender_version >= 400:
        with bpy.context.temp_override(**context_override):
            bpy.ops.constraint.move_to_index(constraint=copy_rotation.name,owner='BONE',index=0)
    else:
        bpy.ops.constraint.move_to_index(context_override,constraint=copy_rotation.name,owner='BONE',index=0)

def newCopyLocation(source,target,subtarget,name):
    copy_location = source.constraints.new('COPY_LOCATION')
    copy_location.name = name
    copy_location.target = target
    copy_location.subtarget = subtarget.name
    copy_location.target_space = 'LOCAL'
    copy_location.owner_space = 'LOCAL'
    copy_location.use_offset = True
    context_override = {'active_pose_bone' : source}
    if cur_blender_version >= 400:
        with bpy.context.temp_override(**context_override):
            bpy.ops.constraint.move_to_index(constraint=copy_location.name,owner='BONE',index=0)
    else:
        bpy.ops.constraint.move_to_index(context_override,constraint=copy_location.name,owner='BONE',index=0)

def newCopyScale(source,target,subtarget,name):
    copy_scale = source.constraints.new('COPY_SCALE')
    copy_scale.name = name
    copy_scale.target = target
    copy_scale.subtarget = subtarget.name
    copy_scale.target_space = 'LOCAL'
    copy_scale.owner_space = 'LOCAL'
    copy_scale.use_offset = True
    context_override = {'active_pose_bone' : source}
    if cur_blender_version >= 400:
        with bpy.context.temp_override(**context_override):
            bpy.ops.constraint.move_to_index(constraint=copy_scale.name,owner='BONE',index=0)
    else:
        bpy.ops.constraint.move_to_index(context_override,constraint=copy_scale.name,owner='BONE',index=0)

def setRestPose(context):
    rig = isRigSelected(context)
    original_mode = bpy.context.mode

    ignore_bones_list = ["Shoulder LeftPOS","Shoulder LeftPOS.001","Shoulder RightPOS","Shoulder RightPOS.001"] #ONLY HERE FOR COMPATABILITY WITH OLDER ICE CUBE VERSIONS
    

    for bone in rig.pose.bones:
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

        if reset_loc or reset_rot or reset_scale:
            try:
                override_pose_bone = bone["OverridePoseBone"]
                continue
            except:
                pass

            try:
                ignore_pose_bone = bone["IgnoreOverrideCheck"]
                continue
            except:
                pass
            
            if bone.name in ignore_bones_list:
                continue

            if not bpy.context.mode == "EDIT_ARMATURE":
                bpy.ops.object.mode_set(mode='EDIT')
            
            #try:
            edit_bone = rig.data.edit_bones.get(bone.name)

            new_bone_name = duplicateBone(rig,edit_bone,bone)

            bpy.ops.object.mode_set(mode='POSE')

            new_bone = rig.pose.bones[new_bone_name]
            new_bone.matrix_basis = bone.matrix_basis.copy()
            #new_bone.matrix = bone.matrix
            
            bone.location = (0,0,0)
            bone.rotation_quaternion = Quaternion((1,0,0,0))
            bone.scale = (1,1,1)
            bone["OverridePoseBone"] = new_bone.name
            new_bone["OverridePoseBone"] = "OverrideBone"

            if reset_scale:
                newCopyScale(bone,rig,new_bone,f"{bone.name}_{new_bone.name}_SCALE")

            if reset_rot:
                newCopyRotation(bone,rig,new_bone,f"{bone.name}_{new_bone.name}_ROTATION")
            
            if reset_loc:
                newCopyLocation(bone,rig,new_bone,f"{bone.name}_{new_bone.name}_LOCATION")
            
            if cur_blender_version >= 400:
                collections = rig.data.collections
                custom_default = selectBoneCollection(collections,"Custom Default")
                custom_default.assign(new_bone)
            else:
                for i in range(32):
                    new_bone.bone.layers[11] = True
                    new_bone.bone.layers[i] = False
                
            
            

            print(f"Created override pose for {bone.name}")
            #except:
            #    pass

            

                
    
    if original_mode == "POSE":
        bpy.ops.object.mode_set(mode='POSE')
    else:
        bpy.ops.object.mode_set(mode='OBJECT')

def resetRestPose(context):
    rig = isRigSelected(context)
    original_mode = bpy.context.mode

    reset_data = {}

    for bone in rig.pose.bones:
        try:
            boneOverrideData = bone["OverridePoseBone"]
            if boneOverrideData != "OverrideBone":
                reset_data[bone.name] = boneOverrideData
                override_bone = rig.pose.bones[boneOverrideData]

                location_constraint = bone.constraints.get(f"{bone.name}_{boneOverrideData}_LOCATION")
                rotation_constraint = bone.constraints.get(f"{bone.name}_{boneOverrideData}_ROTATION")
                scale_constraint = bone.constraints.get(f"{bone.name}_{boneOverrideData}_SCALE")

                if cur_blender_version >= 400:
                    if location_constraint:
                        context_override = {'active_pose_bone' : bone}
                        with context.temp_override(**context_override):
                            bpy.ops.constraint.apply(constraint=location_constraint.name,owner='BONE')
                
                    if rotation_constraint:
                        context_override = {'active_pose_bone' : bone}
                        with context.temp_override(**context_override):
                            bpy.ops.constraint.apply(constraint=rotation_constraint.name,owner='BONE')

                    if scale_constraint:
                        context_override = {'active_pose_bone' : bone}
                        with context.temp_override(**context_override):
                            bpy.ops.constraint.apply(constraint=scale_constraint.name,owner='BONE')
                else:

                    if location_constraint:
                        context_override = {'active_pose_bone' : bone}
                        bpy.ops.constraint.apply(context_override,constraint=location_constraint.name,owner='BONE')

                    if rotation_constraint:
                        context_override = {'active_pose_bone' : bone}
                        bpy.ops.constraint.apply(context_override,constraint=rotation_constraint.name,owner='BONE')

                    if scale_constraint:
                        context_override = {'active_pose_bone' : bone}
                        bpy.ops.constraint.apply(context_override,constraint=scale_constraint.name,owner='BONE')
                

                #bone.matrix_basis = bone.matrix_basis @ override_bone.matrix_basis
                del bone["OverridePoseBone"]


        except KeyError:
            pass
    for bone in rig.pose.bones: #DELETING BONES
        try:
            boneOverrideData = bone["OverridePoseBone"]
            if not bpy.context.mode == 'EDIT_ARMATURE':
                bpy.ops.object.mode_set(mode='EDIT')
            if boneOverrideData == "OverrideBone":
                target_bone = rig.data.edit_bones.get(bone.name)
                if target_bone:
                    rig.data.edit_bones.remove(target_bone)   
        except KeyError:
            pass
    
    if original_mode == "POSE":
        bpy.ops.object.mode_set(mode='POSE')
    else:
        bpy.ops.object.mode_set(mode='OBJECT')

settings_data = open_json(settings_file)

cur_file_loc = f"{root_folder}/lang/{settings_data['current_language_file']}"
english = f"{root_folder}/lang/english.ic_lang"

current_language_file = open_json(cur_file_loc if os.path.exists(cur_file_loc) else english)

class IC_DevMode_SortLanguage(bpy.types.Operator):
    """DO NOT RUN UNLESS YOU KNOW WHAT YOU'RE DOING"""
    bl_idname = "ice_cube_dev.sort_language"
    bl_label = "Ice Cube Sort Language File"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        sorted_language_file = dict(sorted(current_language_file['translations'].items()))
        current_language_file['translations'] = sorted_language_file
        sorted_language_data = json.dumps(current_language_file, indent=4)
        with open(f"{root_folder}/lang/{settings_data['current_language_file']}", "w") as json_file:
            json_file.write(sorted_language_data)

        return{'FINISHED'}

def getLanguageTranslation(translation):
    lang_translations = current_language_file['translations']
    if translation in lang_translations:
        return lang_translations[translation]
    else:
        
        #LANGUAGE WRITING CODE, DO ***NOT*** ENABLE UNLESS YOU KNOW WHAT YOU ARE DOING

        #current_language_file['translations'][translation] = translation
        #converted_settings_data = json.dumps(current_language_file, indent=4)
        #with open(f"{root_folder}/lang/{settings_data['current_language_file']}", "w") as json_file:
        #    json_file.write(converted_settings_data)

        return translation

classes = [
    IC_DevMode_SortLanguage
           ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__=="__main__":
    register()