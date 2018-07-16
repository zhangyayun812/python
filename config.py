# -*- coding: utf-8 -*-
"""
读取配置文件和屏幕分辨率
"""

import os
import sys
import json
import re
from common import logTools

def open_accordant_config():
    """
    调用配置文件
    """
    screen_size = _get_screen_size()
    config_file = "{path}/config/{screen_size}/config.json".format(
        path = sys.path[0],
        screen_size = screen_size
    )
    #sys.path[0] 是程序所在的目录
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            logTools.log('info', "Load config file from {}".format(config_file))
            #format对前面定义的｛｝进行赋值
            return json.load(f)
    else:
        with open('{}/config/default.json'.format(sys.path[0]), 'r') as f:
            logTools.log('info', "Load default config")
            return json.load(f)

def _get_screen_size():
    """
    获取手机屏幕大小
    """
    size_str = os.popen('adb shell wm size').read()
    if not size_str:
        logTools.log('info','请安装 ADB 及驱动并配置环境变量')
        sys.exit()
    m = re.search(r'(\d+)x(\d+)', size_str)
    #match()函数只检测RE是不是在string的开始位置匹配,search()会扫描整个string查找匹配,会扫描整个字符串并返回第一个成功的匹配,也就是说match（）只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回none
    if m:
        return "{height}x{width}".format(height=m.group(2), width=m.group(1))
        #group(1)列出search时第一个括号匹配部分,group(2)列出search时第二个括号匹配部分
    return "1920x1080"

