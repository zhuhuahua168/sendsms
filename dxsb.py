# coding:utf-8
from appium import webdriver
import re
import time
import os
import logging
import datetime
from dingtalkchatbot.chatbot import DingtalkChatbot
import logging.handlers
'''适配小米9手机'''
# logging.basicConfig(level=logging.INFO,
#                     format="%(asctime)s %(name)s %(levelname)s %(message)s",
#                     datefmt='%Y-%m-%d  %H:%M:%S %a'  # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
#                     )

# logging初始化工作
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s|%(levelname)s|%(pathname)s|%(lineno)s|%(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S %a')
logger = logging.getLogger('check')
logger.setLevel(logging.INFO)
# 添加TimedRotatingFileHandler
timefilehandler = logging.handlers.TimedRotatingFileHandler(
    "check.log",  # 日志路径
    when='D',  # S秒 M分 H时 D天 W周 按时间切割 测试选用S
    interval=1,  # 多少天切割一次
    backupCount=7  # 保留多少天
)
# 设置后缀名称，跟strftime的格式一样
timefilehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(pathname)s|%(lineno)s|%(message)s')
timefilehandler.setFormatter(formatter)
logger.addHandler(timefilehandler)



def senddd(mgs):
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=7b342692e50a261ab203f66f400e857b401ea8cd358443872366fb4d84f8e586'
    xiaoding = DingtalkChatbot(webhook)
    xiaoding.send_text(str(mgs))


class driver_configure():
    def get_driver(self):
        '''获取driver'''
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'  # 平台
        self.desired_caps['platformVersion'] = '10.0'  # 系统版本
        self.desired_caps['appPackage'] = 'com.android.mms'  # APK包名
        self.desired_caps['appActivity'] = '.ui.MmsTabActivity'  # 被测程序启动时的Activity
        # self.desired_caps['unicodeKeyboard'] = 'true'  # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
        self.desired_caps['resetKeyboard'] = 'true'  # 是否在测试结束后将键盘重轩为系统默认的输入法。
        # self.desired_caps['60'] # Appium服务器待appium客户端发送新消息的时间。默认为60秒
        self.desired_caps['deviceName'] = '5b84214e'  # 手机ID
        self.desired_caps['noReset'] = True  # true:不重新安装APP，false:重新安装app
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
        return self.driver

    def write(self, path, text):
        f = open(path, mode='w', encoding='utf-8')
        f.write(text)
        f.close()


def jssj():
    logger.info("解锁手机开始")
    logger.info("判断手机电源是否打开")
    a = os.popen("adb shell dumpsys power")
    x = a.read()
    ispower = bool(re.search('state=ON', x))
    if ispower:
        logger.info("电源打开")
    else:
        logger.info("电源关闭开始解锁")
        os.popen("adb shell input keyevent 26")
        time.sleep(1.5)
        # 上滑
        os.popen("adb shell input swipe 300 500 300 100")
        time.sleep(1)
        # 输入密码
        os.popen("adb shell input keyevent 15 14  8 9  9 13")
        time.sleep(3)


def poweoff():
    logger.info("关闭手机电源")
    logger.info("判断手机电源是否打开")
    a = os.popen("adb shell dumpsys power")
    x = a.read()
    ispower = bool(re.search('state=ON', x))
    if ispower:
        logger.info("电源状态为打开")
        os.popen("adb shell input keyevent 26")
    else:
        logger.info("手机电源已关闭")


def reyzm():
    starttime2 = datetime.datetime.now()
    jssj()
    dc = driver_configure()
    dr = dc.get_driver()
    logger.info("-----------短厅探测开始----------")
    logger.info("【流量查询】探测开始")
    os.popen("adb shell am start -a android.intent.action.SENDTO -d sms:{} --es sms_body {}".format(10086, "llcx"))
    # 打开短信按钮
    # ele = dr.find_element_by_id("com.android.mms:id/subject")
    # 点击移动客服按钮
    time.sleep(2)
    # ele = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/miui.view.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.widget.TextView[1]").click()
    # 点击编辑模式
    logger.info("点击编辑模式")
    time.sleep(2)
    ele = dr.find_element_by_accessibility_id("编辑模式").click()
    time.sleep(2)
    logger.info("点击发送按钮")
    ele = dr.find_element_by_id("com.android.mms:id/send_button").click()
    logger.info("等待15s接收短信")
    time.sleep(15)
    logger.info("【余额查询】探测开始")
    time.sleep(2)
    ele = dr.find_element_by_id("com.android.mms:id/embedded_text_editor").send_keys("yecx")
    # 发送短信
    time.sleep(2)
    logger.info("点击发送按钮")
    ele = dr.find_element_by_id("com.android.mms:id/send_button").click()
    time.sleep(15)
    logger.info("获取上一条流量查询短信内容")
    llxcele = dr.find_element_by_id("com.android.mms:id/message_body")
    llcx = llxcele.text
    print(llcx)
    # 获取流量查询返回时间
    hftime = llcx[(llcx.rfind('截至') + 2):(llcx.rfind('截至') + 14)]
    # 判断是否返回流量查询的短信
    isllcx = bool(re.search('流量查询', llcx))
    if isllcx:
        logger.info("上一条短信内容有流量查询关键字|流量查询短信接口探测成功")
    else:
        logger.error("上一条短信内容无流量查询关键字|流量查询短信接口探测失败")
        senddd("[" + str(datetime.datetime.now()) + "][10086流量查询短信接口探测失败]:没有收到反馈短信。")
    string_code = "".join(hftime)
    dc.write('D:/smslog.txt', string_code)
    time.sleep(5)
    logger.info("流量查询短信内容解析结束")

    logger.info("【积分查询】探测开始")
    time.sleep(2)
    ele = dr.find_element_by_id("com.android.mms:id/embedded_text_editor").send_keys("jfcx")
    # 发送短信
    time.sleep(2)
    logger.info("点击发送按钮")
    ele = dr.find_element_by_id("com.android.mms:id/send_button").click()
    logger.info("等待15s接收短信")

    time.sleep(15)
    logger.info("获取上一条余额查询短信内容")
    yecxele = dr.find_element_by_id("com.android.mms:id/message_body")
    yecx = yecxele.text
    print(yecx)
    isyecx = bool(re.search('话费查询', yecx))
    if isyecx:
        logger.info("上一条短信内容有话费查询关键字|话费查询短信接口探测成功")
    else:
        logger.error("上一条短信内容无话费查询关键字|话费查询短信接口探测失败")
        senddd("[" + str(datetime.datetime.now()) + "][10086话费查询短信接口探测失败]:没有收到反馈短信。")
    logger.info("话费查询短信内容解析结束")

    logger.info("【账单查询】探测开始")
    time.sleep(2)
    ele = dr.find_element_by_id("com.android.mms:id/embedded_text_editor").send_keys("zdcx")
    # 发送短信
    time.sleep(2)
    logger.info("点击发送按钮")
    ele = dr.find_element_by_id("com.android.mms:id/send_button").click()
    logger.info("等待15s接收短信")
    time.sleep(15)
    ele = dr.find_element_by_id("com.android.mms:id/embedded_text_editor").send_keys("zdcx")
    # 发送短信
    time.sleep(2)
    logger.info("点击发送按钮")
    ele = dr.find_element_by_id("com.android.mms:id/send_button").click()
    logger.info("等待15s接收短信")
    logger.info("获取上一条积分查询短信内容")
    jfcxele = dr.find_element_by_id("com.android.mms:id/message_body")
    jfcx = jfcxele.text
    print(jfcx)
    isjfcx = bool(re.search('积分', jfcx))
    if isjfcx:
        logger.info("上一条短信内容有【积分】关键字|积分查询短信接口探测成功")
    else:
        logger.error("上一条短信内容无【积分】关键字|积分查询短信接口探测失败")
        senddd("[" + str(datetime.datetime.now()) + "][10086积分查询短信接口探测失败]:没有收到反馈短信。")

    logger.info("【实时话费查询】探测开始")
    time.sleep(2)
    ele = dr.find_element_by_id("com.android.mms:id/embedded_text_editor").send_keys("sshfcx")
    # 发送短信
    time.sleep(2)
    logger.info("点击发送按钮")
    ele = dr.find_element_by_id("com.android.mms:id/send_button").click()
    logger.info("等待15s接收短信")
    time.sleep(15)
    logger.info("获取上一条账单短信内容")
    zdcxele = dr.find_element_by_id("com.android.mms:id/message_body")
    zdcx = zdcxele.text
    print(zdcx)
    iszdcx = bool(re.search('共消费', zdcx))
    if iszdcx:
        logger.info("上一条短信内容有【共消费】关键字|账单查询短信接口探测成功")
    else:
        logger.error("上一条短信内容无【共消费】关键字|账单查询短信接口探测失败")
        senddd("[" + str(datetime.datetime.now()) + "][10086账单查询短信接口探测失败]:没有收到反馈短信。短信内容如下:["+iszdcx+"]")

    logger.info("【实时话费查询】探测开始")
    time.sleep(2)
    ele = dr.find_element_by_id("com.android.mms:id/embedded_text_editor").send_keys("sshfcx")
    # 发送短信
    time.sleep(2)
    logger.info("点击发送按钮")
    ele = dr.find_element_by_id("com.android.mms:id/send_button").click()
    logger.info("等待15s接收短信")
    time.sleep(15)
    logger.info("获取上一条账单短信内容")
    sshfcxele = dr.find_element_by_id("com.android.mms:id/message_body")
    sshfcx = sshfcxele.text
    print(sshfcx)
    issshfcx = bool(re.search('共消费', sshfcx))
    if issshfcx:
        logger.info("上一条短信内容有【共消费】关键字|实时话费查询短信接口探测成功")
    else:
        logger.error("上一条短信内容无【共消费】关键字|实时话费查询短信接口探测失败")
        senddd("[" + str(datetime.datetime.now()) + "][10086实时话费查询短信接口探测失败]:没有收到反馈短信。")
    dr.quit()
    poweoff()
    endtime = datetime.datetime.now()
    logger.info("本次循环结束，耗时：" + str((endtime - starttime2).seconds) + "秒")


def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec


second = sleeptime(0, 6, 0)
if __name__ == '__main__':
    while 1 == 1:

        try:
            logger.info("---------短厅探测任务开始-------")
            time.sleep(second)
            reyzm()
        except:
            print("程序发生异常")
            senddd("10086探测程序发生异常，请处理")

