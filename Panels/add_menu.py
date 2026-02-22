import bpy, os, json

from ..icons import ice_cube_icons_collection
from ..constants import CHARACTER_STORAGE

CHARACTERS = {}
CHARACTER_ICONS = None

def fetchCharacters():

    print("Fetching saved characters")

    # Library Check
    if not os.path.exists(CHARACTER_STORAGE):
        os.makedirs(CHARACTER_STORAGE,exist_ok=True)

    CHARACTERS.clear()
    
    for character in os.listdir(CHARACTER_STORAGE): # Loop for every character folder in 
        character_folder = os.path.join(CHARACTER_STORAGE,character)
        c_json = os.path.join(character_folder,"character.json")
        if not os.path.exists(c_json):
            print(f"Failed to find character.json in {character}")
            continue

        with open(c_json, 'r') as json_reader:
            json_data = json_reader.read()
        c_data = json.loads(json_data)

        icon_id = 0

        if c_data.get("has_icon"):
            icon_path = os.path.join(character_folder,"icon.png")

            if os.path.exists(icon_path):
                key = f"character_{character}"

                if key not in CHARACTER_ICONS:
                    CHARACTER_ICONS.load(key,icon_path,'IMAGE')
                
                icon_id = CHARACTER_ICONS[key].icon_id

        c_data['icon_id'] = icon_id
        CHARACTERS[character] = c_data

class ICECUBE_AppendChar(bpy.types.Operator):
    bl_idname = "ice_cube.append_character"
    bl_label = "Appends a saved character"

    character_id: bpy.props.StringProperty()

    def execute(self, context):
        c_data = CHARACTERS.get(self.character_id)

        if not c_data:
            self.report({'ERROR'}, "Character not found")
            return {'CANCELLED'}
        
        blend_path = os.path.join(CHARACTER_STORAGE,f"{c_data['author'].lower()}-{c_data['name'].lower()}-{c_data['version'].lower()}",f"{c_data['name']}.blend")
        collection = c_data['name']

        with bpy.data.libraries.load(blend_path,link=False) as (data_from, data_to):
            if collection in data_from.collections:
                data_to.collections = [collection]
            else:
                self.report({'ERROR'}, "Character Collection not found")
                return {'CANCELLED'}
        
        for col in data_to.collections:
            if col:
                context.scene.collection.children.link(col)
        
        return {'FINISHED'}

class ICECUBERIG_CUSTOMCHAR_MT_3dview_add(bpy.types.Menu):
    bl_label = "Ice Cube"
    bl_idname = "ICECUBERIG_CUSTOMCHAR_MT_3dview_add"

    def draw(self, context):
        layout = self.layout
        
        if not CHARACTERS:
            layout.label(text="No Saved Characters")
            return
        
        for char_id, c_data in CHARACTERS.items():
            custom_op = layout.operator("ice_cube.append_character",text=c_data.get("display_name",char_id),icon_value=c_data.get("icon_id",0))
            custom_op.character_id = char_id

class ICECUBERIG_MT_3dview_add(bpy.types.Menu):
    bl_label = "Ice Cube"
    bl_idname = "ICECUBERIG_MT_3dview_add"

    def draw(self, context):
        layout = self.layout

        pcoll = ice_cube_icons_collection["ice_cube_remake"]
        
        layout.operator("ice_cube.append_ice_cube_10px",text="Append Ice Cube (10px)",icon_value=pcoll['ice_cube_logo'].icon_id)
        layout.operator("ice_cube.append_ice_cube",text="Append Ice Cube (Default)",icon_value=pcoll['ice_cube_logo'].icon_id)
        layout.operator("ice_cube.append_ice_cube_14px",text="Append Ice Cube (14px)",icon_value=pcoll['ice_cube_logo'].icon_id)
        layout.menu("ICECUBERIG_CUSTOMCHAR_MT_3dview_add",text="Saved Characters")

def AddMenuFunction(self, context):
    layout = self.layout
    pcoll = ice_cube_icons_collection["ice_cube_remake"]
    layout.menu(ICECUBERIG_MT_3dview_add.bl_idname,icon_value=pcoll['ice_cube_logo'].icon_id)


def register():
    global CHARACTER_ICONS
    CHARACTER_ICONS = bpy.utils.previews.new()
    fetchCharacters()

def unregister():
    global CHARACTER_ICONS
    bpy.utils.previews.remove(CHARACTER_ICONS)