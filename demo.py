from time import sleep
from appium import webdriver
cap = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "HJS0218B27006432",
    "appPackage": "com.android.settings",
    "appActivity": ".HWSettings",
    "recreateChromeDriverSessions": True,
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)

# 文本框案例
# el_search = driver.find_element_by_id('android:id/search_src_text')
# el_search.click()
# sleep(1)
# el_search.send_keys('安全和隐私')

# 计算器案例
driver.start_activity("com.android.calculator2", ".Calculator")

el_plus = driver.find_element_by_id('com.android.calculator2:id/op_add')
el_2 = driver.find_element_by_id('com.android.calculator2:id/digit_2')
el_5 = driver.find_element_by_id('com.android.calculator2:id/digit_5')
el_equal = driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="等于"]')
el_cancel = driver.find_element_by_accessibility_id('清除')

el_2.click()
el_5.click()
el_plus.click()
el_5.click()
el_2.click()
el_equal.click()
sleep(3)
try:
    result = driver.find_element_by_id('com.android.calculator2:id/formula').text
    print(f'结果是{result}',type(result))
    assert result == '77'
    print('断言成功，测试用例通过')
except Exception:
    print('断言失败，断言失败测试用例不通过')
    raise
finally:
    el_cancel.click()

driver.quit()

el_plus = driver.find_element_by_id('com.android.calculator2:id/op_add')
el_plus.click
driver.find_element_by_id('com.android.calculator2:id/op_add').click()
