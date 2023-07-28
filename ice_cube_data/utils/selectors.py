import bpy

def partOfRig(obj): #replace this stupid shit later
    
    return False

def isRigSelected(context): #checks if the rig is selected
    return bpy.context.active_object.parent if partOfRig(bpy.context.active_object) else bpy.context.active_object

def main_face(rig): #locates the ice cube mesh
    try:
        for obj in rig.children:
            try:
                if obj.data['materials'] == 1:
                    return obj
            except:
                pass
    except (AttributeError, KeyError, TypeError):
        return False

def mat_holder_func(rig): #locates the ice cube mesh
    try:
        for obj in rig.children:
            try:
                if obj.data['material_holder'] == 1:
                    return obj
            except:
                pass
    except (AttributeError, KeyError, TypeError):
        return False
    
def eye_mesh(rig): #locates the ice cube mesh
    try:
        for obj in rig.children:
            try:
                if obj.data['ice_cube_eye_mesh'] == 1:
                    return obj
            except:
                pass
    except (AttributeError, KeyError, TypeError):
        return False

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