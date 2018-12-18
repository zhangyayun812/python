# -*- coding: utf-8 -*-
"""
调取配置文件和屏幕分辨率的代码
"""

from aip import AipOcr
import json

""" 你的 APPID AK SK """
APP_ID = '11673987'
API_KEY = 'E6pGl9GgBvIa4OXK5LozNAZ4'
SECRET_KEY = 'A3xTg7x8Djv4pKS75nKVZeGjSoD4zdBi'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_position(file, queryStr):
    list = []
    image = get_file_content(file)
    """ 调用通用文字识别（含位置信息版）, 图片参数为本地图片 """
    result_ocr = client.general(image)['words_result']
    """ 将结果返回 """
    for j in range(len(result_ocr)):
        result_ocr_temp = result_ocr[j]
        if queryStr in result_ocr_temp['words']: 
            list.append(result_ocr_temp['location']['width']/2 + result_ocr_temp['location']['left'])
            list.append(result_ocr_temp['location']['height']/2 + result_ocr_temp['location']['top'])
    return list 

