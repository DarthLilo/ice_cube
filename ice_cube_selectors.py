import bpy

def GetMaterialHolder(rig):
    try:
        for obj in rig.children:
            try:
                if obj.data['ice_cube_material_holder']:
                    return obj
            except: continue
    except (AttributeError, KeyError, TypeError):
        return None

def GetMaterial(context, mat_id):
        
        materials = GetMaterialHolder(context.object).data.materials
        for mat in materials:
            try:
                if mat['ice_cube_material'] == mat_id:
                    return mat
            except:
                continue

def GetBone(rig, bone_id):
    bones = rig.pose.bones
    try:
        return bones[bone_id]
    except:
        for bone in bones:
            if 'ice_cube_bone_id' in bone and bone['ice_cube_bone_id'] == bone_id:
                return bone

def GetBoneCollection(collections, target):
        for collection in collections:
            try:
                if collection['ice_cube_layer_id'] == target:
                    return collection
            except:
                pass

def GetCollection(collections, target):
    for collection in collections:
        try:
            if collection['ice_cube_collection_id'] == target:
                return collection
        except:
            pass

def GetLattice(rig, lattice_id):
    child_objects = rig.children_recursive
    for obj in child_objects:
        if obj.type == 'LATTICE':
            if 'ice_cube.lattice_id' in obj and obj['ice_cube.lattice_id'] == lattice_id:
                return obj