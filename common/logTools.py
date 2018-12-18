# -*- coding: utf-8 -*-


import logging


#设置日志等级
#logging.basicConfig(level=logging.DEBUG)

#设置日志格式
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

#设置日志时间
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"


#设置日志等级以及输出文件
logging.basicConfig(filename='/opt/log/my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)




def log(levelName, msg):
    if levelName == 'info':
        logging.info(msg)
    elif levelName == 'debug':
        logging.debug(msg)
    elif levelName == 'warning':
        logging.warning(msg)

