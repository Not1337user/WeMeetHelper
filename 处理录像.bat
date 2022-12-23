@echo off
if exist ffmpeg.exe (
	if exist ffplay.exe (
		if exist ffprobe.exe (
			goto A
		)
	)
)
if exist %PATH%\ffmpeg.exe (
	if exist %PATH%\ffplay.exe (
		if exist %PATH%\ffprobe.exe (
				goto A
		)
	)
)
goto B
:A
for %%i in (*.mp4) do (
	ffmpeg -i %%i -i %%i.aac -c copy %%i.mkv
	del %%i
	del %%i.aac
)
pause
exit

:B
ECHO 缺少ffmpeg，无法使用
ECHO 正在前往github下载
start https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
ECHO 下载后请解压至本目录或添加到环境变量
pause
exit