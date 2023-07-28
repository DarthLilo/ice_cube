#Libraries
import bpy

def parenting_UI(self, context, layout, rig_baked):
    box = layout.box()
    obj = context.object
    box.label(text="This panel has been archived.")
                
    #b = box.row(align=True)
    #b.operator("parent.head", text="Parent Head")
    #b = box.row(align=True)
    #if obj.get("Body_Bend_Half") == True:
    #    b.prop(obj, "Body_Bend_Half", text="",icon='SORT_ASC')
    #else:
    #    b.prop(obj, "Body_Bend_Half", text="",icon='SORT_DESC')
    #b.operator("parent.body", text="Parent Body")
    #if obj.get("Body_Bend_Half") == True:
    #    b.prop(obj, "Body_Bend_Half", text="",icon='SORT_ASC')
    #else:
    #    b.prop(obj, "Body_Bend_Half", text="",icon='SORT_DESC')
    #b = box.row(align=True)
#
    #if obj.get("R_A_Half") == True:
    #    b.prop(obj, "R_A_Half", text="",icon='SORT_ASC')
    #else:
    #    b.prop(obj, "R_A_Half", text="",icon='SORT_DESC')
#
    #b.operator("parent.rightarm", text="Parent Right Arm")
    #b.operator("parent.leftarm", text="Parent Left Arm")
#
    #if obj.get("L_A_Half") == True:
    #    b.prop(obj, "L_A_Half", text="",icon='SORT_ASC')
    #else:
    #    b.prop(obj, "L_A_Half", text="",icon='SORT_DESC')
#
    #b = box.row(align=True)
    #if obj.get("R_L_Half") == True:
    #    b.prop(obj, "R_L_Half", text="",icon='SORT_ASC')
    #else:
    #    b.prop(obj, "R_L_Half", text="",icon='SORT_DESC')
    #b.operator("parent.rightleg", text="Parent Right Leg")
    #b.operator("parent.leftleg", text="Parent Left Leg")
#
    #if obj.get("L_L_Half") == True:
    #    b.prop(obj, "L_L_Half", text="",icon='SORT_ASC')
    #else:
    #    b.prop(obj, "L_L_Half", text="",icon='SORT_DESC')
#
    #
    #box = layout.box()
    #box.label(text= "IMPORTANT", icon= 'HELP')
    #b = box.row(align=True)
    #b = box.row(align=True)
    #b.label(text= "To parent something to the rig with all features")
    #b = box.row(align=True)
    #b.label(text= "inherited, add the correct suffix to the end")
    #b = box.row(align=True)
    #b.label(text= "of their name then click the corresponding button.")
    #b = box.row(align=True)
    #b = box.row(align=True)
    #b.label(text= "Head Suffix: \"_HeadChild\"", icon= 'OUTLINER_OB_ARMATURE')
    #b = box.row(align=True)
    #b.label(text= "Body Suffix: \"_BodyChild\"", icon= 'OUTLINER_OB_ARMATURE')
    #b = box.row(align=True)
    #b.label(text= "Right Arm Suffix: \"_RightArmChild\"", icon= 'OUTLINER_OB_ARMATURE')
    #b = box.row(align=True)
    #b.label(text= "Left Arm Suffix: \"_LeftArmChild\"", icon= 'OUTLINER_OB_ARMATURE')
    #b = box.row(align=True)
    #b.label(text= "Right Leg Suffix: \"_RightLegChild\"", icon= 'OUTLINER_OB_ARMATURE')
    #b = box.row(align=True)
    #b.label(text= "Left Leg Suffix: \"_LeftLegChild\"", icon= 'OUTLINER_OB_ARMATURE')
    #b = box.row(align=True)
    #b = box.row(align=True)
    #b.label(text= "If you want to have a certain part ignore bends,")
    #b = box.row(align=True)
    #b.label(text="just add the \"_IgnoreBend\" after the previous")
    #b = box.row(align=True)
    #b.label(text="suffix and make sure to chose an upper or lower parent.")

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