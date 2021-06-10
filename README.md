发送短信探测短信接口是否正常
2种方案：
1.通过获取手机截图进行图片识别转成文字判断是否有对应短信的关键字
2.通过appium和python，获取页面元素的text，判断是否包含短信关键字
告警对接钉钉和邮件，邮件支持发送故障时的手机截图
![image](https://github.com/zhuhuahua168/sendsms/blob/master/%E6%9E%B6%E6%9E%84%E5%9B%BE.png)
