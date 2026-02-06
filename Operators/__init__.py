import bpy

from . import skin_downloader
from . import ik_snapping
from . import custom_default
from . import bake_rig
from . import append
from . import dev
from . import parenting
from . import url_stuff
from . import reset_all
from . import update_checker
from . import statistics
from . import blender_5_0_fix

classes = (
    skin_downloader.ICECUBE_DOWNLOAD_SKIN,
    skin_downloader.ICECUBE_APPLY_SKIN,
    skin_downloader.ICECUBE_DELETE_SKIN,
    skin_downloader.ICECUBE_RESET_SKIN,
    ik_snapping.ICECUBE_Convert_IK_TO_FK_LEG_L,
    ik_snapping.ICECUBE_Convert_FK_TO_IK_LEG_L,
    ik_snapping.ICECUBE_Convert_IK_TO_FK_LEG_R,
    ik_snapping.ICECUBE_Convert_FK_TO_IK_LEG_R,
    ik_snapping.ICECUBE_Convert_FK_TO_IK_ARM_L,
    ik_snapping.ICECUBE_Convert_IK_TO_FK_ARM_L,
    ik_snapping.ICECUBE_Convert_FK_TO_IK_ARM_R,
    ik_snapping.ICECUBE_Convert_IK_TO_FK_ARM_R,
    custom_default.ICECUBE_SET_CUSTOM_DEFAULT,
    custom_default.ICECUBE_RESET_CUSTOM_DEFAULT,
    bake_rig.ICECUBE_BAKE_RIG,
    append.ICECUBE_AppendIceCube,
    append.ICECUBE_AppendIceCube10PX,
    append.ICECUBE_AppendIceCube14PX,
    dev.ICECUBE_DEVupdateIceCube,
    dev.ICECUBE_DEVupdateIceCube14px,
    dev.ICECUBE_DEVupdateIceCube10px,
    parenting.ICECUBE_UpdateParenting,
    parenting.ICECUBE_ParentArmor,
    url_stuff.ICECUBE_OPEN_WEBSITE,
    url_stuff.ICECUBE_OPEN_DISCORD,
    url_stuff.ICECUBE_OPEN_WIKI,
    reset_all.ICECUBE_Reset,
    update_checker.ICECUBE_CheckForUpdates,
    statistics.ICECUBE_StatsExport,
    statistics.ICECUBE_StatsImport,
    blender_5_0_fix.ICECUBE_Blender5_0_Fix
)

register, unregister = bpy.utils.register_classes_factory(classes)