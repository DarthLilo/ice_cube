#Libraries
import bpy

from ice_cube import bl_info
from ice_cube_data.utils.general_func import BlenderVersConvert, getLanguageTranslation
from ice_cube_data.utils.selectors import isRigSelected

def credits_info_panel(self, context, icon):
    obj = context.object
    script_vers = BlenderVersConvert(bl_info['version'], has_v=False)
    rig = isRigSelected(context)
    rig_vers = rig.data.get("ic_version")
    pcoll = icon["main"]
    ic_logo = pcoll["Ice_Cube"]
    layout = self.layout
    box = layout.box()
    b = box.row(align=True)
    if not rig_vers == None:
        if rig_vers > script_vers:
            message = getLanguageTranslation("ice_cube.errors.outdated_addon") #"OUTDATED ADDON VERSION! PLEASE UPDATE"
        elif script_vers > rig_vers:
            message = getLanguageTranslation("ice_cube.errors.outdated_rig") #"OUTDATED RIG, THINGS MAY NOT WORK AS EXPECTED"
    else:
        message = getLanguageTranslation("ice_cube.errors.outdated_rig") #"OUTDATED RIG, THINGS MAY NOT WORK AS EXPECTED"
    
    version_text = f"{getLanguageTranslation('ice_cube.ui.main.title')} {BlenderVersConvert(bl_info['version'], has_v=True)}"
    b.label(text= version_text, icon_value= ic_logo.icon_id)
    b.prop(obj,"icecube_menu_version",text="")
    if rig_vers != script_vers:
        b = box.row(align = True)
        b.label(text=message,icon='ERROR')
    credit_labels = {
          "ice_cube.ui.credits.website": "rigpage.link",
          "ice_cube.ui.credits.discord": "discordserver.link",
          "ice_cube.ui.credits.dlc_folder": "custom_presets.open",
          "ice_cube.ui.credits.wiki": "wiki.open"
       }
    for label in credit_labels:
        b = box.row(align = True)
        b.label(text = getLanguageTranslation(label))
        b.operator(credit_labels[label])
    b = box.row(align=True)
    b.label(text=getLanguageTranslation("ice_cube.ui.credits.ui_scale"))
    b.prop(obj,"UI_Scale",text="",slider=True)