# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
import time
import tpzwz
import pd
import adb_shell
import sendsmfj


def sendsms(content, mobiles):
    # 发送短信
    os.popen("adb shell am start -a android.intent.action.SENDTO -d sms:{} --es sms_body {}".format(mobiles, content))
    time.sleep(3)
    # 模拟发送
    # 导航键 向右
    os.popen("adb shell input keyevent 22")
    # print('按向右按键')
    time.sleep(2)
    # 回车键
    os.popen("adb shell input keyevent 66")
    print('按回车键')
    time.sleep(3)
    os.popen("adb shell am start -a android.intent.action.SENDTO -d sms:{} --es sms_body {}".format(mobiles, content))
    # 按键Home
    #os.popen("adb shell input keyevent 3")
    # print('按home')


def jt(ntime):
    # 截图
    pname = "sendsms-" + ntime + ".png"
    print("生成的图片名称为 :", pname)
    os.popen("adb shell screencap -p /sdcard/sendsms-" + ntime + ".png")
    print('完成截图')
    time.sleep(3)
    os.popen("adb pull /sdcard/sendsms-" + ntime + ".png G:\python\sendsms\jt")
    print('获取截图')
    #ptname = "G:\python\sendsms\jt\sendsms-" + ntime + ".png"
    # 按键Home
    time.sleep(3)
    os.popen("adb shell input keyevent 3")
    print('按home')
    # 打开电源
    time.sleep(3)
    print('关闭电源')
    os.popen("adb shell input keyevent 26")


def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec;


second = sleeptime(0, 2, 0);
if __name__ == '__main__':
    te = []
    while 1 == 1:
        time.sleep(second)
        print('-----检测开始任务-----')
        time.sleep(3)
        localtime = time.localtime(time.time())
        ntime = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
        pptname = "G:\python\sendsms\jt\sendsms-" + ntime + ".png"
        print("解锁手机")
        # 打开电源
        os.popen("adb shell input keyevent 26")
        time.sleep(1)
        # 上滑
        os.popen("adb shell input swipe 300 500 300 100")
        time.sleep(1)
        # 输入密码
        os.popen("adb shell input keyevent 15 14  8 9  9 13")
        time.sleep(3)
        sendsms("llcx", '10086')
        print("等待接收短信")
        time.sleep(6)
        jt(ntime)
        time.sleep(5)
        sms = tpzwz.sb(ntime)
        (fftime, agjz) = pd.getdata(sms, ntime)
        # 判断是否能接收到短信
        if agjz:
            print("有流量关键字")
            if fftime not in te:
                print("流量查询成功", ntime)
                te.append(fftime)
            else:
                print("上一次短信内容")
                sendsmfj.send_em(pptname, ntime)
        else:
            print("流量查询失败")
            sendsmfj.send_em(pptname, ntime)
        if len(te) > 20:
            del te[0:18]
        print("查询返回时间的列表：", te)
        print('-----检测任务结束-----')
