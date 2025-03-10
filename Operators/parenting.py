import bpy, os

from ..ice_cube_selectors import GetCollection, GetLattice

class GeneralModFunc():
    def move_modifier(obj,mod_name, loc):
        cur_index = obj.modifiers.find(mod_name)
        while cur_index > loc:
            with bpy.context.temp_override(**{'object':obj}):
                bpy.ops.object.modifier_move_up(modifier=mod_name)
            cur_index -= 1

class UpdateParenting():
    def execute(self, context):

        rig = context.object
        rig_collections = rig.users_collection
        collections = GetCollection(rig_collections,"ice_cube.main").children_recursive

        ice_cube_collections = {
            GetCollection(collections,"ice_cube.head") : {
                "armature": {
                    "vertex_group_name":"Head",
                    "index": 0
                },
                "deform": {
                    "id": "ice_cube.head_twist",
                    "index": 1
                },
                "cosmetic": {
                    "id": "ice_cube.head_cosmetic",
                    "index": 2
                }
                },
            GetCollection(collections,"ice_cube.body") : {
                "deform": {
                    "id": "ice_cube.body_deform",
                    "index": 1
                },
                "cosmetic": {
                    "id": "ice_cube.body_cosmetic",
                    "index": 0
                }
            },
            GetCollection(collections,"ice_cube.left_arm") : {
                "deform": {
                    "id": "ice_cube.left_arm_deform",
                    "index": 1
                },
                "cosmetic": {
                    "id": "ice_cube.left_arm_cosmetic",
                    "index": 0
                }
            },
            GetCollection(collections,"ice_cube.right_arm") : {
                "deform": {
                    "id": "ice_cube.right_arm_deform",
                    "index": 1
                },
                "cosmetic": {
                    "id": "ice_cube.right_arm_cosmetic",
                    "index": 0
                }
            },
            GetCollection(collections,"ice_cube.left_leg") : {
                "deform": {
                    "id": "ice_cube.left_leg_deform",
                    "index": 1
                },
                "cosmetic": {
                    "id": "ice_cube.left_leg_cosmetic",
                    "index": 0
                }
            },
            GetCollection(collections,"ice_cube.right_leg") : {
                "deform": {
                    "id": "ice_cube.right_leg_deform",
                    "index": 1
                },
                "cosmetic": {
                    "id": "ice_cube.right_leg_cosmetic",
                    "index": 0
                }
            }
        }
        #[GetCollection(collections,"ice_cube.head"),GetCollection(collections,"ice_cube.body"),GetCollection(collections,"ice_cube.left_arm"),GetCollection(collections,"ice_cube.right_arm"),GetCollection(collections,"ice_cube.left_leg"),GetCollection(collections,"ice_cube.right_leg")]

        for collection in ice_cube_collections.keys():
            for obj in collection.all_objects:
                if 'ice_cube.parented' in obj and obj['ice_cube.parented'] == True:
                    continue
                
                lattice_data = ice_cube_collections[collection]

                if "armature" in lattice_data:
                    UpdateParenting.full_weight_paint(obj,lattice_data['armature']['vertex_group_name'])
                    UpdateParenting.add_armature_modifier(obj,rig,lattice_data['armature']['index'])
                
                UpdateParenting.add_lattice_modifier(obj,"Deform",GetLattice(rig,lattice_data['deform']['id']),lattice_data["deform"]['index'])
                UpdateParenting.add_lattice_modifier(obj,"Cosmetic",GetLattice(rig,lattice_data['cosmetic']['id']),lattice_data["cosmetic"]['index'])

                obj['ice_cube.parented'] = True
                obj.parent = rig

        return {'FINISHED'}
    
    def add_lattice_modifier(obj, name, target_lattice, index):
        lattice_mod = obj.modifiers.new(name=name, type='LATTICE')
        lattice_mod.object = target_lattice
        GeneralModFunc.move_modifier(obj,name,index)
    
    def full_weight_paint(obj, vertex_group_name):
        vertex_group = obj.vertex_groups.new(name=vertex_group_name)
        verts = []
        for vert in obj.data.vertices:
            verts.append(vert.index)
        vertex_group.add(verts, 1.0, 'ADD')
    
    def add_armature_modifier(obj, rig, index):
        modifier = obj.modifiers.new(name="Ice Cube",type='ARMATURE')
        modifier.object = rig
        GeneralModFunc.move_modifier(obj,"Ice Cube",index)

class ICECUBE_UpdateParenting(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.update_parenting'
    bl_label = "Update Parenting"

    def execute(self, context):

        UpdateParenting.execute(self,context)

        return {'FINISHED'}

class ICECUBE_ParentArmor(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.parent_armor'
    bl_label = "Parent Armor"

    def execute(self, context):
        scene = context.scene
        rig = context.object
        rig_collections = rig.users_collection
        collections = GetCollection(rig_collections,"ice_cube.main").children_recursive
        selected_collection = scene.ice_cube_remake.armor_collection_target

        if not selected_collection:
            return {'FINISHED'} #ice_cube_asset_library.parent_type
        
        objs_to_update = {}

        for obj in selected_collection.all_objects:
            if "ice_cube_asset_library.parent_type" in obj:
                
                parent_type = obj["ice_cube_asset_library.parent_type"]
                target_collection = GetCollection(collections,f"ice_cube.{parent_type}")

                objs_to_update[obj] = target_collection
        
        for obj in objs_to_update.keys():
            for c in obj.users_collection:
                c.objects.unlink(obj)
            
            objs_to_update[obj].objects.link(obj)
            obj.scale = (1.67,1.67,1.67)

        UpdateParenting.execute(self,context)

        bpy.data.collections.remove(selected_collection)
        scene.ice_cube_remake.armor_collection_target = None

        return {'FINISHED'}