[![NPM version](https://badge.fury.io/js/appium.svg)](https://npmjs.org/package/appium)
[![Dependency Status](https://david-dm.org/appium/appium.svg)](https://david-dm.org/appium/appium)
[![devDependency Status](https://david-dm.org/appium/appium/dev-status.svg)](https://david-dm.org/appium/appium#info=devDependencies)

[![Monthly Downloads](https://img.shields.io/npm/dm/appium.svg)](https://npmjs.org/package/appium)

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fappium%2Fappium.svg?type=shield)](https://app.fossa.io/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fappium%2Fappium?ref=badge_shield)

发送短信探测短信接口是否正常
2种方案：
1.通过获取手机截图进行图片识别转成文字判断是否有对应短信的关键字
2.通过appium和python，获取页面元素的text，判断是否包含短信关键字
告警对接钉钉和邮件，邮件支持发送故障时的手机截图
![image](https://github.com/zhuhuahua168/sendsms/blob/master/tcjgt.png)
