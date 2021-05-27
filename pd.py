# -*- coding: utf-8 -*-
import re
def wirte_dx(tx):
    with open(r"G:\python\sendsms\jt\cx.txt", "a") as t:  # 将识别出来的文字存到本地
        t.write(str(tx))
def readfile():
    file = open(r"G:\python\sendsms\jt\cx.txt")
    lines = file.readlines()
    aa = []
    for line in lines:
        temp = line.replace('"', '').split('\n')
        aa.append(temp)
    return aa
def getdata(text,tm):
    te = []
    ptname = "G:\python\sendsms\jt\sendsms-" + tm + ".png"
    fhtime = text[(text.rfind('截至')+2):(text.rfind('截至')+14)]
    print("流量查询截止时间：",fhtime)
    gjz = bool(re.search('流量查询', text))
    return fhtime, gjz
