import os
import re
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import pandas as pd
import numpy as np
import time
import tpzwz
import pd
from dingtalkchatbot.chatbot import DingtalkChatbot
import main
import logging.handlers

scheduler = BlockingScheduler()
# logging初始化工作
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s|%(levelname)s|%(pathname)s|%(lineno)s|%(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S %a')
logger = logging.getLogger('script')
logger.setLevel(logging.INFO)
# 添加TimedRotatingFileHandler
timefilehandler = logging.handlers.TimedRotatingFileHandler(
    "test.log",  # 日志路径
    when='D',  # S秒 M分 H时 D天 W周 按时间切割 测试选用S
    interval=1,  # 多少天切割一次
    backupCount=7  # 保留多少天
)
# 设置后缀名称，跟strftime的格式一样
timefilehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(pathname)s|%(lineno)s|%(message)s')
timefilehandler.setFormatter(formatter)
logger.addHandler(timefilehandler)



def power():
    a = os.popen("adb shell dumpsys power")
    x = a.read()
    print("打开电源返回值：", x)
    isllcx = bool(re.search('state=ON', x))
    return isllcx


def job_func():
    print("job1当前时间1：", datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f"))
    time.sleep(124)
    print("job1当前时间1睡眠2分钟：", datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f"))
def job_2():
    print("job2当前时间22：", datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f"))
if __name__ == '__main__':
    scheduler.add_job(job_func, 'interval', minutes=1, start_date='2021-05-27 14:00:00', end_date='2021-05-27 17:00:00')
    scheduler.add_job(job_2, 'interval', minutes=1, start_date='2021-05-27 14:00:00', end_date='2021-05-27 17:00:00')
    scheduler.start()
