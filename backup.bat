mkdir "C:\backupTeste"
set destiny="C:\backupTeste"
set origin="C:\Users\Rodrigo\Desktop"
echo "Iniciando Backup.."
xcopy %origin%\*.jpg %destiny%\ /s /c /y
xcopy %origin%\*.jpeg %destiny%\ /s /c /y
xcopy %origin%\*.png %destiny%\ /s /c /y
xcopy %origin%\*.gif %destiny%\ /s /c /y
xcopy %origin%\*.tiff %destiny%\ /s /c /y
xcopy %origin%\*.bmp %destiny%\ /s /c /y
xcopy %origin%\*.psd %destiny%\ /s /c /y
xcopy %origin%\*.raw %destiny%\ /s /c /y
xcopy %origin%\*.xcf %destiny%\ /s /c /y
xcopy %origin%\*.svg %destiny%\ /s /c /y
xcopy %origin%\*.ppm %destiny%\ /s /c /y
xcopy %origin%\*.pgm %destiny%\ /s /c /y
xcopy %origin%\*.pbm %destiny%\ /s /c /y
xcopy %origin%\*.pnm %destiny%\ /s /c /y
xcopy %origin%\*.cdr %destiny%\ /s /c /y
xcopy %origin%\*.txt %destiny%\ /s /c /y
xcopy %origin%\*.pdf %destiny%\ /s /c /y
xcopy %origin%\*.xps %destiny%\ /s /c /y
xcopy %origin%\*.doc %destiny%\ /s /c /y
xcopy %origin%\*.docx %destiny%\ /s /c /y
xcopy %origin%\*.ppt %destiny%\ /s /c /y
xcopy %origin%\*.pptx %destiny%\ /s /c /y
xcopy %origin%\*.xls %destiny%\ /s /c /y
xcopy %origin%\*.xlsm %destiny%\ /s /c /y
xcopy %origin%\*.xlsx %destiny%\ /s /c /y
xcopy %origin%\*.ods %destiny%\ /s /c /y
xcopy %origin%\*.odf %destiny%\ /s /c /y
xcopy %origin%\*.odt %destiny%\ /s /c /y
xcopy %origin%\*.odp %destiny%\ /s /c /y
xcopy %origin%\*.rtf %destiny%\ /s /c /y
xcopy %origin%\*.mp3 %destiny%\ /s /c /y
xcopy %origin%\*.ogg %destiny%\ /s /c /y
xcopy %origin%\*.wma %destiny%\ /s /c /y
xcopy %origin%\*.wav %destiny%\ /s /c /y
xcopy %origin%\*.aac %destiny%\ /s /c /y
xcopy %origin%\*.avi %destiny%\ /s /c /y
xcopy %origin%\*.mp4 %destiny%\ /s /c /y
xcopy %origin%\*.wmv %destiny%\ /s /c /y
xcopy %origin%\*.3gp %destiny%\ /s /c /y
xcopy %origin%\*.mkv %destiny%\ /s /c /y
xcopy %origin%\*.srt %destiny%\ /s /c /y
xcopy %origin%\*.py %destiny%\ /s /c /y
xcopy %origin%\*.c %destiny%\ /s /c /y
xcopy %origin%\*.cpp %destiny%\ /s /c /y
xcopy %origin%\*.java %destiny%\ /s /c /y
xcopy %origin%\*.js %destiny%\ /s /c /y
xcopy %origin%\*.html %destiny%\ /s /c /y
xcopy %origin%\*.css %destiny%\ /s /c /y
echo "Fim do Backup."
cmd