import pyautogui
import os
import time
from datetime import datetime
import cv2

def record(ti:int,output:str):
    # 设置捕获方法
    video_method = "gdigrab"
    audio_method = 'dshow'
    
    output_file_V = output + '.mp4'
    output_file_A = output_file_V + '.aac'
    t=str(ti)
    
    # 设置音频编码和比特率
    audio_codec = 'aac'
    audio_bitrate = '128k'

    # 设置视频编码和比特率
    video_codec = 'libx264'
    video_bitrate = '400k'

    width, height = pyautogui.size()
    resolution = str(width)+'x'+str(height)

    # 设置帧率
    frame_rate = '30'
    
    # 设置输入设备
    video_input = 'desktop'
    audio_input = "OBS-Audio" #这里改成你的桌面音频捕获设备
    
    command = 'ffmpeg -f '+ video_method + ' -framerate '+ frame_rate+' -video_size '+ resolution+' -t '+t+' -i '+video_input+ ' -c:v '+ video_codec+' -b:v '+video_bitrate+' -c:a '+ audio_codec+' -b:a '+audio_bitrate+ ' -y ' +output_file_V
    command_a = 'ffmpeg -f '+ audio_method +  ' -i audio='+'"'+audio_input+'"'+' -t '+t+' -c:a '+ audio_codec+' -b:a '+audio_bitrate+ ' -y ' +output_file_A
    print(command)
    print(command_a)
    os.system('start /min '+command)
    os.system('start /min '+command_a)
    
NULL=None

def ImgAutoClick(tempFile,whatDo, debug=False):
    while True:
        pyautogui.moveTo(1,1)
        pyautogui.screenshot('screen.png')
        time.sleep(0.5)
        gray = cv2.imread('screen.png', 0)
        img_templete = cv2.imread(tempFile, 0)
        w, h = img_templete.shape[::-1]
        res = cv2.matchTemplate(gray, img_templete, cv2.TM_SQDIFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top = min_loc[0]
        left = min_loc[1]
        top_left = min_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        if(min_val < 1000):
            pyautogui.moveTo(top+h/2, left+w/2)
            time.sleep(0.5)
            if whatDo:
                pyautogui.click(duration=0.1)
            print("Success")
            break
        else:
            print("Failed")
            time.sleep(10)
            continue
    os.remove('screen.png')
    
    return True

def CheckImg(tempFile,Click, debug=False):
    pyautogui.moveTo(1,1)
    pyautogui.screenshot('screen.png')
    time.sleep(0.5)
    gray = cv2.imread('screen.png', 0)
    img_templete = cv2.imread(tempFile, 0)
    w, h = img_templete.shape[::-1]
    res = cv2.matchTemplate(gray, img_templete, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top = min_loc[0]
    left = min_loc[1]
    x = [top, left, w, h]
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    print(min_val)
    if(min_val < 1000):
        pyautogui.moveTo(top+h/2, left+w/2)
        time.sleep(0.5)
        if Click:
            pyautogui.click(duration=0.1)
            print("Success")
        cv2.destroyAllWindows()
        os.remove("screen.png")
        return True
    else:
        print("Failed")
        os.remove("screen.png")
        time.sleep(10)
        return False

def SignIn(meeting_id, password=None):
    os.startfile("C:\Program Files (x86)\Tencent\WeMeet\wemeetapp.exe")
    time.sleep(7)
    ImgAutoClick("JoinMeeting.png",True, False)
    time.sleep(1)
    pyautogui.write(meeting_id)
    time.sleep(2)
    pyautogui . press( 'enter' )
    time.sleep(1)
    if password != None :
        if CheckImg("password2.png",False , False):
            pyautogui.write(password)
            time.sleep(1)
            ImgAutoClick("passwordJoin.png", pyautogui.click(duration=0.5), False)
            time.sleep(1)
    return True


#===============================================================================


print("请在schedule.txt中以以下格式写入时间和会议号")
print("时间(hh/mm)")
print("会议号(末尾可加入 A 打开摄像头; R 开始录制直到下次激活; L 离开会议; P:密码 会议密码)")
print(
"""
示例:
06:40
123456789
"""
)
print("读取文件...")



list_time=list()
list_meeting_number=list()
"""
while True:
    list_time.append(input("时间(HH:MM)"))
    list_meeting_number.append(input("会议号"))
    C=input("继续？Y/N")
    if C == "Y" :
        continue
    else :
        schedule=dict(zip(list_time,list_meeting_number))
        print(schedule)
        break
"""
schedule=dict(zip(list_time,list_meeting_number))



f=(open("schedule.txt" , "r",encoding='utf-8'))
list_time=list()
list_meetingnumber=list()
while True:
    time1= f.readline()
    time1= time1.strip()
    if time1 != "" :
        list_time.append(time1)
        m_id=f.readline().strip()
        list_meetingnumber.append(m_id)
    else:
        break
schedule2=dict(zip(list_time , list_meetingnumber))



schedule.update(schedule2)
print(schedule)



print("脚本启动")



while True:
    now = datetime.now().strftime('%H:%M')
    password = None #会议密码
    if schedule.__contains__(now): # sign in time 
        meeting_id = schedule[now] # meeting id
        print("激活")
        # 录制
        if "R" in meeting_id:
            meeting_id = meeting_id.replace("R", "")
            R_time_unc=datetime.strptime(list_time[list_time.index(now)+1],'%H:%M') - datetime.strptime(now,'%H:%M')
            R_time=int(R_time_unc.total_seconds())
            record(abs(R_time) , datetime.now().strftime('%Y%m%d%H%M%S'))
        # 退出
        if "L" in meeting_id:
            meeting_id = meeting_id.replace("L", "")
            time.sleep(1)
            pyautogui.hotkey ('alt', 'f4')
            time.sleep(1)
            CheckImg('leaveC.png',True ,False)
            time.sleep(55)
            continue
        # 视频
        if "A" in meeting_id:
            Cam_on = True
            meeting_id = meeting_id.replace("A", "")
        else :
            Cam_on = False
        #会议密码
        if 'P' in meeting_id:
            password = meeting_id.split('P:',1)[1]
            meeting_id = meeting_id.split('P:',1)[0]
        #进入会议
        SignIn(meeting_id, str(password))
        print("Sign In!")
        if Cam_on is True:
            time.sleep(1)
            CheckImg("cam.png" , True , False)
        time.sleep(55)
    else:
        """
        #检测签到弹窗，还没做好
        if CheckImg("check.png",True):
            time.sleep(10)
            ImgAutoClick("CheckIn.png" , True , False)
        """
        print("Standing by at ",now)
        time.sleep(59)
