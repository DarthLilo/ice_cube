import bpy

def CustomErrorBox(message = "", title = "Custom Error Box", icon = 'INFO'): #Draws a custom popup error

    def draw(self, context):
        lines = message.split("\n")

        for l in lines:
            self.layout.label(text=l)
    
    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)

classes = [
           ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__=="__main__":
    register()