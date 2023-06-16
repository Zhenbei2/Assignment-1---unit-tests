from selenium import webdriver

# 创建一个浏览器实例
driver = webdriver.Chrome()

# 打开应用程序的首页
driver.get('http://localhost:5000')

# 找到输入框并输入测试字符串
input_element = driver.find_element_by_name('input_string')
input_element.send_keys('aabbcc')

# 找到提交按钮并点击
submit_button = driver.find_element_by_name('submit')
submit_button.click()

# 找到结果元素并获取文本
result_element = driver.find_element_by_id('result')
result = result_element.text

# 验证处理结果是否正确
assert result == '4'

# 关闭浏览器
driver.quit()
