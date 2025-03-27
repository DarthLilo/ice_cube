import bpy, json
from urllib import request
import traceback

from ..constants import INTERNAL_VERSION, GITHUB_URL

class ICECUBE_CheckForUpdates(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.check_for_updates'
    bl_label = "Check for Ice Cube Updates"

    def execute(self, context):
        github_request_vers = None

        try:
            github_request = json.loads(request.urlopen(GITHUB_URL).read().decode())
            github_request_vers = github_request['tag_name']
        except:
            traceback.format_exc()
            self.CustomPopupWindow("Error when checking for updates! :(")
            pass
        
        if self.format_version(INTERNAL_VERSION) < self.format_version(github_request_vers):
            self.CustomPopupWindow(f"There are updates available! {github_request_vers} > {INTERNAL_VERSION}\n Download them from the Ice Cube website!", "Ice Cube Updater")
        else:
            self.CustomPopupWindow("You are up to date, no new updates!", "Ice Cube Updater")

        
        return {'FINISHED'}
    
    def format_version(self, version):
        return tuple(map(int,str(version).split(".")))
    
    def CustomPopupWindow(_, message = "", title = "Custom Popup Window", icon = 'INFO'): #Draws a custom popup error
        print(message)
        def draw(self, context):
            lines = message.split("\n")

            for l in lines:
                self.layout.label(text=l)

        bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)