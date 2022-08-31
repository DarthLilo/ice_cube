#Libraries
import bpy

from ice_cube import bl_info
from ice_cube_data.utils.general_func import BlenderVersConvert


def credits_ui_panel(self, context):
    obj = context.object
    layout = self.layout
    box = layout.box()
    b = box.row(align=True)
    version_text = f"Ice Cube {BlenderVersConvert(bl_info['version'], has_v=True)}"
    b.label(text= version_text, icon= 'OUTLINER_OB_ARMATURE')
    credit_labels = {
          "Created by DarthLilo": "lilocredits.link",
          "Got a problem with the rig?": "discordserver.link",
          "Want to add your own DLC?": "custom_presets.open",
          "Need help with something?": "wiki.open"
       }
    for label in credit_labels:
        b = box.row(align = True)
        b.label(text = label)
        b.operator(credit_labels[label])