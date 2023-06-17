from selenium import webdriver

# 创建 Chrome WebDriver 对象
driver = webdriver.Chrome()

# 打印 Chrome 浏览器和 ChromeDriver 的版本号
print("Chrome 浏览器版本：", driver.capabilities['browserVersion'])
print("ChromeDriver 版本：", driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0])
