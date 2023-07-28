#Libraries
import bpy
import os
import json
from base64 import b64decode
from urllib import request

#Custom Libraries
from ice_cube import root_folder
from ice_cube_data.utils.ui_tools import CustomErrorBox
from ice_cube_data.utils.selectors import isRigSelected, main_face
from ice_cube_data.utils.file_manage import unpack_img
from ice_cube_data.utils.general_func import isOldSkin

def getSkinNode():
    material_list = {}
    materials = bpy.data.materials
    for mat in materials:
        try:
            if mat["ice_cube_material"]:
                material_list[mat["ice_cube_material"]] = mat
        except KeyError:
            pass
    
    return material_list['skin']

#Downloads a skin based on a username
class skin_downloader(bpy.types.Operator):
    bl_idname = "skin.download"
    bl_label = "skin downloader"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):

        
        
        #variable setup
        username = context.scene.minecraft_username
        current_skin = getSkinNode().node_tree.nodes['Skin Tex'].image
        
        #Checks if there is no username, if so, display an error, if not, try to download it.
        if not username:
            CustomErrorBox(message= "Please enter a username!", title = "Skin Exception", icon='ERROR')
        else:
            try:
                #downloads the usernames information
                username_uuid = json.loads(request.urlopen("https://api.mojang.com/users/profiles/minecraft/"+username).read().decode())['id']
                Nusername = json.loads(request.urlopen("https://api.mojang.com/users/profiles/minecraft/"+username).read().decode())['name']
                #attempts to download the UUID skin
                try:
                    #gets UUID data
                    texture_raw = json.loads(request.urlopen("https://sessionserver.mojang.com/session/minecraft/profile/"+username_uuid).read().decode())['properties'][0]['value']
                    decoded_texture = str(b64decode(texture_raw), 'utf-8')
                    texture_data = json.loads(decoded_texture)['textures']
                    skin = texture_data['SKIN']['url']
                    #attempts to retreive model data, if none, default to classic
                    try:
                        player_model = texture_data['SKIN']['metadata']['model']
                    except:
                        player_model = "classic"

                    #Attempt to actually save the skin file
                    try:
                        #locates the skins directory
                        skin_filename = "{}_skin_".format(Nusername)
                        skin_filename = skin_filename+player_model+".png"
                        skin_path = os.path.join(root_folder,'ice_cube_data/internal_files/skins/',skin_filename)

                        #unpacks the current skin
                        unpack_img(current_skin)

                        #downloads, applies, and then packs the new skin.
                        request.urlretrieve(skin, skin_path)
                        if isOldSkin(skin_path) == True:
                            CustomErrorBox("Downloaded skin but failed to apply skin.\nPlease convert to 1.8 format!","Skin Format Error",'ERROR')
                        else:
                            current_skin.filepath = skin_path
                            current_skin.pack()
                            #sets the player model of the rig depending on which result came up
                            if player_model == "slim":
                                context.object.armtype_enum = 'two' #alex
                            else:
                                context.object.armtype_enum = 'one' #steve
    
                            CustomErrorBox(message="Downloaded and applied the skin for "+Nusername+"!", title="Skin Saved!", icon='INFO')
                    except:
                        CustomErrorBox(message="Failed to download skin", title="Skin Exception", icon='ERROR')
                except:
                    CustomErrorBox(message="Too many requests, please wait a while.")
            except:
                CustomErrorBox(message="Failed to find a user with the name "+username+"!")

        return{'FINISHED'}

#Applies a skin based of a selected image
class apply_skin(bpy.types.Operator):
    bl_idname = "skin.apply"
    bl_label = "idk this exists"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        
        try:
            #sets up variables
            thumbnail = bpy.data.window_managers["WinMan"].skins_folder
            skin_nodes = getSkinNode().node_tree
            current_skin = skin_nodes.nodes['Skin Tex'].image
            skin_path = root_folder+"/ice_cube_data/internal_files/skins/"
            skin_path = skin_path+thumbnail
            if isOldSkin(skin_path) == True:
                CustomErrorBox("Unable to apply selected skin, please convert it to the 1.8 skin format!","Skin Format Error",'ERROR')
            else:
                #unpacks the current image
                unpack_img(current_skin)
                #applies the skin
                current_skin.filepath = skin_path
                #packs the new skin
                current_skin.pack()
                #changes the rigs model depending on which tag is in the name
                if str(thumbnail).__contains__("slim"):
                    context.object.armtype_enum = 'two' #alex
                elif str(thumbnail).__contains__("classic"):
                    context.object.armtype_enum = 'one' #steve
                else:
                    pass
        except:
            CustomErrorBox(message="An Unknown Error Has Occurred", title="Skin Exception", icon='ERROR')
        return{'FINISHED'}

#Resets the skin to default
class reset_skin(bpy.types.Operator):
    bl_idname = "skin.reset"
    bl_label = "idk this exists"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        
        try:
            #Sets up variables
            skin_nodes = getSkinNode().node_tree
            current_skin = skin_nodes.nodes['Skin Tex'].image
            skin_path = root_folder+"/ice_cube_data/internal_files/rigs/textures/skin.png"
            #unpacks the skin
            unpack_img(current_skin)
            #applies the new skin
            current_skin.filepath = skin_path
            #packs the new skin
            current_skin.pack()
            #resets arms to classic
            context.object.armtype_enum = 'one'
        except:
            CustomErrorBox(message="An Unknown Error Has Occurred", title="Skin Exception", icon='ERROR')
        return{'FINISHED'}

#deletes the selected skin file
class delete_skin(bpy.types.Operator):
    bl_idname = "skin.delete"
    bl_label = "idk this exists"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        
        try:
            #sets up variables
            thumbnail = bpy.data.window_managers["WinMan"].skins_folder
            skin_nodes = getSkinNode().node_tree
            current_skin = skin_nodes.nodes['Skin Tex'].image
            skin_path = root_folder+"/ice_cube_data/internal_files/skins/"
            default_skin = root_folder+"/ice_cube_data/internal_files/rigs/textures/skin.png"
            skin_path = skin_path+"\\"+thumbnail
            skin_path = os.path.normpath(skin_path)
            #if the skin on the rig matches the selected skin, unpack it, reset it to default, and re-pack it
            current_skin1 = os.path.normpath(current_skin.filepath)
            if current_skin1 == skin_path:
                unpack_img(current_skin)
                current_skin.filepath = default_skin
                current_skin.pack()
                context.object.armtype_enum = 'one'
            #removes the currently selected skin
            os.remove(skin_path)
        except:
            CustomErrorBox(message="An Unknown Error Has Occurred", title="Skin Exception", icon='ERROR')
        return{'FINISHED'}

classes = [skin_downloader,
           apply_skin,
           reset_skin,
           delete_skin,
           ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__=="__main__":
    register()