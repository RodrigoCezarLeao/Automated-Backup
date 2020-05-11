from time import time
from sys import platform
from tkinter import Tk
from tkinter.messagebox import showinfo
from os import system

        

#Global Variables (path without final \\)
originPath = "C:\\Users\\Rodrigo\\Desktop"
destinyPath = "C:\\backupTeste"

SO = platform
imagesExtensions = ["jpg", "jpeg", "png", "gif", "tiff", "bmp", "psd", "raw", "xcf", "svg", "ppm", "pgm", "pbm", "pnm", "cdr"]
documentsExtensions = ["txt", "pdf", "xps", "doc", "docx", "ppt", "pptx", "xls", "xlsm", "xlsx", "ods", "odf", "odt", "odp", "rtf"]
songsExtensions = ["mp3", "ogg", "wma", "wav", "aac"]
videosExtensions = ["avi", "mp4", "wmv", "3gp", "mkv"]
subtitlesExtensions = ["srt"]
developsExtensions = ["py", "c", "cpp", "java", "js", "html", "css"]

extensions = {
    "image": imagesExtensions,
    "document": documentsExtensions,
    "song": songsExtensions,
    "video" : videosExtensions,
    "subtitle": subtitlesExtensions,
    "develop": developsExtensions
}

"""
mode = 1 -> script python
mode = 2 -> generate cmd bash
"""
mode = 2


#Start Python Script
if mode == 1:
    root=Tk()
    root.withdraw()
    showinfo(message="Inicializando o Backup...")

    ini = time()
    #Select proper Operating System
    if 'WIN' in SO.upper():   
        system(f"mkdir {destinyPath}")

        for category in extensions:
            for ext in extensions[category]:     
                comando = f"xcopy {originPath}\\*.{ext} {destinyPath} /s /c "
                system(comando)
                

    fim = time()            
    showinfo(message=f"Fim do Backup. Tempo de Execução: {round(fim-ini, 2)} s")
    root.destroy()

#Start bat generation
elif mode == 2:
    if 'WIN' in SO.upper():
        fp = open("backup.bat", "w")
        fp.write(f"mkdir {destinyPath}\n")
        fp.write(f"echo \"Iniciando Backup..\"\n")

        for category in extensions:
            for ext in extensions[category]:     
                fp.write(f"xcopy {originPath}\\*.{ext} {destinyPath} /s /c /y\n")

        fp.write(f"echo \"Fim do Backup.\"\ncmd")        
        fp.close()
