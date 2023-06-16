from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import Chrome

# 启动浏览器
driver = webdriver.Chrome()

# 导航到应用程序主页
driver.get("http://localhost:5000")

# 找到输入框并输入测试字符串
input_element = driver.find_element_by_name("input_string")
input_element.send_keys("test string")

# 提交表单
input_element.send_keys(Keys.ENTER)

# 等待结果页面加载
time.sleep(2)

# 找到结果元素并获取结果
result_element = driver.find_element_by_id("result")
result = result_element.text

# 断言结果是否符合预期
assert result == "expected result"

# 关闭浏览器
driver.quit()
