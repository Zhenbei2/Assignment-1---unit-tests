import unittest
import coverage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WebUITest(unittest.TestCase):
    def setUp(self):
        # 启动浏览器
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # 关闭浏览器
        self.driver.quit()

    def test_web_ui(self):
        # 导航到应用程序主页
        self.driver.get("http://localhost:5000")

        # 找到输入框并输入测试字符串
        input_element = self.driver.find_element(By.NAME, "input_string")
        input_element.send_keys("aabbcc")

        # 提交表单
        input_element.send_keys(Keys.ENTER)

        # 等待结果元素加载
        result_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )

        # 获取结果文本
        result = result_element.text

        # 断言结果是否符合预期
        self.assertEqual(result, "expected result")

if __name__ == '__main__':
    # 创建Coverage对象
    cov = coverage.Coverage()
    # 启动覆盖率监测
    cov.start()

    # 运行测试
    suite = unittest.TestLoader().loadTestsFromTestCase(WebUITest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # 停止覆盖率监测并生成报告
    cov.stop()
    cov.save()
    cov.report()
    cov.html_report(directory='htmlcov')

