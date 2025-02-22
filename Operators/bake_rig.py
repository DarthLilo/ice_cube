import bpy

from ..ice_cube_selectors import GetCollection

class ICECUBE_BAKE_RIG(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.bake_rig'
    bl_label = "Bake Rig"

    def execute(self, context):
        rig = context.object
        rig_collections = rig.users_collection
        collections = GetCollection(rig_collections,"ice_cube.main").children_recursive
        
        delete_collections = []
        search_collections = []

        if rig.arm_type == '1':
            delete_collections.extend(['ice_cube.alex_l','ice_cube.alex_r','ice_cube.thin_l','ice_cube.thin_r'])
            search_collections.extend(['ice_cube.steve_l','ice_cube.steve_r'])
        
        if rig.arm_type == '2':
            delete_collections.extend(['ice_cube.steve_l','ice_cube.steve_r','ice_cube.thin_l','ice_cube.thin_r'])
            search_collections.extend(['ice_cube.alex_l','ice_cube.alex_r'])
        
        if rig.arm_type == '3':
            delete_collections.extend(['ice_cube.steve_l','ice_cube.steve_r','ice_cube.alex_l','ice_cube.alex_r'])
            search_collections.extend(['ice_cube.thin_l','ice_cube.thin_r'])

        if rig.eyelashes == '1':
            delete_collections.extend(['ice_cube.eyelashes_default','ice_cube.eyelashes_andromeda','ice_cube.eyelashes_bushy'])
        elif rig.eyelashes == '2':
            delete_collections.extend(['ice_cube.eyelashes_andromeda','ice_cube.eyelashes_bushy'])
        elif rig.eyelashes == '3':
            delete_collections.extend(['ice_cube.eyelashes_default','ice_cube.eyelashes_bushy'])
        elif rig.eyelashes == '4':
            delete_collections.extend(['ice_cube.eyelashes_default','ice_cube.eyelashes_andromeda'])
        
        search_collections.extend(['ice_cube.head','ice_cube.body','ice_cube.face'])
        
        for collection in delete_collections:
            for mesh in GetCollection(collections,collection).objects:
                bpy.data.objects.remove(mesh,do_unlink=True)
        
        ModifiersToApply = ["Cosmetic Lattice","Cosmetic Lattice Finger"]

        for collection in search_collections:
            for mesh in GetCollection(collections,collection).objects:
                for modifier in ModifiersToApply:
                    self.apply_modifier(mesh,modifier)

        return {'FINISHED'}
    
    def apply_modifier(self,mesh,modifier):
        context_override = {'object':mesh}
        try:
            with bpy.context.temp_override(**context_override):
                bpy.ops.object.modifier_apply(modifier=modifier)
        except RuntimeError:
            print(f"Could not apply modifiers for {mesh.name} because it has shape keys!")
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self,title="Bake rig confirmation?",confirm_text="Bake")