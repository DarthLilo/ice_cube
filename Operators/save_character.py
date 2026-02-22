import bpy, os, json, shutil

from ..constants import CHARACTER_STORAGE
from ..Panels.add_menu import fetchCharacters

class ICECUBE_SaveCharacter(bpy.types.Operator):
    bl_idname = "ice_cube.save_character"
    bl_label = "Save Character (Ice Cube)"
    bl_options = {'REGISTER'}
    
    def collection_items(self, context):
        items = []

        for col in bpy.data.collections:
            if col.name == "Scene Collection":
                continue

            if not "ice_cube_collection_id" in col:
                continue
            else:
                if not col['ice_cube_collection_id'] == "ice_cube.main":
                    continue

            items.append((col.name, col.name, ""))

        if not items:
            items.append(("NONE", "No Collections Found", ""))

        return items
    
    def default_collection(seelf, context):
        scene = context.scene
        children = scene.collection.children

        if not children:
            return "NONE"
        
        highest_col = max(children, key=lambda c: len(c.all_objects))
        return highest_col.name
    
    author: bpy.props.StringProperty(name="Author")
    version: bpy.props.StringProperty(name="Version", default="1")
    display_name: bpy.props.StringProperty(name="Display Name")

    collection: bpy.props.EnumProperty(
        name="Collection",
        items=collection_items,
        description="The collection that will be imported upon adding the character"
    )

    has_icon: bpy.props.BoolProperty(name="Include Icon", default=False)

    icon_path: bpy.props.StringProperty(
        name="Icon Path",
        subtype='FILE_PATH'
    )


    def draw(self, context):
        layout = self.layout

        layout.prop(self, "author")
        layout.prop(self, "collection")
        layout.prop(self, "version")
        layout.prop(self, "display_name")
        layout.prop(self, "has_icon")

        if self.has_icon:
            layout.prop(self, "icon_path")
    
    def execute(self, context):
        name = self.collection

        if name == "NONE":
            self.report({'ERROR'}, "No collections available")
            return {'CANCELLED'}
        
        if not self.author or not self.version:
            self.report({'ERROR'},"Author and Version are required!")
            return {'CANCELLED'}
        
        folder_name = f"{self.author.lower()}-{name.lower()}-{self.version.lower()}"
        char_folder = os.path.join(CHARACTER_STORAGE, folder_name)
        os.makedirs(char_folder,exist_ok=True)

        json_data = {
            "author": self.author,
            "name": name,
            "version": self.version,
            "display_name": self.display_name or f"{name} v{self.version}",
            "has_icon": self.has_icon
        }

        json_path = os.path.join(char_folder,"character.json")
        with open(json_path, "w") as f:
            json.dump(json_data, f, indent=4)
        
        blend_path = os.path.join(char_folder,f"{name}.blend")
        bpy.ops.wm.save_as_mainfile(
            filepath=blend_path,
            copy=True
        )

        if self.has_icon and self.icon_path and os.path.exists(self.icon_path):
            icon_dest = os.path.join(char_folder, "icon.png")
            shutil.copyfile(self.icon_path, icon_dest)
        
        self.report({'INFO'}, "Character Saved")
        fetchCharacters()
        return {'FINISHED'}
        

    def invoke(self, context, event):
        if not context.scene.collection.children:
            self.report({'ERROR'}, "No collections in scene")
            return {'CANCELLED'}

        self.collection = self.default_collection(context)
        return context.window_manager.invoke_props_dialog(self, width=400)