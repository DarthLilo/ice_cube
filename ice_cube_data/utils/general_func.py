import imghdr
import struct
import json
from urllib import request
import bpy
from mathutils import Matrix

from ice_cube import github_url

from ice_cube_data.utils.selectors import isRigSelected

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