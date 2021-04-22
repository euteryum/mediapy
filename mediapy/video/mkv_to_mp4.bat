REM --RESOURCES--
REM https://forum.videohelp.com/threads/356314-How-to-batch-convert-multiplex-any-files-with-ffmpeg
REM https://stackoverflow.com/questions/12407800/which-comment-style-should-i-use-in-batch-files
REM https://stackoverflow.com/questions/46361260/what-does-percent-sign-with-tilde-syntaxa-mean-in-command-line
REM https://stackoverflow.com/questions/2591758/batch-script-loop

REM --POTENTIAL IMPROVEMENTS--
REM "In-directory-overwrite" is preferable; currently doesn't respect video file's original directory


FOR /r %%a IN ("*.mkv") DO (
	ffmpeg -i "%%a" -vcodec copy -acodec copy "%%~na.mp4"
	DEL %%a
)
echo Finished

pause
:: exit