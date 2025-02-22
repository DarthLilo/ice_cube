import bpy, imghdr, struct

def CustomPopupBox(message, title, icon='INFO'):
    def draw(self, context):
        lines = message.split("\n")

        for l in lines:
            self.layout.label(text=l)
    
    bpy.context.window_manager.popup_menu(draw,title= title,icon=icon)

def UnpackImage(img):
    if img.packed_files:
        if bpy.data.is_saved:
            return img.unpack()
        else:
            return img.unpack(method='REMOVE')

def IsOldSkinFormat(skin): #Checks if the specified skin is up to date (checks if image is 64x64 or 64x32)

    with open(skin, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(skin) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
    if height == 64:
        return False
    else:
        return True