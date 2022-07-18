import bpy
from ice_cube_data.properties import properties

def advanced_misc_UI(self, context, layout, obj):
    box = layout.box()
    box.label(text="Misc", icon='ACTION')
    b = box.row(align=True)
    box_sub_1 = box.box()
    box_sub_1.label(text="Settings Data", icon='SETTINGS')
    bs1 = box_sub_1.row(align=True)
    bs1.prop(obj,"prop_clipboard",text="Use Clipboard?")
    bs1.prop(obj,"ipaneltab7",text="")
    if obj.get("ipaneltab7") == 0:
        if obj.get("prop_clipboard") == False:
            bs1 = box_sub_1.row(align=True)
            bs1.prop(obj,"export_settings_filepath",text="Export Loc",icon='EXPORT')
            bs1 = box_sub_1.row(align=True)
            bs1.prop(obj,"export_settings_name",text="Filename",icon='INFO')
        bs1 = box_sub_1.row(align=True)
        if obj.get("prop_clipboard") == True:
            bs1.operator("export.settings", text="Export to Clipboard")
        else:
            bs1.operator("export.settings", text="Export to File")
    
    elif obj.get("ipaneltab7") == 1:
        if obj.get("prop_clipboard") == False:
            bs1 = box_sub_1.row(align=True)
            bs1.prop(obj,"import_settings_filepath",text="Import File",icon='EXPORT')
        bs1 = box_sub_1.row(align=True)
        if obj.get("prop_clipboard") == True:
            bs1.operator("import.settings", text="Import from Clipboard")
        else:
            bs1.operator("import.settings", text="Import from File")
    bs1 = box_sub_1.row(align=True)
    bs1.operator("reset.settings", text="Reset to Default")

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
