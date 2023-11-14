import imghdr
import struct
import json
from urllib import request
import bpy
from mathutils import Matrix
import aud

from ice_cube import github_url, root_folder

from ice_cube_data.utils.selectors import isRigSelected, mat_holder_func, eye_mesh
from ice_cube_data.utils.ui_tools import CustomErrorBox

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


def applyMod(mesh,modifier):
    try:
        bpy.ops.object.modifier_apply({'object': mesh}, modifier=modifier)
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

def bakeIceCube(self,context,override):
    rig = isRigSelected(context)
    ice_cube_col = rig.users_collection
    col_children = ice_cube_col[0].children
    obj = context.object
    final_res = obj.eye_bake_resolution

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


        if obj.bake_all_unused_features:
            if isRigSelected(context).data.layers[10] == False:
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

    setattr(rig, 'baked_rig', True)

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