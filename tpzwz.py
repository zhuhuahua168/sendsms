# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image
import datetime


def sb(natime):
    for i in range(1, 2):
        starttime = datetime.datetime.now()
        ptname = r"G:\python\sendsms\jt\sendsms-"+natime+".png"
        print("截图文件：", ptname)
        #print(ptname)
        image = Image.open(ptname)
        text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用简体中文解析图片
        endtime = datetime.datetime.now()
        print(r"图片识别" + str(i) + r"转换完成，耗时：" + str((endtime - starttime).seconds))
        text = text.replace(" ", "")
        with open(r"G:\python\sendsms\jt\dx.txt", "a") as f:  # 将识别出来的文字存到本地
            #print(text)
            f.write(str(text))
    return text
