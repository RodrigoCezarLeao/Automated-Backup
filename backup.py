
import time
import sys
from tkinter import Tk
from tkinter.messagebox import showinfo
import os

        

#Global Variables (path without final \\)
originPath = "C:\\Users\\Rodrigo"
destinyPath = "C:\\backupTeste\\"

SO = sys.platform
imagesExtensions = ["jpg", "jpeg", "png", "gif", "tiff", "bmp", "psd", "raw", "xcf", "svg", "ppm", "pgm", "pbm", "pnm", "cdr"]
documentsExtensions = ["txt", "pdf", "xps", "doc", "docx", "ppt", "pptx", "xls", "xlsm", "xlsx", "ods", "odf", "odt", "odp", "rtf"]
songsExtensions = ["mp3", "ogg", "wma", "wav", "aac"]
videosExtensions = ["avi", "mp4", "wmv", "3gp", "mkv"]
subtitlesExtensions = ["srt"]

extensions = {
    "image": imagesExtensions,
    "document": documentsExtensions,
    "song": songsExtensions,
    "video" : videosExtensions,
    "subtitle": subtitlesExtensions}


#Start
root=Tk()
root.withdraw()
showinfo(message="Inicializando o Backup...")

ini = time.time()
#Select proper Operating System
if 'WIN' in SO.upper():   
    os.system(f"mkdir {destinyPath}")

    for category in extensions:
        for ext in extensions[category]:     
            comando = f"xcopy {originPath}\\*.{ext} {destinyPath} /s /c"
            os.system(comando)
            

fim = time.time()            
showinfo(message=f"Fim do Backup. Tempo de Execução: {round(fim-ini, 2)} s")
root.destroy()

