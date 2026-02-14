import bpy

class ICECUBE_Blender5_0_Fix(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.blender_5_0_fix'
    bl_label = "Attempts to convert a rig to work on Blender 5.0"

    def execute(self, context):

        for shape_key in bpy.data.shape_keys:
            self.fix_driver_def(shape_key)

        for material in bpy.data.materials:
            if material.node_tree:
                self.fix_driver_def(material.node_tree)

        for armature in bpy.data.armatures:
            self.fix_driver_def(armature)

        for obj in bpy.context.scene.objects:
            self.fix_driver_def(obj)

            if obj.name.__contains__("Arm Bend Fix lat") or obj.name.__contains__("Leg Bend Fix lat"):
                key = obj.data.shape_keys
                if key.animation_data and key.animation_data.drivers:
                    for driver_fcurve in key.animation_data.drivers:
                        if obj.name.__contains__("Right") and not obj.name.__contains__("Leg"):
                            driver_fcurve.driver.expression = "tan(var/2)*(1-bend_smoothness if bend_smoothness <= 0 else 1)"
                        else:
                            driver_fcurve.driver.expression = "-tan(var/2)*(1-bend_smoothness if bend_smoothness <= 0 else 1)"
                            
                        for driver_variable in driver_fcurve.driver.variables:

                            # Fix bend smoothness variable
                            if driver_variable.name == "point":
                                for driver_target in driver_variable.targets:
                                    driver_target.data_path = "bend_smoothness"
                                driver_variable.name = "bend_smoothness"
        
        context.object.data["ice_cube.converted_to_5_0"] = True
        
        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self,title="Attempt to convert the rig to work on Blender 5.0, make sure you ONLY have the rig in the scene!",confirm_text="Convert")
        
    def fix_driver_def(self, source):
        if source.animation_data and source.animation_data.drivers:
            for driver_fcurve in source.animation_data.drivers:
                for driver_variable in driver_fcurve.driver.variables:
                    for driver_target in driver_variable.targets:
                        if str(driver_target.data_path).startswith("[\"") and str(driver_target.data_path).endswith("\"]"):
                            driver_target.data_path = driver_target.data_path[2:-2]