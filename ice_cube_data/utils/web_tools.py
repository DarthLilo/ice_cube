import webbrowser
import bpy
import urllib.request

def CustomLink(url = ""): #Opens a URL in the default browser of the user
    http = ["http://"]
    https = ["https://"]

    http_str = "http://"
    https_str = "https://"

    blnk_str = ""
    fixed_url = (blnk_str.join(url))
    if any(x in url for x in http):
        url = (fixed_url.split(http_str)[1])

    elif any(x in url for x in https):
        url = (fixed_url.split(https_str)[1])

    elif():
        url = url
    
    
    webbrowser.open_new(http_str + url)



def ICDownloadImage(url, filepath, filename):

    full_path = filepath + filename + '.png'
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url, full_path)
    

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