# -*- coding: utf-8 -*-
import os
import datetime
import time
import tpzwz
import pd
import sendsmfj
from dingtalkchatbot.chatbot import DingtalkChatbot
'''本脚本是通过截图识别短信内容的'''
def senddd(mgs):
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=7b342692e50a261ab203f66f400e857b401ea8cd358443872366fb4d84f8e586'
    xiaoding = DingtalkChatbot(webhook)
    xiaoding.send_text(str(mgs))


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
second = sleeptime(0, 2, 0)
if __name__ == '__main__':
    starttime = datetime.datetime.now()
    print(starttime, 'info：开始10086流量查询短信接口检测')
    te = []
    while 1 == 1:
        time.sleep(second)
        starttime2 = datetime.datetime.now()
        print(starttime2, '-----检测开始任务-----')
        time.sleep(3)
        localtime = time.localtime(time.time())
        ntime = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
        pptname = "G:\python\sendsms\jt\sendsms-" + ntime + ".png"
        print("解锁手机")
        # 打开电源
        a = os.popen("adb shell input keyevent 26")
        print("打开电源返回值：", a)
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
                ddmgs = "["+ntime+"][10086流量查询接口告警]:没有收到反馈短信,详情请查看邮件附件。"
                senddd(ddmgs)
        else:
            print("流量查询失败")
            sendsmfj.send_em(pptname, ntime)
            ddmgs = "[" + ntime + "][10086流量查询接口告警]:没有收到反馈短信,详情请查看邮件附件。"
            senddd(ddmgs)
        if len(te) > 20:
            del te[0:18]
        print("查询返回时间的列表：", te)
        with open(r"G:\python\sendsms\jt\llcx.txt", "a") as t:  # 将识别出来的文字存到本地
            t.write(str("流量查询返回时间："+fftime+"\n"))
            t.close()
        endtime = datetime.datetime.now()
        print(datetime.datetime.now(), '-----检测任务结束-----耗时：' + str((endtime - starttime2).seconds)+"秒")
