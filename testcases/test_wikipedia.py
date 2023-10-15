import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

desired_caps = {
    'deviceName': '5200d42b8c7a863b',
    'platformName': 'Android',
    'automationName':'uiautomator2',
    'chromedriverExecutable':"C:\\Program Files\\Appium Server GUI\\resources\\app\\node_modules\\appium\\node_modules\\appium-chromedriver\\chromedriver\\chromedriver.exe",
    'browserName': 'Chrome'
}
capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
appium_server_url = "http://127.0.0.1:4723/wd/hub"
driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.get("http://wikipedia.org")
print(driver.title)
drop_down = Select(driver.find_element(By.CSS_SELECTOR, "#searchLanguage"))
drop_down.select_by_value("hi")
time.sleep(20)
