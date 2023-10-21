import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
# Hii
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
driver.get("http://google.com")
print(driver.title)
driver.find_element(By.XPATH, "//*[@name='q']").send_keys("Hellow appium....")
time.sleep(20)
