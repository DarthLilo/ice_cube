import bpy, os, subprocess
from sys import platform

class ICECUBE_OpenFolder(bpy.types.Operator):
    bl_idname = "ice_cube.open_folder"
    bl_label = "Opens a specified folder"

    folder_path: bpy.props.StringProperty()

    def execute(self, context):

        if not os.path.exists(os.path.normpath(self.folder_path)):
            print(f"Failed to open folder [{self.folder_path}]")
            self.report({'ERROR'},"Folder path not found!")
            return {'CANCELLED'}

        try:
            if platform == "win32":
                subprocess.Popen(fr'explorer "{self.folder_path}"')
            elif platform == "darwin":
                subprocess.call(["open", "-R", self.folder_path])
            else:
                subprocess.Popen(["xdg-open", self.folder_path])
        except Exception as e:
            print(f"Error when openeing folder \n{e}")
            self.report({'ERROR'}, "Error when opening folder, see console for details!")

        return {'FINISHED'}