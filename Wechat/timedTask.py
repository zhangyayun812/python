# -*- coding: utf-8 -*-
import itchat, time
import datetime

itchat.auto_login(enableCmdQR=2, hotReload=True)
#想给谁发信息，先查找到这个朋友
users = itchat.search_friends(name=u'yayun')
print(users)

userName = users[0]['UserName']
#然后给他发消息
while 1:
    time.sleep(60)
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if nowTime == "7:30:00":
        itchat.send("当前时间早上{},请注意关蚊香液".format(nowTime), toUserName = userName)
    elif nowTime == "17:30:00":
        itchat.send("当前时间下午{},请注意钥匙、U盘".format(nowTime), toUserName = userName)
    else:
        itchat.send("当前时间为{},只发给自己".format(nowTime), toUserName = 'filehelper')
	
#itchat.logout()    #强制退出登录
