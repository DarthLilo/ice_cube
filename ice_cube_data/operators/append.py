import bpy
import os

from ice_cube import root_folder

from ice_cube_data.utils.file_manage import getFiles
from ice_cube_data.utils.ui_tools import CustomErrorBox
from ice_cube_data.utils.selectors import isRigSelected

def append_preset_func(self, context, rig_baked):
        files_list = []
        #sets up variables
        normals = {};
        baked = {};
        obj = context.object
        try:
            selected_file = context.scene.selected_rig_preset
            asset_directory = root_folder+"/ice_cube_data/internal_files/user_packs/rigs/"+selected_file+"/rigs"
            thumbnails_directory = root_folder+"/ice_cube_data/internal_files/user_packs/rigs/"+selected_file+"/thumbnails"
        except:
            selected_file = "important"
            asset_directory = root_folder+"/ice_cube_data/internal_files/"+selected_file+"/rigs"
            thumbnails_directory = root_folder+"/ice_cube_data/internal_files/"+selected_file+"/thumbnails"
        asset_directory = os.path.normpath(asset_directory)
        thumbnails_directory = os.path.normpath(thumbnails_directory)

        dirs = getFiles(asset_directory)

        try:
            for dir in dirs:
                newDir = os.path.join(asset_directory, dir);

                for file in os.listdir(newDir):
                
                    newFile = os.path.join(newDir, file)
                    if (file.__contains__('BAKED')):
                        baked[dir] = newFile;
                    elif (file.__contains__('NORMAL')):
                        normals[dir] = newFile;
        except:
            CustomErrorBox(message="Unknown Error", title="Append Exception", icon='ERROR')
        
        thumbnailnopngmis = bpy.data.window_managers["WinMan"].my_previews_presets.split(".")[0]

        #detects if the current preset is baked or not
        def getPreset(thumbnail, isBaked):
            try:
                if isBaked:
                    return baked[thumbnail];
                else:
                    return normals[thumbnail];
            except KeyError:
                if rig_baked == True:
                    CustomErrorBox("Missing \'BAKED\' file.","Append Exception",'ERROR')
                elif rig_baked == False:
                    CustomErrorBox("Missing \'NORMAL\' file.", "Append Exception", 'ERROR')
                elif():
                    CustomErrorBox(message="Couldn't find file or folder for \""+thumbnailnopngmis+"\" from \""+selected_file+"\"", title="Append Exception", icon='ERROR')
            except:
                CustomErrorBox("Unknown Error" "Append Exception", 'ERROR')

        #sets up appending variables
        thumbnail = bpy.data.window_managers["WinMan"].my_previews_presets
        thumbnailnopng = thumbnail.split(".")[0]

        blendfile = getPreset(thumbnailnopng,rig_baked)
        if rig_baked == True:
            isBaked = "_BAKED"
        else:
            isBaked = "_NORMAL"
        blendfile_name = thumbnailnopng+isBaked+".blend"
        section = "Collection"
        obj = thumbnailnopng


        #Attemps to append it based on the previously established variables, if not, draw a custom error box
        try:
            filepath  = os.path.join(blendfile,section,obj)
            directory = os.path.join(blendfile,section)
            filename  = obj
            bpy.ops.wm.append(filepath=filepath,filename=filename,directory=directory,link=False,active_collection=True)
            CustomErrorBox("Appended \""+thumbnailnopng+"\" from \""+blendfile_name+"\" in \""+selected_file+"\"", "Operation Completed", 'CHECKMARK')
        except RuntimeError:
            CustomErrorBox("Please delete any \".blend1\" files from the directory!", "Directory Error", 'ERROR')
        except:
            CustomErrorBox("An unknown error has occured.", "Unknown Error", 'ERROR')

        return{'FINISHED'}

def append_default_rig(self, context):
    #sets up variables
    
    script_directory = root_folder
    script_directory = os.path.join(script_directory, "ice_cube_data/internal_files/rigs")
    script_directory = os.path.normpath(script_directory)
    blendfile = os.path.join(script_directory, "Ice Cube.blend")
    section = "Collection"
    obj = "Ice Cube"
    filepath = os.path.join(blendfile,section,obj)
    directory = os.path.join(blendfile,section)
    filename = obj
    #appends the rig
    bpy.ops.wm.append(filepath=filepath,filename=filename,directory=directory,link=False,active_collection=True)
    return {'FINISHED'}

def append_emotion_line_func(self, context):
        emotion_line_dir = root_folder+"/ice_cube_data/internal_files/rigs"
        emotion_line_dir = os.path.normpath(emotion_line_dir)

        blendfile = os.path.join(emotion_line_dir, "emotion_line.blend")
        section = "Collection"
        obj = "emotion_line"
        filepath = os.path.join(blendfile,section,obj)
        directory = os.path.join(blendfile,section)
        filename = obj
        #appends the mesh
        bpy.ops.wm.append(filepath=filepath,filename=filename,directory=directory,link=False,active_collection=True)

        obj1 = bpy.context.selected_objects[0]
        obj2 = bpy.context.selected_objects[1]
        rig = isRigSelected(context)

        #parent objects
        obj1.parent = rig

        
        obs = [bpy.data.objects[str(rig.name)], bpy.data.objects[str(obj2.name)]]

        c = {}
        c["object"] = bpy.data.objects[str(rig.name)]
        c["active_object"] = bpy.data.objects[str(rig.name)]
        c["selected_objects"] = obs
        c["selected_editable_objects"] = obs
        bpy.ops.object.join(c)

        root_bones_list = []
        mesh_line_list = []
        bend_bone_list = []
        dynamic_obj_list = []
        key_term = ["_ImANewEmotion"]
        key_term2 = ["_ImALineThing"]
        key_term3 = ["_ImAnInternalBend"]
        dynamic_objs = ["Head Squish"]
        bl_str = ""
        key_term_to_str = (bl_str.join(key_term))
        key_term2_to_str = (bl_str.join(key_term2))
        key_term3_to_str = (bl_str.join(key_term3))

        #checks if they have the proper name
        for bones in rig.pose.bones:
            if any(x in bones.name for x in key_term):
                root_bones_list.append(bones.name)

        for obj in bpy.data.objects:
            if any(x in obj.name for x in key_term2):
                mesh_line_list.append(obj.name)
        
        for bones in rig.pose.bones:
            if any(x in bones.name for x in key_term3):
                bend_bone_list.append(bones.name)
        
        for obj in rig.children:
            if any(x in obj.name for x in dynamic_objs):
                dynamic_obj_list.append(obj.name)

        
        #add constraints to root bone
        for bones in root_bones_list:
            cbone = rig.pose.bones[bones]
            constraint = cbone.constraints.new(type='CHILD_OF')
            constraint.name = 'Parenting DON\'T TOUCH'
            constraint.target = rig
            constraint.subtarget = "headsquish"
        #add modifiers to mesh line
        for obj in mesh_line_list:
            mesh_line = bpy.data.objects[obj]
            rig = isRigSelected(context)
            mat = bpy.data.materials.get("Emotion_Line")

            #Head Squish
            modifier = mesh_line.modifiers.new(name="Head Squish", type='LATTICE')
            modifier.object = bpy.data.objects[str(dynamic_obj_list[0])]

            modifier = mesh_line.modifiers.new(name="Ice Cube", type='ARMATURE')
            modifier.object = rig

            modifier = mesh_line.modifiers.new(name="Subsurf Mod", type='SUBSURF')
            modifier.levels = 1
            modifier.render_levels = 2

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
            driver.expression = "+1 - var"

            vg = mesh_line.vertex_groups.new(name=bend_bone_list[0])
            verts = []
            for vert in mesh_line.data.vertices:
                verts.append(vert.index)
            vg.add(verts, 1.0, 'ADD')

            if mesh_line.data.materials:
                mesh_line.data.materials[0] = mat
            else:
                mesh_line.data.materials.append(mat)
        
        #removes the key term from the name
        for bones in root_bones_list:
            cbone = rig.pose.bones[bones]
            clean_mesh_name = (cbone.name.split(key_term_to_str)[0])
            cbone.name = clean_mesh_name
        
        for obj in mesh_line_list:
            newobj = bpy.data.objects[obj]
            clean_mesh_name = (newobj.name.split(key_term2_to_str)[0])
            newobj.name = clean_mesh_name
        
        for bones in bend_bone_list:
            cbone = rig.pose.bones[bones]
            clean_mesh_name = (cbone.name.split(key_term3_to_str)[0])
            cbone.name = clean_mesh_name

        return{'FINISHED'}

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