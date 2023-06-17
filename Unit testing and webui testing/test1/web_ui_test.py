from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 启动浏览器
driver = webdriver.Chrome()

try:
    # 导航到应用程序主页
    driver.get("http://localhost:5000")

    # 找到输入框并输入测试字符串
    input_element = driver.find_element(By.NAME, "input_string")
    input_element.send_keys("aabbcc")

    # 提交表单
    input_element.send_keys(Keys.ENTER)

    # 等待结果元素加载
    result_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "result"))
    )

    # 获取结果文本
    result = result_element.text

    # 断言结果是否符合预期
    assert result == "expected result"

finally:
    # 关闭浏览器
    driver.quit()
