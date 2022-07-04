import serial
import numpy as np
from matplotlib import pyplot as plt
import time
import subprocess
import keyboard
import win32gui
import ctypes

win32gui.EnumWindows(lambda x, _: print(str(x)+' : '+win32gui.GetClassName(x)+' : '+win32gui.GetWindowText(x)), None)


def forground( hwnd, title):
    name = win32gui.GetWindowText(hwnd)
    if name.find(title) >= 0:

        # 最初化を戻す
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd,1) # SW_SHOWNORMAL

        ctypes.windll.user32.SetForegroundWindow(hwnd)
        return False # 列挙終了



ser = serial.Serial("COM7", 115200, timeout=0.1)
ser.readline()
before_state = 0
# ser.write("*".encode())
# data = ser.readline().strip().rsplit()
i = 0
while True:
    i = i + 1
    val_m5 = 0
    ser.write("*".encode())
    val_m5 = ser.readline()
    # val_decoded = int(repr(val_m5.decode())[1:-5])
    val_decoded = val_m5.strip().decode("utf-8")
    if val_decoded != before_state:
        if val_decoded == "0":
            print(str(i) + "ボタンON")
            win32gui.EnumWindows(forground, 'Teams')
            # subprocess.Popen(r'C:\Windows\notepad.exe')
            # keyboard.press("control")
            # keyboard.press("shift")
            keyboard.press("m")
            # keyboard.release("control")mmmmmmm
            # keyboard.release("shift")
            keyboard.release("m")

            # keyboard.press_and_release("y")
            time.sleep(2)
            # if val_decoded == "1":

        else:
            # print("ボタンOFF")
            pass
    
    else:
        pass
    before_state = val_decoded

    # time.sleep(0.01)


ser.close()
