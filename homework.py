from time import sleep

from appium import webdriver

cap = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "HJS0218B27006432",
    "appPackage": "com.izaodao.gps",
    "appActivity": ".activity.SplashActivity",
    "recreateChromeDriverSessions": True,
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
driver.implicitly_wait(10)
driver.find_element_by_id("com.izaodao.gps:id/jurisdiction_cradtv5").click()
try:
    driver.find_element_by_id("com.izaodao.gps:id/tv_start1").click()
except:
    pass
driver.find_element_by_accessibility_id('我的').click()
driver.find_element_by_id('com.izaodao.gps:id/tvMeUserName').click()
try:
    driver.find_element_by_id("com.izaodao.gps:id/authsdk_switch_view").click()
except:
    pass
driver.find_element_by_xpath('//android.view.View[@content-desc="密码登录"]').click()
driver.find_element_by_xpath('//android.widget.EditText[@text = "请输入您的手机/邮箱/用户名"]').send_keys('11100009001')
driver.find_element_by_xpath('//android.widget.EditText[@text = "请输入密码"]').send_keys('123456')
driver.find_element_by_xpath('//android.view.View[@content-desc="确定"]').click()
try:
    assert driver.find_element_by_xpath('//android.widget.TextView[@text = "测试号9001"]')
    print('登录成功')
except Exception:
    print('登录失败')
    raise
