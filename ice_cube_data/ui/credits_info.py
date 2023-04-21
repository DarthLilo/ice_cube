#Libraries
import bpy

from ice_cube import bl_info
from ice_cube_data.utils.general_func import BlenderVersConvert


def credits_ui_panel(self, context,icon):
    obj = context.object
    pcoll = icon["main"]
    ic_logo = pcoll["Ice_Cube"]
    layout = self.layout
    box = layout.box()
    b = box.row(align=True)
    version_text = f"Ice Cube {BlenderVersConvert(bl_info['version'], has_v=True)}"
    b.label(text= version_text, icon_value= ic_logo.icon_id)
    credit_labels = {
          "Ice Cube Homepage": "rigpage.link",
          "Discord Server": "discordserver.link",
          "Open DLC Folder": "custom_presets.open",
          "Ice Cube Wiki Page": "wiki.open"
       }
    for label in credit_labels:
        b = box.row(align = True)
        b.label(text = label)
        b.operator(credit_labels[label])