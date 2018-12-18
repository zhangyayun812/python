# -*- coding: utf-8 -*-
"""
根据坐标点击
"""
import time
import traceback
import os
from common import logTools 

def tap_by_xy(x, y):
    try:
        logTools.log('info', "开始点击{} {}".format(x, y))
        os.system('adb shell input tap {} {}'.format(x, y))
        time.sleep(1)
    except Exception:
        logTools.log('info', "tap_by_xy error")
        traceback.print_exc()
        exit(-1) 

def swipe_by_2point(x1, y1, x2, y2):
    try:
        logTools.log('info', "开始滑动{} {} {} {} 300".format(x1, y1, x2, y2))
        os.system('adb shell input swipe {} {} {} {} 300'.format(x1, y1, x2, y2))
        time.sleep(1)
    except Exception:
        logTools.log('info', "swipe_by_2point error")
        traceback.print_exc()
        exit(-1) 



def keyevent_by_num(num):
    try:
        logTools.log('info', "开始模拟按键{}".format(num))
        os.system('adb shell input keyevent {}'.format(num))
        time.sleep(1)
    except Exception:
        logTools.log('info', "keyevent_by_num error")
        traceback.print_exc()
        exit(-1) 
