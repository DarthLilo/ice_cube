import bpy, json, os, traceback
from urllib import request
from base64 import b64decode

from ..ice_cube_selectors import GetMaterialHolder, GetMaterial
from ..utils import CustomPopupBox, UnpackImage, IsOldSkinFormat
from ..constants import SKIN_STORAGE, DEFAULT_SKIN

class ICECUBE_DOWNLOAD_SKIN(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.download_skin'
    bl_label = "Skin Downloader"

    def execute(self, context):

        minecraft_username = context.scene.ice_cube_minecraft_username
        current_skin = GetMaterial(context, 'skin').node_tree.nodes['Skin Texture'].image

        if not minecraft_username:
            CustomPopupBox("Please enter a username!","No Username!")
            return {'FINISHED'}
        
        try:
            # Attempts to get the UUID/Username information from mojangs API
            response = json.loads(request.urlopen("https://api.mojang.com/users/profiles/minecraft/"+minecraft_username).read().decode())
            minecraft_uuid = response['id']
            minecraft_accurate_username = response['name']

            try:
                raw_texture_data = json.loads(request.urlopen("https://sessionserver.mojang.com/session/minecraft/profile/"+minecraft_uuid).read().decode())['properties'][0]['value']
                decoded_texture = str(b64decode(raw_texture_data), 'utf-8')
                texture_data = json.loads(decoded_texture)['textures']
                skin_data = texture_data['SKIN']['url']

                #Grab Player Model
                try:
                    player_model = texture_data['SKIN']['metadata']['model']
                except:
                    player_model = "classic"
                
                try:
                    skin_filename = f"{minecraft_accurate_username}_{player_model}_skin.png"
                    skins_folder = SKIN_STORAGE
                    os.makedirs(skins_folder,exist_ok=True)

                    skin_path = os.path.join(skins_folder,skin_filename)
                    UnpackImage(current_skin)

                    request.urlretrieve(skin_data,skin_path)
                    if IsOldSkinFormat(skin_path) == True:
                        CustomPopupBox("The requested skin was in a pre 1.8 format, please convert it and manually apply!","Wrong Skin Format!",'ERROR')
                        return {'FINISHED'}
                    else:
                        current_skin.filepath = skin_path
                        if player_model == "slim":
                            context.object.arm_type = '2'
                        else:
                            context.object.arm_type = '1'
                except:
                    CustomPopupBox("Failed to download skin, check console for more info!",'Skin Download Error','ERROR')
                    traceback.print_exc()
            except:
                CustomPopupBox("Error while fetching skin data, check console for more info!",'Too Many Requests','ERROR')
                traceback.print_exc()
        except:
            CustomPopupBox(f"Unable to find a user with the name {minecraft_username}!",'Invalid Username')

        return {'FINISHED'}

class ICECUBE_APPLY_SKIN(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.apply_skin'
    bl_label = "Apply Skin"

    def execute(self, context):
        try:
            selected_skin = context.window_manager.ice_cube_skin_library.skin_library
            if not selected_skin:
                return {'FINISHED'}
            
            current_skin = GetMaterial(context, 'skin').node_tree.nodes['Skin Texture'].image
            UnpackImage(current_skin)
            current_skin.filepath = os.path.join(SKIN_STORAGE, selected_skin)
            if str(selected_skin).__contains__("slim"):
                context.object.arm_type = '2'
            else:
                context.object.arm_type = '1'

        except:
            CustomPopupBox("Something has gone wrong, check the console for more info!",'Error','ERROR')
            traceback.print_exc()
        
        return {'FINISHED'}

class ICECUBE_RESET_SKIN(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.reset_skin'
    bl_label = "Reset Skin"

    def execute(self, context):
        try:
            current_skin = GetMaterial(context, 'skin').node_tree.nodes['Skin Texture'].image
            UnpackImage(current_skin)
            current_skin.filepath = DEFAULT_SKIN
            context.object.arm_type = '1'
        except:
            CustomPopupBox("Something has gone wrong, check the console for more info!",'Error','ERROR')
            traceback.print_exc()
        
        return {'FINISHED'}

class ICECUBE_DELETE_SKIN(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.delete_skin'
    bl_label = "Delete Skin"

    def execute(self, context):
        try:
            selected_skin = context.window_manager.ice_cube_skin_library.skin_library
            if not selected_skin:
                return {'FINISHED'}
            
            current_skin = GetMaterial(context, 'skin').node_tree.nodes['Skin Texture'].image
            UnpackImage(current_skin)
            current_skin.filepath = DEFAULT_SKIN
            context.object.arm_type = '1'
            os.remove(os.path.join(SKIN_STORAGE, selected_skin))

        except:
            CustomPopupBox("Something has gone wrong, check the console for more info!",'Error','ERROR')
            traceback.print_exc()
        
        return {'FINISHED'}
