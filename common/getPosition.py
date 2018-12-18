# -*- coding: utf-8 -*-
"""
根据图片取得文字坐标
"""

import os
from common import logTools 


def recognition_img_txt(imgName):
    """
    将图片中文件识别出来

    """
    if os.path.isfile(imgName):
        os.system('/usr/local/bin/tesseract {} out -l chi_sim makebox'.format(imgName))
        logTools.log('info', "输出坐标文件 out.box")
    else:
        logTools.log('info', "screen.png not found")


def get_position(str, imgName):
    """
    根据文字获取需要点击坐标 
    """
    recognition_img_txt(imgName)
    list = []
    if os.path.isfile('out.box'):
        with open('out.box') as f:
            for line in f:
                if line.split()[0] in str:
                    list.append(line.split())
    return list

def get_position_only_str(str):
    list = []
    if os.path.isfile('out.box'):
        with open('out.box') as f:
            for line in f:
                if line.split()[0] in str:
                    list.append(line.split())
    return list

