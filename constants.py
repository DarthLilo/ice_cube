import bpy, os


ADDON_VERSION = "Ice Cube 2.0.9"
INTERNAL_VERSION = (2,0,9)

RIG_ID = "Ice_Cube_v2_Remake"
LOCAL_STORAGE = bpy.utils.extension_path_user(__package__, path="", create=True)
SKIN_STORAGE = os.path.join(LOCAL_STORAGE,'libraries/skins')
ADDON_PATH = os.path.dirname(os.path.abspath(__file__))
ASSETS_STORAGE = os.path.join(ADDON_PATH,"Assets")
ICONS = os.path.join(ASSETS_STORAGE,"icons")
DEFAULT_SKIN = os.path.join(ASSETS_STORAGE,"ice_cube_default.png")
ICE_CUBE_DEFAULT = os.path.join(ASSETS_STORAGE,"ice_cube.blend")
ICE_CUBE_14PX = os.path.join(ASSETS_STORAGE,"ice_cube_14px.blend")
ICE_CUBE_10PX = os.path.join(ASSETS_STORAGE,"ice_cube_10px.blend")
GITHUB_URL = "https://api.github.com/repos/DarthLilo/ice_cube/releases/latest"