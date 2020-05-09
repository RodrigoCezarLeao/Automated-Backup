import os
import sys
from tkinter import Tk
from tkinter.messagebox import showinfo


#Windows functions
def createDirectories():
    for fileCategory in extensions:
        os.system(f"mkdir {destinyPath}\\{fileCategory}")
        for extension in extensions[fileCategory]:
            os.system(f"mkdir {destinyPath}\\{fileCategory}\\{extension}")

def isProperFile(path):
    for fileCategory in extensions:
        for extension in extensions[fileCategory]:
            if extension.upper() in path[-4:].upper():
                return True

    return False

def properDestinyPath(abspath):    
    ext = abspath[-4:].replace(".", "")
    ext = ext.replace("\\", "")

                      
    for fileCategory in extensions:
        for extension in extensions[fileCategory]:
            if ext.upper() == extension.upper():
                return f"{destinyPath}\{fileCategory}\{extension}\\"

    
    
        


#Global Variables (path without final \\
originPath = "C:\\Users\\Rodrigo"
destinyPath = "C:\\backupTeste\\"

SO = sys.platform
imagesExtensions = ["jpg", "jpeg", "png", "gif", "tiff", "bmp", "psd", "raw", "xcf", "svg", "ppm", "pgm", "pbm", "pnm", "cdr"]
documentsExtensions = ["txt", "pdf", "xps", "doc", "docx", "ppt", "pptx", "xls", "xlsm", "xlsx", "ods", "odf", "odt", "odp"]
songsExtensions = ["mp3", "ogg", "wma", "wav", "aac"]
videosExtensions = ["avi", "mp4", "wmv", "3gp", "mkv"]
subtitlesExtensions = ["srt"]

extensions = {
    "image": imagesExtensions,
    "document": documentsExtensions,
    "song": songsExtensions,
    "video" : videosExtensions,
    "subtitle": subtitlesExtensions}

root=Tk()
root.withdraw()

showinfo(message="Inicializando o Backup...")
#Select proper Operating System
if 'WIN' in SO.upper():   
    os.system(f"mkdir {destinyPath}")
    #createDirectories()

    for category in extensions:
        for ext in extensions[category]:     
            comando = f"xcopy {originPath}\\*.{ext} {destinyPath} /s /c"
            os.system(comando)
            
            
input("Pressione uma tecla")
showinfo(message="Fim do Backup.")
root.destroy()

