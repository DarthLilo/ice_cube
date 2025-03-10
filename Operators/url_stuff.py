import bpy, webbrowser

class ICECUBE_OPEN_WEBSITE(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.open_website'
    bl_label = "Open Ice Cube Website"

    def execute(self, context):
        webbrowser.open_new("https://ice-cube-rig.carrd.co/")
        return {'FINISHED'}

class ICECUBE_OPEN_DISCORD(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.open_discord'
    bl_label = "Open DarthLilo Discord"

    def execute(self, context):
        webbrowser.open_new("https://discord.gg/3G44QQM")
        return {'FINISHED'}

class ICECUBE_OPEN_WIKI(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.open_wiki'
    bl_label = "Open Ice Cube Wiki"

    def execute(self, context):
        webbrowser.open_new("https://darthlilo.gitbook.io/ice-cube-wiki")
        return {'FINISHED'}