import bpy, struct, struct

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

def GetPNGDim(filepath):
    """
    Will get the hight and width of a PNG file without using IMGHDR since it was removed
    """

    with open(filepath, 'rb') as f:
        header = f.read(24)

        if len(header) < 24:
            return None
        
        if header[:8] != b'\x89PNG\r\n\x1a\n':
            print("PNG signature did not match!")
            return None
        
        if header[12:16] != b'IHDR':
            print("IHDR chunk check failed")
            return None
        
        width, height = struct.unpack(">II", header[16:24])
        return width, height


def IsOldSkinFormat(skin): #Checks if the specified skin is up to date (checks if image is 64x64 or 64x32)

    dim = GetPNGDim(skin)
    
    width, height = dim

    if height == 64:
        return False
    else:
        return True