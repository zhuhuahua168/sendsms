# coding:utf-8
from appium import webdriver
import dxsb
import time






class driver_configure():
    def get_driver(self):
        '''获取driver'''
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'  # 平台
        self.desired_caps['platformVersion'] = '10.0'  # 系统版本
        self.desired_caps['appPackage'] = 'com.greenpoint.android.mc10086.activity'  # APK包名
        self.desired_caps['appActivity'] = 'com.mc10086.cmcc.base.StartPageActivity'  # 被测程序启动时的Activity
        #self.desired_caps['unicodeKeyboard'] = 'true'  # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
        self.desired_caps['resetKeyboard'] = 'true'  # 是否在测试结束后将键盘重轩为系统默认的输入法。
        #self.desired_caps['60'] # Appium服务器待appium客户端发送新消息的时间。默认为60秒
        self.desired_caps['deviceName'] = '5b84214e'  # 手机ID
        self.desired_caps['noReset'] = True  # true:不重新安装APP，false:重新安装app
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
        return self.driver

    def write(self, path, text):
        f = open(path, mode='w', encoding='utf-8')
        f.write(text)
        f.close()

if __name__ == '__main__':
    dc = driver_configure()
    dr = dc.get_driver()
    time.sleep(10)
    print("点击[我的]")
    ele = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout[5]/android.widget.ImageView").click()
    #ele = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout[5]/android.widget.ImageView").click()
    time.sleep(5)
    print("点击[登录]")
    ele = dr.find_element_by_id("com.greenpoint.android.mc10086.activity:id/mine_login_btn").click()
    time.sleep(5)
    print("点击[其他移动号码登录]")
    ele = dr.find_element_by_id("com.greenpoint.android.mc10086.activity:id/sms_login_tip").click()
    time.sleep(5)
    print("输入手机号")
    ele = dr.find_element_by_id("com.greenpoint.android.mc10086.activity:id/user_phoneno_edt").send_keys('15051858587')
    time.sleep(5)
    print("点击[发送验证码]")
    ele = dr.find_element_by_id("com.greenpoint.android.mc10086.activity:id/login_checksms_btn").click()
    time.sleep(10)
    ele = dr.find_element_by_id("com.greenpoint.android.mc10086.activity:id/user_login_smspassword_edt").send_keys()
    time.sleep(5)
    print("quit")
    dr.quit()