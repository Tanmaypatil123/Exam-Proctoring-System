from sys import platform
import os

def scrn_res():
    if(platform == "win32"):
        from win32api import GetSystemMetrics
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
    
    if(platform == "linux" or platform == "linux2"):
        screen = os.popen("xrandr -q -d :0").readlines()[0]
        width = screen.split()[7]
        height = screen.split()[9][:-1]

    return (width,height)

print(scrn_res())