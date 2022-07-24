import bpy
import os
import sys

from ice_cube_data.utils.selectors import isRigSelected
from ice_cube_data.utils.general_func import GetListIndex
from ice_cube_data.utils.ui_tools import CustomErrorBox
from ice_cube import print_information

def parent_left_arm(self, context):
    #lists
    named_meshes_list = []
    ignore_bend_meshes_list = []
    dynamic_obj_L_list = []
    #terms
    no_bend_term = ["_IgnoreBend"]
    key_term = ["_LeftArmChild"]
    dynamic_objs_L = ["Arm Twist LAT L", "Arm Deform LAT L", "Arm Bulge LAT L", "Arm Squish LAT L", "Lattice SMOOTH Arm L", "Sharp LAT Arm L"]
    #other variables
    key_term_to_str = ("".join(key_term))
    no_bend_term_to_str = ("".join(no_bend_term))
    rig = isRigSelected(context)


    #checks if they have the proper name
    for obj in bpy.data.objects:
        if any(x in obj.name for x in key_term):
            if any(x in obj.name for x in no_bend_term):
                ignore_bend_meshes_list.append(obj.name)
            else:
                named_meshes_list.append(obj.name)
    for obj in rig.children:
        if any(x in obj.name for x in dynamic_objs_L):
            dynamic_obj_L_list.append(obj.name)


    #gives the meshes their attributes
    for obj in named_meshes_list:
        left_leg_parent = bpy.data.objects[obj]
        rig = isRigSelected(context)
        
        

        #Arm Deform
        modifier = left_leg_parent.modifiers.new(name="Arm Deform", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Arm Deform LAT L", dynamic_obj_L_list)]]

        #Arm Bulge
        modifier = left_leg_parent.modifiers.new(name="Arm Bulge", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Arm Bulge LAT L", dynamic_obj_L_list)]]

        #twist
        modifier = left_leg_parent.modifiers.new(name="Arm Twist", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Arm Twist LAT L", dynamic_obj_L_list)]]

        #Arm Squish
        modifier = left_leg_parent.modifiers.new(name="Arm Squish", type='LATTICE')
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

        #Smooth Bend
        modifier = left_leg_parent.modifiers.new(name="Smooth Bend", type='LATTICE')
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

        #Sharp Bend
        modifier = left_leg_parent.modifiers.new(name="Sharp Bend", type='LATTICE')
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

        #Parenting
        left_leg_parent.parent = rig

    #make the lower or upper parenting system
    for obj in ignore_bend_meshes_list:
        left_leg_parent = bpy.data.objects[obj]
        rig = isRigSelected(context)

        

        #Arm Deform
        modifier = left_leg_parent.modifiers.new(name="Arm Deform", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Arm Deform LAT L", dynamic_obj_L_list)]]

        #Arm Bulge
        modifier = left_leg_parent.modifiers.new(name="Arm Bulge", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Arm Bulge LAT L", dynamic_obj_L_list)]]

        #twist
        modifier = left_leg_parent.modifiers.new(name="Arm Twist", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Arm Twist LAT L", dynamic_obj_L_list)]]

        #Arm Squish
        modifier = left_leg_parent.modifiers.new(name="Arm Squish", type='LATTICE')
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

        #refresh
        bpy.context.view_layer.update()
        #Parenting Variable Setup
        objP = left_leg_parent
        rigP = rig
        if context.object.get("L_A_Half") == True:
            bone = rig.pose.bones["Arm Lower L"]
        else:
            bone = rig.pose.bones["Arm Upper L"]
        #save position data
        test_matrix = objP.matrix_world.copy()
        #parent objects
        objP.parent = rigP
        objP.parent_bone = bone.name
        objP.parent_type = 'BONE'
        objP.matrix_world = test_matrix
        


        
        




    #removes the key term from the name
    for obj in ignore_bend_meshes_list:
        clean_mesh_name = (obj.split(no_bend_term_to_str)[0])
        clean_mesh_name = (clean_mesh_name.split(key_term_to_str)[0])
        bpy.data.objects[obj].name = clean_mesh_name

    for obj in named_meshes_list:
        clean_mesh_name = (obj.split(key_term_to_str)[0])
        bpy.data.objects[obj].name = clean_mesh_name

    #error message
    
    if obj in named_meshes_list:
        pass
    elif obj in ignore_bend_meshes_list:
        pass
    else:
        CustomErrorBox("Nothing to parent!", "Parenting Exception", 'ERROR')
    
    return {'FINISHED'}

def parent_right_arm(self, context):

    named_meshes_list = []
    ignore_bend_meshes_list = []
    dynamic_obj_R_list = []
    no_bend_term = ["_IgnoreBend"]
    key_term = ["_RightArmChild"]
    dynamic_objs_R = ["Arm Twist LAT R", "Arm Deform LAT R", "Arm Bulge LAT R", "Arm Squish LAT R", "Lattice SMOOTH Arm R", "Sharp LAT Arm R"]
    key_term_to_str = ("".join(key_term))
    no_bend_term_to_str = ("".join(key_term))
    rig = isRigSelected(context)

    #checks if they have the proper name
    for obj in bpy.data.objects:
        if any(x in obj.name for x in key_term):
            if any(x in obj.name for x in no_bend_term):
                ignore_bend_meshes_list.append(obj.name)
            else:
                named_meshes_list.append(obj.name)

    for obj in rig.children:
        if any(x in obj.name for x in dynamic_objs_R):
            dynamic_obj_R_list.append(obj.name)



    #gives the meshes their attributes
    for obj in named_meshes_list:
        right_leg_parent = bpy.data.objects[obj]
        rig = isRigSelected(context)


        #Arm Deform
        modifier = right_leg_parent.modifiers.new(name="Arm Deform", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_R_list[GetListIndex("Arm Deform LAT R", dynamic_obj_R_list)]]

        #Arm Bulge
        modifier = right_leg_parent.modifiers.new(name="Arm Bulge", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_R_list[GetListIndex("Arm Bulge LAT R", dynamic_obj_R_list)]]

        #twist
        modifier = right_leg_parent.modifiers.new(name="Arm Twist", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_R_list[GetListIndex("Arm Twist LAT R", dynamic_obj_R_list)]]

        #Arm Squish
        modifier = right_leg_parent.modifiers.new(name="Arm Squish", type='LATTICE')
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

        #Smooth Bend
        modifier = right_leg_parent.modifiers.new(name="Smooth Bend", type='LATTICE')
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

        #Sharp Bend
        modifier = right_leg_parent.modifiers.new(name="Sharp Bend", type='LATTICE')
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

        #Parenting
        right_leg_parent.parent = rig

        

    #ignore attributes
    for obj in ignore_bend_meshes_list:
        right_leg_parent = bpy.data.objects[obj]
        rig = isRigSelected(context)

        

        #Arm Deform
        modifier = right_leg_parent.modifiers.new(name="Arm Deform", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_R_list[GetListIndex("Arm Deform LAT R", dynamic_obj_R_list)]]

        #Arm Bulge
        modifier = right_leg_parent.modifiers.new(name="Arm Bulge", type='LATTICE')
        if print_information:
            print(f"{right_leg_parent.name} MESH NAME")
            print(dynamic_obj_R_list[GetListIndex("Arm Bulge LAT R", dynamic_obj_R_list)] + "LIST INDEX THING")
        modifier.object = bpy.data.objects[dynamic_obj_R_list[GetListIndex("Arm Bulge LAT R", dynamic_obj_R_list)]]

        #twist
        modifier = right_leg_parent.modifiers.new(name="Arm Twist", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_R_list[GetListIndex("Arm Twist LAT R", dynamic_obj_R_list)]]

        #Arm Squish
        modifier = right_leg_parent.modifiers.new(name="Arm Squish", type='LATTICE')
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

        #refresh
        bpy.context.view_layer.update()
        #Parenting Variable Setup
        objP = right_leg_parent
        rigP = rig
        if context.object.get("R_A_Half") == True:
            bone = rig.pose.bones["Arm Lower R"]
        else:
            bone = rig.pose.bones["Arm Upper R"]
        #save position data
        test_matrix = objP.matrix_world.copy()
        #parent objects
        objP.parent = rigP
        objP.parent_bone = bone.name
        objP.parent_type = 'BONE'
        objP.matrix_world = test_matrix


    #removes the key term from the name
    for obj in ignore_bend_meshes_list:
        clean_mesh_name = (obj.split(no_bend_term_to_str)[0])
        clean_mesh_name = (clean_mesh_name.split(key_term_to_str)[0])
        bpy.data.objects[obj].name = clean_mesh_name

    for obj in named_meshes_list:
        clean_mesh_name = (obj.split(key_term_to_str)[0])
        bpy.data.objects[obj].name = clean_mesh_name

    #error message
    if obj in named_meshes_list:
        pass
    elif obj in ignore_bend_meshes_list:
        pass
    else:
        CustomErrorBox("Nothing to parent!", "Parenting Exception", 'ERROR')
    
    return {'FINISHED'}

def parent_right_leg(self, context):
    rig = isRigSelected(context)
    named_meshes_list = []
    ignore_bend_meshes_list = []
    dynamic_obj_R_leg_list = []
    no_bend_term = ["_IgnoreBend"]
    key_term = ["_RightLegChild"]
    dynamic_objs_R_leg = ["Leg Twist LAT R", "Leg Deform LAT R", "Leg Bulge LAT R", "Leg Squish LAT R", "Lattice SMOOTH R", "Sharp LAT R"]
    key_term_to_str = ("".join(key_term))
    no_bend_term_to_str = ("".join(no_bend_term))

    #checks if they have the proper name
    for obj in bpy.data.objects:
        if any(x in obj.name for x in key_term):
            if any(x in obj.name for x in no_bend_term):
                ignore_bend_meshes_list.append(obj.name)
            else:
                named_meshes_list.append(obj.name)
    for obj in rig.children:
        if any(x in obj.name for x in dynamic_objs_R_leg):
            dynamic_obj_R_leg_list.append(obj.name)

    #gives the meshes their attributes
    for obj in named_meshes_list:
        right_leg_parent = bpy.data.objects[obj]
        rig = isRigSelected(context)


        #Arm Deform
        modifier = right_leg_parent.modifiers.new(name="Leg Deform", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_R_leg_list[GetListIndex("Leg Deform LAT R", dynamic_obj_R_leg_list)]]

        #Arm Bulge
        modifier = right_leg_parent.modifiers.new(name="Leg Bulge", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_R_leg_list[GetListIndex("Leg Bulge LAT R", dynamic_obj_R_leg_list)]]


        #Twist
        modifier = right_leg_parent.modifiers.new(name="Leg Twist", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_R_leg_list[GetListIndex("Leg Twist LAT R", dynamic_obj_R_leg_list)]]

        #Arm Squish
        modifier = right_leg_parent.modifiers.new(name="Leg Squish", type='LATTICE')
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

        #Smooth Bend
        modifier = right_leg_parent.modifiers.new(name="Smooth Bend", type='LATTICE')
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

        #Sharp Bend
        modifier = right_leg_parent.modifiers.new(name="Sharp Bend", type='LATTICE')
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

        #Parenting
        right_leg_parent.parent = rig

        
    
    for obj in ignore_bend_meshes_list:
        right_leg_parent = bpy.data.objects[obj]
        rig = isRigSelected(context)


        #Arm Deform
        modifier = right_leg_parent.modifiers.new(name="Leg Deform", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_R_leg_list[GetListIndex("Leg Deform LAT R", dynamic_obj_R_leg_list)]]

        #Arm Bulge
        modifier = right_leg_parent.modifiers.new(name="Leg Bulge", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_R_leg_list[GetListIndex("Leg Bulge LAT R", dynamic_obj_R_leg_list)]]

        #Twist
        modifier = right_leg_parent.modifiers.new(name="Leg Twist", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_R_leg_list[GetListIndex("Leg Twist LAT R", dynamic_obj_R_leg_list)]]

        #Arm Squish
        modifier = right_leg_parent.modifiers.new(name="Leg Squish", type='LATTICE')
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

        #refresh
        bpy.context.view_layer.update()
        #Parenting Variable Setup
        objP = right_leg_parent
        rigP = rig
        if context.object.get("R_L_Half") == True:
            bone = rig.pose.bones["Leg Lower R"]
        else:
            bone = rig.pose.bones["Leg Upper R"]
        #save position data
        test_matrix = objP.matrix_world.copy()
        #parent objects
        objP.parent = rigP
        objP.parent_bone = bone.name
        objP.parent_type = 'BONE'
        objP.matrix_world = test_matrix  

    #removes the key term from the name

    for obj in ignore_bend_meshes_list:
        clean_mesh_name = (obj.split(no_bend_term_to_str)[0])
        clean_mesh_name = (clean_mesh_name.split(key_term_to_str)[0])
        bpy.data.objects[obj].name = clean_mesh_name

    for obj in named_meshes_list:
        clean_mesh_name = (obj.split(key_term_to_str)[0])
        bpy.data.objects[obj].name = clean_mesh_name
    
    

    #error message
    if obj in named_meshes_list:
        pass
    elif obj in ignore_bend_meshes_list:
        pass
    else:
        CustomErrorBox("Nothing to parent!", "Parenting Exception", 'ERROR')
    
    return {'FINISHED'}

def parent_left_leg(self, context):
    rig = isRigSelected(context)
    named_meshes_list = []
    ignore_bend_meshes_list = []
    dynamic_obj_L_list = []
    no_bend_term = ["_IgnoreBend"]
    key_term = ["_LeftLegChild"]
    dynamic_objs_L = ["Leg Twist LAT L", "Leg Deform LAT L", "Leg Bulge LAT L", "Leg Squish LAT L", "Lattice SMOOTH L", "Sharp LAT L"]
    key_term_to_str = ("".join(key_term))
    no_bend_term_to_str = ("".join(no_bend_term))


    #checks if they have the proper name
    for obj in bpy.data.objects:
        if any(x in obj.name for x in key_term):
            if any(x in obj.name for x in no_bend_term):
                ignore_bend_meshes_list.append(obj.name)
            else:
                named_meshes_list.append(obj.name)
    
    for obj in rig.children:
        if any(x in obj.name for x in dynamic_objs_L):
            dynamic_obj_L_list.append(obj.name)
    

    #gives the meshes their attributes
    for obj in named_meshes_list:
        left_leg_parent = bpy.data.objects[obj]
        rig = isRigSelected(context)


        #Arm Deform
        modifier = left_leg_parent.modifiers.new(name="Leg Deform", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Leg Deform LAT L", dynamic_obj_L_list)]]

        #Arm Bulge
        modifier = left_leg_parent.modifiers.new(name="Leg Bulge", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Leg Bulge LAT L", dynamic_obj_L_list)]]

        #Twist
        modifier = left_leg_parent.modifiers.new(name="Leg Twist", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Leg Twist LAT L", dynamic_obj_L_list)]]

        #Arm Squish
        modifier = left_leg_parent.modifiers.new(name="Leg Squish", type='LATTICE')
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

        #Smooth Bend
        modifier = left_leg_parent.modifiers.new(name="Smooth Bend", type='LATTICE')
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

        #Sharp Bend
        modifier = left_leg_parent.modifiers.new(name="Sharp Bend", type='LATTICE')
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

        #Parent
        left_leg_parent.parent = rig

        
    
    for obj in ignore_bend_meshes_list:
        left_leg_parent = bpy.data.objects[obj]
        rig = isRigSelected(context)


        #Arm Deform
        modifier = left_leg_parent.modifiers.new(name="Leg Deform", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Leg Deform LAT L", dynamic_obj_L_list)]]

        #Arm Bulge
        modifier = left_leg_parent.modifiers.new(name="Leg Bulge", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Leg Bulge LAT L", dynamic_obj_L_list)]]

        #Twist
        modifier = left_leg_parent.modifiers.new(name="Leg Twist", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_L_list[GetListIndex("Leg Twist LAT L", dynamic_obj_L_list)]]

        #Arm Squish
        modifier = left_leg_parent.modifiers.new(name="Leg Squish", type='LATTICE')
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

        #refresh
        bpy.context.view_layer.update()
        #Parenting Variable Setup
        objP = left_leg_parent
        rigP = rig
        if context.object.get("L_L_Half") == True:
            bone = rig.pose.bones["Leg Lower L"]
        else:
            bone = rig.pose.bones["Leg Upper L"]
        #save position data
        test_matrix = objP.matrix_world.copy()
        #parent objects
        objP.parent = rigP
        objP.parent_bone = bone.name
        objP.parent_type = 'BONE'
        objP.matrix_world = test_matrix

    #removes the key term from the name
    for obj in ignore_bend_meshes_list:
        clean_mesh_name = (obj.split(no_bend_term_to_str)[0])
        clean_mesh_name = (clean_mesh_name.split(key_term_to_str)[0])
        bpy.data.objects[obj].name = clean_mesh_name

    for obj in named_meshes_list:
        clean_mesh_name = (obj.split(key_term_to_str)[0])
        bpy.data.objects[obj].name = clean_mesh_name

    #error message
    if obj in named_meshes_list:
        pass
    elif obj in ignore_bend_meshes_list:
        pass
    else:
        CustomErrorBox("Nothing to parent!", "Parenting Exception", 'ERROR')
    
    return {'FINISHED'}

def parent_body_func(self, context):
    named_meshes_list = []
    ignore_bend_meshes_list = []
    dynamic_obj_list = []
    no_bend_term = ["_IgnoreBend"]
    key_term = ["_BodyChild"]
    dynamic_objs = ["Chest Lattice", "Shape_2_Chest", "BodyStretch", "BodyDeforms", "Breathing Lattice", "RoundedBodyTopDeform", "BodyBulge"]
    key_term_to_str = ("".join(key_term))
    no_bend_term_to_str = ("".join(no_bend_term))
    rig = isRigSelected(context)

    #checks if they have the proper name
    for obj in bpy.data.objects:
        if any(x in obj.name for x in key_term):
            if any(x in obj.name for x in no_bend_term):
                ignore_bend_meshes_list.append(obj.name)
            else:
                named_meshes_list.append(obj.name)
    for obj in rig.children:
        if any(x in obj.name for x in dynamic_objs):
            dynamic_obj_list.append(obj.name)
    


    #gives the meshes their attributes
    for obj in named_meshes_list:
        body_parent = bpy.data.objects[obj]
        rig = isRigSelected(context)

        #weight painting
        vg = body_parent.vertex_groups.new(name="Body_Bendy")
        verts = []
        for vert in body_parent.data.vertices:
            verts.append(vert.index)
        vg.add(verts, 1.0, 'ADD')

        #Chest Lattice
        modifier = body_parent.modifiers.new(name="Chest Lattice", type='LATTICE')
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

        #Chest Lattice 2
        modifier = body_parent.modifiers.new(name="Chest Lattice 2", type='LATTICE')
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

        #Body Deform
        modifier = body_parent.modifiers.new(name="Body Deform", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("BodyDeforms", dynamic_obj_list)]]

        #Breath
        modifier = body_parent.modifiers.new(name="Breath Lattice", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("Breathing Lattice", dynamic_obj_list)]]


        #Body Stretch
        modifier = body_parent.modifiers.new(name="Body Stretch", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("BodyStretch", dynamic_obj_list)]]

    

        spot = modifier.driver_add("show_viewport")
        driver = spot.driver
        driver.type = 'SCRIPTED'
        var = driver.variables.new()
        var.type = 'SINGLE_PROP'
        var.name = "var"
        target = var.targets[0]
        target.id_type = 'OBJECT'
        target.id = rig
        target.data_path = "[\"body_deforms\"]"
        driver.expression = "var"

        #Rounded Top
        modifier = body_parent.modifiers.new(name="Rounded Top Deform", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("RoundedBodyTopDeform", dynamic_obj_list)]]

        #Body Bulge
        modifier = body_parent.modifiers.new(name="Body Bulge", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("BodyBulge", dynamic_obj_list)]]

        #Armature
        modifier = body_parent.modifiers.new(name="Ice Cube", type='ARMATURE')
        modifier.object = rig

        #Parenting
        body_parent.parent = rig


    for obj in ignore_bend_meshes_list:
        body_parent = bpy.data.objects[obj]
        rig = isRigSelected(context)

        #Chest Lattice
        modifier = body_parent.modifiers.new(name="Chest Lattice", type='LATTICE')
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

        #Chest Lattice 2
        modifier = body_parent.modifiers.new(name="Chest Lattice 2", type='LATTICE')
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

        #Body Deform
        modifier = body_parent.modifiers.new(name="Body Deform", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("BodyDeforms", dynamic_obj_list)]]


        #Body Stretch
        modifier = body_parent.modifiers.new(name="Body Stretch", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("BodyStretch", dynamic_obj_list)]]

    

        spot = modifier.driver_add("show_viewport")
        driver = spot.driver
        driver.type = 'SCRIPTED'
        var = driver.variables.new()
        var.type = 'SINGLE_PROP'
        var.name = "var"
        target = var.targets[0]
        target.id_type = 'OBJECT'
        target.id = rig
        target.data_path = "[\"body_deforms\"]"
        driver.expression = "var"

        #Rounded Top
        modifier = body_parent.modifiers.new(name="Rounded Top Deform", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("RoundedBodyTopDeform", dynamic_obj_list)]]

        #Body Bulge
        modifier = body_parent.modifiers.new(name="Body Bulge", type='LATTICE')
        modifier.object = bpy.data.objects[dynamic_obj_list[GetListIndex("BodyBulge", dynamic_obj_list)]]

        #Armature
        modifier = body_parent.modifiers.new(name="Ice Cube", type='ARMATURE')
        modifier.object = rig

        #refresh
        bpy.context.view_layer.update()
        #Parenting Variable Setup
        objP = body_parent
        rigP = rig
        if context.object.get("Body_Bend_Half") == True:
            bone = rig.pose.bones["Body_Bendy_Start"]
        else:
            bone = rig.pose.bones["Body_Bendy_End"]
        #save position data
        test_matrix = objP.matrix_world.copy()
        #parent objects
        objP.parent = rigP
        objP.parent_bone = bone.name
        objP.parent_type = 'BONE'
        objP.matrix_world = test_matrix



    #removes the key term from the name
    for obj in ignore_bend_meshes_list:
        clean_mesh_name = (obj.split(no_bend_term_to_str)[0])
        clean_mesh_name = (clean_mesh_name.split(key_term_to_str)[0])
        bpy.data.objects[obj].name = clean_mesh_name

    for obj in named_meshes_list:
        clean_mesh_name = (obj.split(key_term_to_str)[0])
        bpy.data.objects[obj].name = clean_mesh_name

    #error message
    if obj in named_meshes_list:
        pass
    elif obj in ignore_bend_meshes_list:
        pass
    else:
        CustomErrorBox("Nothing to parent!", "Parenting Exception", 'ERROR')
    
    return {'FINISHED'}

def parent_head_func(self, context):
        

        named_meshes_list = []
        dynamic_obj_list = []
        key_term = ["_HeadChild"]
        dynamic_objs = ["Head Squish"]
        bl_str = ""
        key_term_to_str = (bl_str.join(key_term))
        rig = isRigSelected(context)


        #checks if they have the proper name
        for obj in bpy.data.objects:
            if any(x in obj.name for x in key_term):
                named_meshes_list.append(obj.name)
        
        for obj in rig.children:
            if any(x in obj.name for x in dynamic_objs):
                dynamic_obj_list.append(obj.name)
        
        #gives the meshes their attributes
        for obj in named_meshes_list:
            head_parent = bpy.data.objects[obj]
            rig = isRigSelected(context)

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

            #Armature
            modifier = head_parent.modifiers.new(name="Ice Cube", type='ARMATURE')
            modifier.object = rig

            #Parenting
            head_parent.parent = rig


        #removes the key term from the name
        for obj in named_meshes_list:
            clean_mesh_name = (obj.split(key_term_to_str)[0])
            bpy.data.objects[obj].name = clean_mesh_name
        
        #error message
        if obj in named_meshes_list:
            pass
        else:
            CustomErrorBox("Nothing to parent!", "Parenting Exception", 'ERROR')
        
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
