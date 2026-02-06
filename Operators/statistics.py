import bpy, datetime,json
from bpy_extras.io_utils import ExportHelper, ImportHelper

from ..constants import INTERNAL_VERSION
from .reset_all import get_modified_settings

def GetIceCubeVersion():

    version = bpy.context.active_object.data.get("ice_cube.rig_version")

    if not version:
        return (0,0,0)
    
    return tuple(version)

class ICECUBE_StatsExport(bpy.types.Operator, ExportHelper):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = "ice_cube.statsexport"
    bl_label = "Export Statistics"

    filename_ext = ".icecubereport"

    filepath: bpy.props.StringProperty(
        name="Filepath",
        description="Where to save the Ice Cube report to",
        default="",
        subtype='FILE_PATH'
    )

    def execute(self, context):

        blender_version = ".".join([str(x) for x in bpy.app.version])
        modified_settings = get_modified_settings()

        data = {
            "Blender" : blender_version,
            "Addon Version": ".".join([str(x) for x in INTERNAL_VERSION]),
            "Ice Cube Version": ".".join([str(x) for x in GetIceCubeVersion()]),
            "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "settings": modified_settings
        }

        with open(self.filepath, 'w') as f:
            f.write(json.dumps(data,indent=4))

        return {'FINISHED'}

class ICECUBE_StatsImport(bpy.types.Operator, ImportHelper):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = "ice_cube.statsimport"
    bl_label = "Import Statistics"

    filename_ext = ".icecubereport"

    filter_glob: bpy.props.StringProperty(
        default='*.icecubereport',  # Example: filter for text and CSV files
        options={'HIDDEN'}
    )

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
    
    def execute(self,context):
        
        with open(self.filepath, 'r') as json_reader:
            json_data = json_reader.read()
        json_data = json.loads(json_data)
        
        settings = json_data['settings']

        for value in settings.keys():
            try:
                setattr(bpy.context.object,value,settings[value])
            except:
                print("Unable to set a value, it was either removed or renamed!")

        return{'FINISHED'}