#Libraries
import bpy
import os
import json
from bpy.props import EnumProperty

#Custom Libraries
from ice_cube import root_folder, cur_asset_id
from ice_cube_data.utils.ui_tools import CustomErrorBox
from ice_cube_data.utils.file_manage import getFiles
from ice_cube_data.utils.selectors import isRigSelected

############Entries Code############

#File Variables
asset_entries_list = []
asset_entries_names = []

def RefreshEntriesList():
    items = []
    items = asset_entries_list
    return items

#File Variables
asset_pack_list = []
asset_pack_names = []

#File Definition
internalfiles = os.path.join(root_folder, "ice_cube_data/internal_files/user_packs/inventory")
user_packs = os.path.normpath(internalfiles)

def RefreshInvList():
    items = []
    items = asset_pack_list
    return items

bpy.types.Scene.selected_inv_asset = EnumProperty(
        name = "Selected Pack",
        items = [('NONE', 'REFRESH','REFRESH')]
        )

bpy.types.Scene.asset_entries = EnumProperty(
        name = "Asset Entries",
        items = [('Default', 'Default Entry','Default Entry')]
        )

#Armor Trim Colors
armor_trim_colors = {
    "Amethyst" : [[0.000000, 0.000000, 0.000000, 1.000000],[0.008568, 0.001821, 0.043735, 1.000000],[0.017642, 0.003677, 0.086500, 1.000000],[0.036889, 0.011612, 0.144129, 1.000000],[0.054480, 0.020289, 0.181164, 1.000000],[0.084376, 0.036889, 0.242281, 1.000000],[0.149960, 0.066626, 0.401978, 1.000000],[0.323143, 0.107023, 0.564712, 1.000000],[0.584079, 0.274677, 0.896270, 1.000000]],
    "Copper" : [[0.000000, 0.000000, 0.000000, 1.000000],[0.046665, 0.009134, 0.003347, 1.000000],[0.072272, 0.014444, 0.005182, 1.000000],[0.114435, 0.024158, 0.009134, 1.000000],[0.152926, 0.034340, 0.014444, 1.000000],[0.191202, 0.045186, 0.021219, 1.000000],[0.323143, 0.063010, 0.025187, 1.000000],[0.456411, 0.138432, 0.074214, 1.000000],[0.768151, 0.223228, 0.149960, 1.000000]],
    "Diamond" : [[0.000000, 0.000000, 0.000000, 1.000000],[0.000304, 0.045186, 0.063010, 1.000000],[0.001214, 0.082283, 0.114435, 1.000000],[0.002125, 0.130137, 0.187821, 1.000000],[0.003677, 0.187821, 0.266356, 1.000000],[0.012286, 0.304987, 0.323143, 1.000000],[0.025187, 0.491021, 0.391573, 1.000000],[0.155926, 0.838799, 0.644480, 1.000000],[0.597202, 1.000000, 0.913099, 1.000000]],
    "Diamond_darker" : [[0.000000, 0.000000, 0.000000, 1.000000],[0.001214, 0.051269, 0.048172, 1.000000],[0.000911, 0.061246, 0.054480, 1.000000],[0.002732, 0.082283, 0.064803, 1.000000],[0.001821, 0.109462, 0.104617, 1.000000],[0.000607, 0.174647, 0.168269, 1.000000],[0.001214, 0.219526, 0.234551, 1.000000],[0.003035, 0.332452, 0.356400, 1.000000],[0.007499, 0.450786, 0.356400, 1.000000]],
    "Emerald" : [[0.000000, 0.000000, 0.000000, 1.000000],[0.000607, 0.046665, 0.004391, 1.000000],[0.000911, 0.080220, 0.006512, 1.000000],[0.002732, 0.124772, 0.010960, 1.000000],[0.004391, 0.168269, 0.015996, 1.000000],[0.005182, 0.198069, 0.017642, 1.000000],[0.005605, 0.351533, 0.036889, 1.000000],[0.004391, 0.571125, 0.088656, 1.000000],[0.223228, 0.921582, 0.417885, 1.000000]],
    "Gold" : [[0.000000, 0.000000, 0.000000, 1.000000],[0.095307, 0.016807, 0.000000, 1.000000],[0.165132, 0.026241, 0.000000, 1.000000],[0.215861, 0.035601, 0.000911, 1.000000],[0.351533, 0.059511, 0.003035, 1.000000],[0.439657, 0.135633, 0.006049, 1.000000],[0.730461, 0.439657, 0.026241, 1.000000],[0.838799, 0.693872, 0.049707, 1.000000],[1.000000, 0.982251, 0.278894, 1.000000]],
    "Gold_darker" : [[0.000000, 0.000000, 0.000000, 1.000000],[0.048172, 0.010960, 0.000911, 1.000000],[0.095307, 0.016807, 0.000000, 1.000000],[0.165132, 0.026241, 0.000000, 1.000000],[0.215861, 0.035601, 0.000911, 1.000000],[0.250158, 0.063010, 0.003677, 1.000000],[0.366253, 0.114435, 0.006995, 1.000000],[0.491021, 0.226966, 0.020289, 1.000000],[0.539480, 0.332452, 0.023153, 1.000000]],
    "Iron" : [[0.000000, 0.000000, 0.000000, 1.000000],[0.061246, 0.082283, 0.082283, 1.000000],[0.095307, 0.124772, 0.124772, 1.000000],[0.130137, 0.162029, 0.162029, 1.000000],[0.165132, 0.205079, 0.205079, 1.000000],[0.198069, 0.250158, 0.250158, 1.000000],[0.337164, 0.401978, 0.401978, 1.000000],[0.520996, 0.584079, 0.577581, 1.000000],[0.558341, 0.644480, 0.658375, 1.000000]],
    "Iron_darker" : [[0.000000, 0.000000, 0.000000, 1.000000],[0.012286, 0.021219, 0.021219, 1.000000],[0.024158, 0.034340, 0.034340, 1.000000],[0.030713, 0.043735, 0.043735, 1.000000],[0.030713, 0.043735, 0.043735, 1.000000],[0.095307, 0.124772, 0.124772, 1.000000],[0.158961, 0.181164, 0.181164, 1.000000],[0.254152, 0.287441, 0.283149, 1.000000],[0.361307, 0.434154, 0.450786, 1.000000]],
    "Lapis" : [[0.000000, 0.000000, 0.000000, 1.000000],[0.001518, 0.008023, 0.036889, 1.000000],[0.002732, 0.012983, 0.059511, 1.000000],[0.002732, 0.012983, 0.059511, 1.000000],[0.005605, 0.027321, 0.124772, 1.000000],[0.006049, 0.033105, 0.130137, 1.000000],[0.015209, 0.066626, 0.198069, 1.000000],[0.011612, 0.074214, 0.332452, 1.000000],[0.052861, 0.155926, 0.309469, 1.000000]],
    "Netherite" : [[0.000000, 0.000000, 0.000000, 1.000000],[0.002732, 0.002125, 0.002125, 1.000000],[0.005182, 0.003677, 0.003677, 1.000000],[0.010330, 0.008023, 0.008023, 1.000000],[0.016807, 0.012983, 0.012983, 1.000000],[0.028426, 0.020289, 0.020289, 1.000000],[0.030713, 0.027321, 0.030713, 1.000000],[0.057805, 0.042311, 0.043735, 1.000000],[0.102242, 0.095307, 0.102242, 1.000000]],
    "Netherite_darker" : [[0.000000, 0.000000, 0.000000, 1.000000],[0.003347, 0.002732, 0.002732, 1.000000],[0.006995, 0.004777, 0.004777, 1.000000],[0.012286, 0.006512, 0.006512, 1.000000],[0.013702, 0.008568, 0.008568, 1.000000],[0.017642, 0.010330, 0.010330, 1.000000],[0.021219, 0.012286, 0.012286, 1.000000],[0.021219, 0.017642, 0.018500, 1.000000],[0.027321, 0.021219, 0.022174, 1.000000]],
    "Quartz" : [[0.000000, 0.000000, 0.000000, 1.000000],[0.023153, 0.021219, 0.015996, 1.000000],[0.059511, 0.056129, 0.045186, 1.000000],[0.130137, 0.119538, 0.093059, 1.000000],[0.278894, 0.270498, 0.215861, 1.000000],[0.467784, 0.417885, 0.304987, 1.000000],[0.768151, 0.708376, 0.552011, 1.000000],[0.921582, 0.822786, 0.737911, 1.000000],[0.887923, 0.863157, 0.846874, 1.000000]],
    "Redstone" : [[0.000000, 0.000000, 0.000000, 1.000000],[0.012286, 0.001518, 0.000607, 1.000000],[0.036889, 0.002428, 0.000911, 1.000000],[0.084376, 0.004025, 0.001821, 1.000000],[0.130137, 0.003347, 0.000304, 1.000000],[0.187821, 0.005605, 0.000304, 1.000000],[0.309469, 0.008023, 0.002125, 1.000000],[0.508881, 0.014444, 0.002428, 1.000000],[0.791298, 0.014444, 0.002428, 1.000000]]
}


#Gets a list of assets in the "inventory" folder
class refresh_inventory_list(bpy.types.Operator):
    bl_idname = "refresh.inv_list"
    bl_label = "refresh inv list"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):
        #Clearing the old lists
        asset_pack_list.clear()
        asset_pack_names.clear()
        
        #variables
        count = 1

        #Updating the list of installed packs
        for file in getFiles(user_packs):
            description = f"Asset ID: {count}"
            item_descriptor = (file, file, description)
            asset_pack_list.append(item_descriptor)
            asset_pack_names.append(file)
            count += 1
        
        
        #Drawing the custom property
        bpy.types.Scene.selected_inv_asset = EnumProperty(
        name = "Selected Pack",
        items = RefreshInvList()
        )

        try:
            context.scene.selected_inv_asset = asset_pack_names[0]
        except:
            pass

        return{'FINISHED'}

def gettingCustomizationJson(context):
    scene = context.scene
    obj = context.object
    thumbnail = bpy.data.window_managers["WinMan"].inventory_preview
    thumbnailnopng = thumbnail.split(".")[0]


    asset_missing_file_dir_inf = root_folder+"/ice_cube_data/internal_files/important/missing_info.json"
    
    cur_asset = context.scene.get("selected_inv_asset")
    if cur_asset != None:
        cur_selected_asset = context.scene.selected_inv_asset
        asset_info_dir = f"{root_folder}/ice_cube_data/internal_files/user_packs/inventory/{cur_selected_asset}/assets/{thumbnailnopng}/info.json"
    else:
        asset_info_dir = root_folder+"/ice_cube_data/internal_files/important/info_asset.json"

    try:
        with open(asset_info_dir, 'r') as notmyfile:
            asset_data_inf = notmyfile.read()
    except:
        with open(asset_missing_file_dir_inf, 'r') as notmyfile:
            asset_data_inf = notmyfile.read()

    asset_infodata = json.loads(asset_data_inf)

    return asset_infodata

class refresh_customizations(bpy.types.Operator):
    bl_idname = "refresh.customizations"
    bl_label = "refresh customizations"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        #clearing old list data
        asset_entries_list.clear()
        asset_entries_names.clear()
        cur_asset_id.clear()

        count = 1

        #updating list
        try:
            cus_json_data = gettingCustomizationJson(context)
            asset_id = str(cus_json_data['asset_id']) #Asset ID
            try:
                cus_entries = cus_json_data['asset_settings']['entries'] #A list of asset entries


                for entry in cus_entries:
                    item_descriptor = (entry,entry,f"Asset ID: {count}")
                    asset_entries_list.append(item_descriptor)
                    asset_entries_names.append(entry)
                    cur_asset_id.append(asset_id)

                    count += 1
            except:
                print("No Entries Found, Ignoring")
                cur_asset_id.append(asset_id)
            
            bpy.types.Scene.asset_entries = EnumProperty(
            name = "Asset Entries",
            items = RefreshEntriesList()
            )


        except KeyError:
            CustomErrorBox("The selected asset has no customization options","No Customization Options",'ERROR')
        

        try:
            context.scene.asset_entries = asset_entries_names[0]
            context.object.armor_trim_material = 'Amethyst'
            context.object.armor_trim_pattern = 'none'
        except:
            pass


        return{'FINISHED'}

#Append Asset Class
class append_asset(bpy.types.Operator):
    bl_idname = "append.asset"
    bl_label = "append asset"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):
        assets = {};
        obj = context.object
        scene = context.scene
        default_collection = True
        json_data = gettingCustomizationJson(context)
        rig = isRigSelected(context)
        extension = ""
        customizable = bool(json_data['customizable'])

        try:
            if json_data['asset_settings']['entries']:
                default_collection = False
            else:
                default_collection = True
        except KeyError:
            pass

        if cur_asset_id[0] != json_data['asset_id']:
            obj.armor_trim_material = 'Amethyst'
            obj.armor_trim_pattern = 'none'
            bpy.types.Scene.asset_entries = EnumProperty(
            name = "Asset Entries",
            items = [('Default', 'Default Entry','Default Entry')]
            )
            scene.asset_entries = 'Default'
            print("CHANGED")

        
        

        #Tries to get a list of all files in [SELECTED ASSET PACK], if none is found it defaults to a backup.
        try:
            selected_file = context.scene.selected_inv_asset
            asset_directory = root_folder+"/ice_cube_data/internal_files/user_packs/inventory/"+selected_file+"/assets"
            thumbnails_directory = root_folder+"/ice_cube_data/internal_files/user_packs/inventory/"+selected_file+"/thumbnails"
            textures_directory = root_folder+"/ice_cube_data/internal_files/user_packs/inventory/"+selected_file+"/textures" #OPTIONAL FOR MOST ASSET PACKS
        except:
            selected_file = "important"
            asset_directory = root_folder+"/ice_cube_data/internal_files/"+selected_file+"/assets"
            thumbnails_directory = root_folder+"/ice_cube_data/internal_files/"+selected_file+"/thumbnails"
        asset_directory = os.path.normpath(asset_directory)
        thumbnails_directory = os.path.normpath(thumbnails_directory)

        dirs = getFiles(asset_directory)

        try:
            for dir in dirs:
                newDir = os.path.join(asset_directory, dir);

                for file in os.listdir(newDir):
                
                    newFile = os.path.join(newDir, file)
                    assets[dir] = newFile;
        except:
            CustomErrorBox(message="Unknown Error", title="Append Exception", icon='ERROR')

        #Gets the thumbnail data
        thumbnail = bpy.data.window_managers["WinMan"].inventory_preview
        thumbnailnopng = thumbnail.split(".")[0]
        
        #Sets up appending variables
        blendfile = f"{asset_directory}/{thumbnailnopng}/{thumbnailnopng}.blend"
        blendfile_name = thumbnailnopng+".blend"
        section = "Collection"
        if default_collection == True:
            obj = thumbnailnopng
        else:
            obj = context.scene.asset_entries
        



        #Appends the rig using established variables before, if failed, give a custom error message
        try:
            filepath  = os.path.join(blendfile,section,obj)
            directory = os.path.join(blendfile,section)
            filename  = obj
            bpy.ops.wm.append(filepath=filepath,filename=filename,directory=directory,link=False,active_collection=True)
            CustomErrorBox("Appended \""+thumbnailnopng+"\" from \""+blendfile_name+"\" in \""+selected_file+"\"", "Operation Completed", 'CHECKMARK')
        except:
            CustomErrorBox("An unknown error has occured.", "Unknown Error", 'ERROR')

        #####Armor Trim Support

        armor_trim_mats = []
        key_term = ["_ArmorTrimMat"]
        bl_str = ""
        key_term_to_string = (bl_str.join(key_term))
        darker = ""

        for mat in bpy.data.materials:
            if any(x in mat.name for x in key_term):
                armor_trim_mats.append(mat.name)

        try:
            if json_data['customizable']:
                if json_data['asset_settings']['supports_armor_trims']:
                    if rig.get("armor_trim_pattern") != None and rig.get("armor_trim_pattern") != 0:

                        material_type = json_data['asset_settings']['materialType']
                        
                        cur_pattern = rig.armor_trim_pattern
                        pattern_mat = rig.armor_trim_material
    
                        if default_collection == False:
                            if context.scene.asset_entries == rig.armor_trim_material:
                                darker = "_darker"
                        elif customizable == True and str(rig.armor_trim_material).lower() == str(material_type).lower():
                            darker = "_darker"
    
                        if json_data['asset_settings']['leggings_half']:
                            extension = "_leggings"
    
                        #applying changes
    
                        for mat in armor_trim_mats:

                            if material_type != "leather":
                        
                                armor_mat = bpy.data.materials[mat]
                                node_tree = armor_mat.node_tree
                                nodes = node_tree.nodes
                                links = node_tree.links
                                bsdf = nodes.get("Principled BSDF")
                                base_loc = bsdf.location
                                org_tex = nodes.get("Armor Texture")

                                #pattern node
                                pattern = nodes.new('ShaderNodeTexImage')
                                pattern.name = "Armor Trim Pattern"
                                pattern.location = (base_loc[0]-850,base_loc[1])
                                pattern_texture = bpy.data.images.load(f"{textures_directory}/{cur_pattern}{extension}.png")
                                nodes["Armor Trim Pattern"].image = pattern_texture
                                pattern.interpolation = 'Closest'

                                #base texture node
                                org_tex.location = (base_loc[0]-850,base_loc[1]+350)

                                #mix node
                                mix = nodes.new('ShaderNodeMix')
                                mix.name = "Armor Trim Mix"
                                mix.location = (base_loc[0]-225,base_loc[1]+175)
                                mix.data_type = 'RGBA'

                                #pallete node
                                pallete = nodes.new('ShaderNodeValToRGB')
                                pallete.name = "Pallete Node"
                                pallete.location = (base_loc[0]-555,base_loc[1])
                                pallete.color_ramp.interpolation = 'CONSTANT'
                                elements = pallete.color_ramp.elements
                                #element_colors = [[0.000000, 0.000000, 0.000000, 1.000000],[0.005605, 0.005605, 0.005605, 1.000000],[0.014444, 0.014444, 0.014444, 1.000000],[0.051269, 0.051269, 0.051269, 1.000000],[0.116971, 0.116971, 0.116971, 1.000000],[0.215861, 0.215861, 0.215861, 1.000000],[0.351533, 0.351533, 0.351533, 1.000000],[0.527115, 0.527115, 0.527115, 1.000000],[0.745404, 0.745404, 0.745404, 1.000000]]
                                element_colors = armor_trim_colors[f"{pattern_mat}{darker}"]
                                element_pos = [0,0.002,0.007683,0.049982,0.111502,0.204226,0.342723,0.525823,0.741785]

                                for i in range(len(element_pos)):
                                    element = elements.new(element_pos[i])
                                    element.color = element_colors[i]
                                elements.remove(elements[0])
                                elements.remove(elements[9])


                                #linking nodes
                                links.new(org_tex.outputs[0], mix.inputs[6])
                                node_tree.links.new(pattern.outputs[0], pallete.inputs[0])
                                node_tree.links.new(pallete.outputs[0], mix.inputs[7])
                                node_tree.links.new(pattern.outputs[1], mix.inputs[0])
                                node_tree.links.new(mix.outputs[2], bsdf.inputs[0])

                            elif material_type == "leather":
                                armor_mat = bpy.data.materials[mat]
                                node_tree = armor_mat.node_tree
                                nodes = node_tree.nodes
                                links = node_tree.links
                                leathermat = nodes.get("Leather MAT")
                                base_loc = leathermat.location

                                #pattern node
                                pattern = nodes.new('ShaderNodeTexImage')
                                pattern.name = "Armor Trim Pattern"
                                pattern.location = (base_loc[0]-850,base_loc[1])
                                pattern_texture = bpy.data.images.load(f"{textures_directory}/{cur_pattern}{extension}.png")
                                nodes["Armor Trim Pattern"].image = pattern_texture
                                pattern.interpolation = 'Closest'

                                #pallete node
                                pallete = nodes.new('ShaderNodeValToRGB')
                                pallete.name = "Pallete Node"
                                pallete.location = (base_loc[0]-555,base_loc[1])
                                pallete.color_ramp.interpolation = 'CONSTANT'
                                elements = pallete.color_ramp.elements
                                #element_colors = [[0.000000, 0.000000, 0.000000, 1.000000],[0.005605, 0.005605, 0.005605, 1.000000],[0.014444, 0.014444, 0.014444, 1.000000],[0.051269, 0.051269, 0.051269, 1.000000],[0.116971, 0.116971, 0.116971, 1.000000],[0.215861, 0.215861, 0.215861, 1.000000],[0.351533, 0.351533, 0.351533, 1.000000],[0.527115, 0.527115, 0.527115, 1.000000],[0.745404, 0.745404, 0.745404, 1.000000]]
                                element_colors = armor_trim_colors[f"{pattern_mat}{darker}"]
                                element_pos = [0,0.002,0.007683,0.049982,0.111502,0.204226,0.342723,0.525823,0.741785]

                                for i in range(len(element_pos)):
                                    element = elements.new(element_pos[i])
                                    element.color = element_colors[i]
                                elements.remove(elements[0])
                                elements.remove(elements[9])


                                #linking nodes
                                node_tree.links.new(pattern.outputs[0], pallete.inputs[0])
                                node_tree.links.new(pattern.outputs[1], leathermat.inputs[1])
                                node_tree.links.new(pallete.outputs[0], leathermat.inputs[0])




                        
        except KeyError:
            pass

        #removing tag
        for mat in armor_trim_mats:
            new_armor = bpy.data.materials[mat]
            clean_armor_name = (new_armor.name.split(key_term_to_string)[0])
            new_armor.name = clean_armor_name

        return{'FINISHED'}


#Attempts to create the enumerator property, if it fails it goes to a backup version.




classes = [
    refresh_inventory_list,
    refresh_customizations,
    append_asset,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__=="__main__":
    register()