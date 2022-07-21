#Libraries
import bpy

def credits_ui_panel(self, context):
    obj = context.object
    layout = self.layout
    box = layout.box()
    b = box.row(align=True)
    b.label(text= "Ice Cube v1.4.0", icon= 'OUTLINER_OB_ARMATURE')
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