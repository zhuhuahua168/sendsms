from appium import webdriver
import time
import os


def start():
    desired_caps = {'platformName': 'Android', 'platformVersion': '10', 'deviceName': '5b84214e',
                    'unicodeKeyboard': True,
                    "resetKeyboard": True, 'appPackage': 'com.jsmcc',
                    'appActivity': 'com.jsmcc.ui.WelcomeActivity', 'noReset': "True"}

    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
    time.sleep(15)
    # driver.tap([(739, 1459)], 500)

    print("点击我的")
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.RadioGroup/android.widget.RadioButton[5]").click()
    # ele = dr.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout[5]/android.widget.ImageView").click()
    time.sleep(5)
    print("点击登录")
    driver.find_element_by_id("com.jsmcc:id/tv_mine_header_login_large").click()
    time.sleep(5)
    print("输入手机号")
    driver.find_element_by_id("com.jsmcc:id/index_mobile").send_keys('15051858587')
    time.sleep(5)
    print("下一步")
    # driver.tap([(355, 635)], 500)
    driver.tap([(535, 871)])
    time.sleep(5)
    print("点击短信验证码登录")
    driver.find_element_by_id("com.jsmcc:id/sms_login").click()
    time.sleep(3)
    print("点击获取短信验证码")
    # driver.tap([(330, 575)], 500)
    driver.tap([(529, 791)])
    time.sleep(7)
    # print("退出掌上营业厅到后台")
    # driver.press_keycode(3)
    print("点击复制短信验证码")
    driver.tap([(925, 225)])
    clipboard_text = driver.get_clipboard_text()
    print(clipboard_text)
    a0 = str(int(clipboard_text[0]) + 7)
    a1 = str(int(clipboard_text[1]) + 7)
    a2 = str(int(clipboard_text[2]) + 7)
    a3 = str(int(clipboard_text[3]) + 7)
    a4 = str(int(clipboard_text[4]) + 7)
    a5 = str(int(clipboard_text[5]) + 7)
    time.sleep(1)
    driver.tap([(273, 861)])
    print("a0:", a0, "a1:", a1, "a2:", a2, "a3:", a3, "a4:", a4, "a5:", a5)
    # 输入验证码
    os.popen("adb shell input keyevent " + a0 + " " + a1 + " " + a2 + " " + a3 + " " + a4 + " " + a5)
    # driver.press_keycode(a0)
    # driver.press_keycode(a1)
    # driver.press_keycode(a2)
    # driver.press_keycode(a3)
    # driver.press_keycode(a4)
    # driver.press_keycode(a5)

    # print("切换短信")
    # #driver.start_activity("com.android.mms", "com.android.mms.ui.MmsTabActivity")
    # driver.tap([(406, 2107)])
    # time.sleep(3)
    # print("点击验证码短信")
    # driver.find_element_by_xpath('//android.widget.TextView[@text="验证码"]').click()
    # time.sleep(3)
    # print("获取第一条验证码的复制按钮")
    # xpath = driver.find_element_by_xpath(
    #     '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]')
    # code = xpath.text
    # print('验证码：' + code)
    # time.sleep(3)
    # print('退出短信到后台')
    # driver.press_keycode(3)
    time.sleep(1)
    # print("手动点击掌上移动app")
    # driver.tap([(658, 1438)])
    # driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="掌上营业厅"]').click()
    time.sleep(2)
    # print("输入短信验证码")
    # driver.find_element_by_id("com.jsmcc:id/duanxin_pwd").send_keys(clipboard_text)
    # time.sleep(3)
    print("点击登录")
    driver.find_element_by_id("com.jsmcc:id/index_login_btn").click()
    # time.sleep(3)

    # print("再次点击登录")
    # driver.find_element_by_id("com.jsmcc:id/index_login_btn").click()
    # 925 225
    # time.sleep(3)
    # print("交费历史")
    # driver.find_element_by_xpath(
    #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[9]/android.view.ViewGroup/android.widget.ImageView").click()
    # time.sleep(2)
    # driver.back()
    # time.sleep(2)
    # print("话费余额")
    # driver.find_element_by_xpath(
    #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[6]/android.view.ViewGroup/android.widget.ImageView").click()
    # time.sleep(2)
    # driver.back()
    # time.sleep(2)
    # print("账单查询")
    # driver.find_element_by_xpath(
    #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[3]/android.view.ViewGroup").click()
    # time.sleep(2)
    # driver.back()
    # time.sleep(2)
    # print("已订业务")
    # driver.find_element_by_xpath(
    #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[4]/android.view.ViewGroup").click()
    # time.sleep(2)
    # driver.back()
    # time.sleep(2)
    # print("详细查询")
    # driver.find_element_by_xpath(
    #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[7]/android.view.ViewGroup").click()
    # time.sleep(2)
    # print("查询详单输入手机号")
    # driver.find_element_by_id("com.greenpoint.android.mc10086.activity:id/user_password_edt").send_keys("18251810456")
    # time.sleep(2)
    # print("查询详单输入密码")
    # driver.find_element_by_id("com.greenpoint.android.mc10086.activity:id/user_password_edt").send_keys("472083")
    # time.sleep(2)
    # print("查询详单点击获取验证码")
    # driver.find_element_by_id("com.greenpoint.android.mc10086.activity:id/login_checksms_btn").click()
    # time.sleep(20)
    # print("查询详单点击验证码提示")
    # driver.find_element_by_id("com.miui.contentcatcher:id/user_suggestion_item").click()
    # time.sleep(2)
    # print("查询详单点击查看并同意")
    # driver.find_element_by_id(
    #     "com.greenpoint.android.mc10086.activity:id/text_read").click()
    # time.sleep(2)
    # print("查询详单点击认证")
    # driver.find_element_by_id(
    #     "com.greenpoint.android.mc10086.activity:id/one_key_login_btn").click()
    # time.sleep(2)
    # driver.back()

    # el1 = dr.find_element_by_id("com.android.mms:id/recipient_rows")
    # tc = dr.find_element_by_id("cn.phzdp:id/et_input_phone").send_keys("150518585
    time.sleep(5)
    print("quit")
    driver.quit()


if __name__ == '__main__':
    start()
