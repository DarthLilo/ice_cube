import bpy
import os
import sys

from ice_cube_data.utils.selectors import isRigSelected
from ice_cube_data.utils.general_func import GetListIndex
from ice_cube_data.utils.ui_tools import CustomErrorBox

def moveModifier(input_mesh,name,loc):
    cur_index = input_mesh.modifiers.find(name)
    while cur_index > loc:
        bpy.ops.object.modifier_move_up({'object': input_mesh},modifier=name)
        cur_index -= 1

def parent_left_arm(self, context, input_mesh):
    dynamic_obj_L_list = []
    dynamic_objs_L = ["Arm Twist LAT L", "Arm Deform LAT L", "Arm Bulge LAT L", "Arm Squish LAT L", "Lattice SMOOTH Arm L", "Sharp LAT Arm L"]
    rig = isRigSelected(context)

    try:
        if input_mesh['ParentedToIceCube'] == 1:
            return {'FINISHED'}
    except:
        pass


    for obj in rig.children:
        if any(x in obj.name for x in dynamic_objs_L):
            dynamic_obj_L_list.append(obj.name)


    #gives the meshes their attributes
    left_leg_parent = input_mesh
    rig = isRigSelected(context)
    
    

    #Arm Deform
    mod_name = "Arm Deform"
    modifier = left_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Arm Deform LAT L", dynamic_obj_L_list)]]
    moveModifier(input_mesh,mod_name,0)

    #Arm Bulge
    mod_name = "Arm Bulge"
    modifier = left_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Arm Bulge LAT L", dynamic_obj_L_list)]]
    moveModifier(input_mesh,mod_name,1)

    #twist
    mod_name = "Arm Twist"
    modifier = left_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Arm Twist LAT L", dynamic_obj_L_list)]]
    moveModifier(input_mesh,mod_name,2)

    #Arm Squish
    mod_name = "Arm Squish"
    modifier = left_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Arm Squish LAT L", dynamic_obj_L_list)]]

    spot = modifier.driver_add("show_viewport")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"antilag\"]"
    driver.expression = "+1 -var"
    moveModifier(input_mesh,mod_name,3)

    #Smooth Bend
    mod_name = "Smooth Bend"
    modifier = left_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Lattice SMOOTH Arm L", dynamic_obj_L_list)]]

    spot = modifier.driver_add("strength")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"bendstyle\"]"
    driver.expression = "1 if (var==1) else 0"
    moveModifier(input_mesh,mod_name,4)

    #Sharp Bend
    mod_name = "Sharp bend"
    modifier = left_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Sharp LAT Arm L", dynamic_obj_L_list)]]

    spot = modifier.driver_add("strength")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"bendstyle\"]"
    driver.expression = "1 if (var==0) else 0"
    moveModifier(input_mesh,mod_name,5)

    #Parenting
    left_leg_parent.parent = rig

    input_mesh['ParentedToIceCube'] = 1
    
    return {'FINISHED'}

def parent_right_arm(self, context, input_mesh):

    dynamic_obj_R_list = []
    dynamic_objs_R = ["Arm Twist LAT R", "Arm Deform LAT R", "Arm Bulge LAT R", "Arm Squish LAT R", "Lattice SMOOTH Arm R", "Sharp LAT Arm R"]
    rig = isRigSelected(context)

    try:
        if input_mesh['ParentedToIceCube'] == 1:
            return {'FINISHED'}
    except:
        pass


    for obj in rig.children:
        if any(x in obj.name for x in dynamic_objs_R):
            dynamic_obj_R_list.append(obj.name)



    #gives the meshes their attributes
    right_leg_parent = input_mesh
    rig = isRigSelected(context)


    #Arm Deform
    mod_name = "Arm Deform"
    modifier = right_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_R_list[GetListIndex("Arm Deform LAT R", dynamic_obj_R_list)]]
    moveModifier(input_mesh,mod_name,0)

    #Arm Bulge
    mod_name = "Arm Bulge"
    modifier = right_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_R_list[GetListIndex("Arm Bulge LAT R", dynamic_obj_R_list)]]
    moveModifier(input_mesh,mod_name,1)

    #twist
    mod_name = "Arm Twist"
    modifier = right_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_R_list[GetListIndex("Arm Twist LAT R", dynamic_obj_R_list)]]
    moveModifier(input_mesh,mod_name,2)

    #Arm Squish
    mod_name = "Arm Squish"
    modifier = right_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_R_list[GetListIndex("Arm Squish LAT R", dynamic_obj_R_list)]]

    spot = modifier.driver_add("show_viewport")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"antilag\"]"
    driver.expression = "+1 -var"
    moveModifier(input_mesh,mod_name,3)

    #Smooth Bend
    mod_name = "Smooth Bend"
    modifier = right_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_R_list[GetListIndex("Lattice SMOOTH Arm R", dynamic_obj_R_list)]]

    spot = modifier.driver_add("strength")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"bendstyle\"]"
    driver.expression = "1 if (var==1) else 0"
    moveModifier(input_mesh,mod_name,4)

    #Sharp Bend
    mod_name = "Sharp Bend"
    modifier = right_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_R_list[GetListIndex("Sharp LAT Arm R", dynamic_obj_R_list)]]

    spot = modifier.driver_add("strength")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"bendstyle\"]"
    driver.expression = "1 if (var==0) else 0"
    moveModifier(input_mesh,mod_name,5)

    #Parenting
    right_leg_parent.parent = rig

    input_mesh['ParentedToIceCube'] = 1
    
    return {'FINISHED'}

def parent_right_leg(self, context,input_mesh):
    rig = isRigSelected(context)
    dynamic_obj_R_leg_list = []
    dynamic_objs_R_leg = ["Leg Twist LAT R", "Leg Deform LAT R", "Leg Bulge LAT R", "Leg Squish LAT R", "Lattice SMOOTH R", "Sharp LAT R"]

    try:
        if input_mesh['ParentedToIceCube'] == 1:
            return {'FINISHED'}
    except:
        pass


    for obj in rig.children:
        if any(x in obj.name for x in dynamic_objs_R_leg):
            dynamic_obj_R_leg_list.append(obj.name)

    #gives the meshes their attributes
    right_leg_parent = input_mesh
    rig = isRigSelected(context)


    #Arm Deform
    mod_name = "Leg Deform"
    modifier = right_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_R_leg_list[GetListIndex("Leg Deform LAT R", dynamic_obj_R_leg_list)]]
    moveModifier(input_mesh,mod_name,0)

    #Arm Bulge
    mod_name = "Leg Bulge"
    modifier = right_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_R_leg_list[GetListIndex("Leg Bulge LAT R", dynamic_obj_R_leg_list)]]
    moveModifier(input_mesh,mod_name,1)


    #Twist
    mod_name = "Leg Twist"
    modifier = right_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_R_leg_list[GetListIndex("Leg Twist LAT R", dynamic_obj_R_leg_list)]]
    moveModifier(input_mesh,mod_name,2)

    #Arm Squish
    mod_name = "Leg Squish"
    modifier = right_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_R_leg_list[GetListIndex("Leg Squish LAT R", dynamic_obj_R_leg_list)]]

    spot = modifier.driver_add("show_viewport")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"antilag\"]"
    driver.expression = "+1 -var"
    moveModifier(input_mesh,mod_name,3)

    #Smooth Bend
    mod_name = "Smooth Bend"
    modifier = right_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_R_leg_list[GetListIndex("Lattice SMOOTH R", dynamic_obj_R_leg_list)]]

    spot = modifier.driver_add("strength")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"bendstyle\"]"
    driver.expression = "1 if (var==1) else 0"
    moveModifier(input_mesh,mod_name,4)

    #Sharp Bend
    mod_name = "Sharp Bend"
    modifier = right_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_R_leg_list[GetListIndex("Sharp LAT R", dynamic_obj_R_leg_list)]]

    spot = modifier.driver_add("strength")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"bendstyle\"]"
    driver.expression = "1 if (var==0) else 0"
    moveModifier(input_mesh,mod_name,5)

    #Parenting
    right_leg_parent.parent = rig

    input_mesh['ParentedToIceCube'] = 1
    
    return {'FINISHED'}

def parent_left_leg(self, context,input_mesh):
    rig = isRigSelected(context)
    dynamic_obj_L_list = []
    dynamic_objs_L = ["Leg Twist LAT L", "Leg Deform LAT L", "Leg Bulge LAT L", "Leg Squish LAT L", "Lattice SMOOTH L", "Sharp LAT L"]

    try:
        if input_mesh['ParentedToIceCube'] == 1:
            return {'FINISHED'}
    except:
        pass
    
    for obj in rig.children:
        if any(x in obj.name for x in dynamic_objs_L):
            dynamic_obj_L_list.append(obj.name)
    

    #gives the meshes their attributes
    left_leg_parent = input_mesh
    rig = isRigSelected(context)


    #Arm Deform
    mod_name = "Leg Deform"
    modifier = left_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Leg Deform LAT L", dynamic_obj_L_list)]]
    moveModifier(input_mesh,mod_name,0)

    #Arm Bulge
    mod_name = "Leg Bulge"
    modifier = left_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Leg Bulge LAT L", dynamic_obj_L_list)]]
    moveModifier(input_mesh,mod_name,1)

    #Twist
    mod_name = "Leg Twist"
    modifier = left_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Leg Twist LAT L", dynamic_obj_L_list)]]
    moveModifier(input_mesh,mod_name,2)

    #Arm Squish
    mod_name = "Leg Squish"
    modifier = left_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Leg Squish LAT L", dynamic_obj_L_list)]]

    spot = modifier.driver_add("show_viewport")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"antilag\"]"
    driver.expression = "+1 -var"
    moveModifier(input_mesh,mod_name,3)

    #Smooth Bend
    mod_name = "Smooth Bend"
    modifier = left_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Lattice SMOOTH L", dynamic_obj_L_list)]]

    spot = modifier.driver_add("strength")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"bendstyle\"]"
    driver.expression = "1 if (var==1) else 0"
    moveModifier(input_mesh,mod_name,4)

    #Sharp Bend
    mod_name = "Sharp Bend"
    modifier = left_leg_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Sharp LAT L", dynamic_obj_L_list)]]

    spot = modifier.driver_add("strength")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"bendstyle\"]"
    driver.expression = "1 if (var==0) else 0"
    moveModifier(input_mesh,mod_name,5)

    #Parent
    left_leg_parent.parent = rig

    input_mesh['ParentedToIceCube'] = 1
    
    return {'FINISHED'}

def parent_body_func(self, context,input_mesh):

    dynamic_obj_list = []
    dynamic_objs = ["Chest Lattice", "Shape_2_Chest", "BodyStretch", "BodyDeforms", "Breathing Lattice", "RoundedBodyTopDeform", "BodyBulge"]
    rig = isRigSelected(context)

    try:
        if input_mesh['ParentedToIceCube'] == 1:
            return {'FINISHED'}
    except:
        pass


    for obj in rig.children:
        if any(x in obj.name for x in dynamic_objs):
            dynamic_obj_list.append(obj.name)
    


    #gives the meshes their attributes
    body_parent = input_mesh
    rig = isRigSelected(context)

    #weight painting
    vg = body_parent.vertex_groups.new(name="Body_Bendy")
    verts = []
    for vert in body_parent.data.vertices:
        verts.append(vert.index)
    vg.add(verts, 1.0, 'ADD')

    #Chest Lattice
    mod_name = "Chest Lattice"
    modifier = body_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("Chest Lattice", dynamic_obj_list)]]
    
    spot = modifier.driver_add("strength")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"breastshape\"]"
    driver.expression = "1 -var"

    moveModifier(input_mesh,mod_name,0)

    #Chest Lattice 2
    mod_name = "Chest Lattice 2"
    modifier = body_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("Shape_2_Chest", dynamic_obj_list)]]

    spot = modifier.driver_add("strength")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"breastshape\"]"
    driver.expression = "var"

    moveModifier(input_mesh,mod_name,1)

    #Body Deform
    mod_name = "Body Deform"
    modifier = body_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("BodyDeforms", dynamic_obj_list)]]

    moveModifier(input_mesh,mod_name,2)

    #Breath
    mod_name = "Breath Lattice"
    modifier = body_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("Breathing Lattice", dynamic_obj_list)]]

    moveModifier(input_mesh,mod_name,3)

    #Body Stretch
    mod_name = "Body Stretch"
    modifier = body_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("BodyStretch", dynamic_obj_list)]]

    moveModifier(input_mesh,mod_name,4)
    
    #Rounded Top
    mod_name = "Rounded Top Deform"
    modifier = body_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("RoundedBodyTopDeform", dynamic_obj_list)]]

    moveModifier(input_mesh,mod_name,5)

    #Body Bulge
    mod_name = "Body Bulge"
    modifier = body_parent.modifiers.new(name=mod_name, type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("BodyBulge", dynamic_obj_list)]]

    moveModifier(input_mesh,mod_name,6)

    #Armature
    mod_name = "Ice Cube"
    modifier = body_parent.modifiers.new(name=mod_name, type='ARMATURE')
    modifier.object = rig

    moveModifier(input_mesh,mod_name,7)

    #Parenting
    body_parent.parent = rig

    input_mesh['ParentedToIceCube'] = 1
    
    return {'FINISHED'}

def parent_head_func(self, context,input_mesh):
        

    dynamic_obj_list = []
    dynamic_objs = ["Head Squish"]
    rig = isRigSelected(context)

    try:
        if input_mesh['ParentedToIceCube'] == 1:
            return {'FINISHED'}
    except:
        pass

    #checks if they have the proper name
    
    for obj in rig.children:
        if any(x in obj.name for x in dynamic_objs):
            dynamic_obj_list.append(obj.name)
    
    #gives the meshes their attributes
    head_parent = input_mesh
    

    #VERTEX

    vg = head_parent.vertex_groups.new(name="headsquish")
    verts = []
    for vert in head_parent.data.vertices:
        verts.append(vert.index)
    vg.add(verts, 1.0, 'ADD')

    #Head Squish
    modifier = head_parent.modifiers.new(name="Head Squish", type='LATTICE')
    modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("Head Squish", dynamic_obj_list)]]

    spot = modifier.driver_add("show_viewport")
    driver = spot.driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.type = 'SINGLE_PROP'
    var.name = "var"
    target = var.targets[0]
    target.id_type = 'OBJECT'
    target.id = rig
    target.data_path = "[\"antilag\"]"
    driver.expression = "+1 -var"
    moveModifier(input_mesh,"Head Squish",0)

    #Armature
    modifier = head_parent.modifiers.new(name="Ice Cube", type='ARMATURE')
    modifier.object = rig
    moveModifier(input_mesh,"Ice Cube",1)

    #Parenting
    head_parent.parent = rig

    input_mesh['ParentedToIceCube'] = 1
    
    return {'FINISHED'}

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