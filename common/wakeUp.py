# -*- coding: utf-8 -*-
"""
唤醒手机并进入应用APP中
"""
import time
import traceback
import os
from common import logTools 

def screenshot_prepare():
    """
    打开app 
    """
    try:
        displayPowerState = os.popen("adb shell dumpsys power | grep 'Display Power: state=' | awk -F '=' '{print $2}'").read().strip('\n')
        #print(displayPowerState)
        if displayPowerState == 'OFF':
            logTools.log('info', '唤醒屏幕')
            os.system('adb shell input keyevent 26')
        else:
            logTools.log('info', "屏幕已开启不需要唤醒")
        isStatusBarKeyguard = os.popen("adb shell dumpsys window policy|grep isStatusBarKeyguard | awk -F '=' ' {print $3}'").read().strip('\n')
        #print(isStatusBarKeyguard)
        if isStatusBarKeyguard == 'true': 
            time.sleep(2)
            logTools.log('info', "解锁屏保")
            #左右滑动才好解锁,并且延迟100ms启动
            os.system('adb shell input swipe 200 400 800 400 100')
            time.sleep(1)
            logTools.log('info', "输入密码")
            os.system('adb shell input text 95729')
        else:
            logTools.log('info', "屏幕已解锁不需要再次解锁")
        time.sleep(1)
        mFocusedActivity = os.popen("adb shell dumpsys activity | grep 'mFocusedActivity' | awk '{print $4}' | awk -F '/' '{print $1}'").read().strip('\n')
        if mFocusedActivity == 'com.eg.android.AlipayGphone':
            logTools.log('info', "APP已启动，停止APP，等待重新启动")
            os.system('adb shell am force-stop com.eg.android.AlipayGphone')
        time.sleep(1)
        logTools.log('info', "启动app")
        os.system('adb shell am start -n com.eg.android.AlipayGphone/com.eg.android.AlipayGphone.AlipayLogin activity')
    except Exception:
        logTools.log('info', "screenshot_prepare error")
        traceback.print_exc()
        exit(-1) 


def app_restart():
    os.system('adb shell am force-stop com.eg.android.AlipayGphone')
    time.sleep(3)
    logTools.log('info', "启动app")
    os.system('adb shell am start -n com.eg.android.AlipayGphone/com.eg.android.AlipayGphone.AlipayLogin activity')
