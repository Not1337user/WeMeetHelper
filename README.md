# WeMeetHelper
一个腾讯会议脚本，能够自动进入和退出会议室并在期间进行桌面录制


# 如何使用脚本：

1.安装requirements.txt中的依赖(pip install -r requirements.txt)

2.将开始时间和会议号以以下格式写入schedule.txt

时间(HH:MM)

[会议号]P:[密码]（没有可不填）

PS:会议号末尾加入A自动打开摄像头；加入R开始录制直到下次激活

结束时间

L

(自动离开并停止录制)

3.打开script.py启动脚本

## 使用录制功能

请下载ffmpeg并复制到脚本目录或添加到环境变量

并将script.py中的 audio_input 改为自己的桌面音频捕获设备


## GUI
没有
