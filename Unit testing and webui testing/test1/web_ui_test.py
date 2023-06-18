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

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def test_web_ui_1(self):
        self.driver.get("http://localhost:5000")
        
        self.wait_for_page_load()

        input_element = self.driver.find_element(By.CSS_SELECTOR, "input[name='input_string']")
        input_element.send_keys("aabbcc")

        input_element.submit()

        result_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))
        )

        result = result_element.text

        self.assertEqual(result, "expected result")

    def test_web_ui_2(self):
        self.driver.get("http://localhost:5000")
        
        self.wait_for_page_load()

        input_element = self.driver.find_element(By.CSS_SELECTOR, "input[name='input_string']")
        input_element.send_keys("xyz")

        input_element.submit()

        result_element = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, "result"))
        )

        result = result_element.text

        self.assertEqual(result, "expected result")

    def test_web_ui_3(self):
        self.driver.get("http://localhost:5000")
        
        self.wait_for_page_load()

        input_element = self.driver.find_element(By.CSS_SELECTOR, "input[name='input_string']")
        input_element.send_keys("12345")

        input_element.submit()

        result_element = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, "result"))
        )

        result = result_element.text

        self.assertEqual(result, "expected result")

if __name__ == '__main__':
    # 创建Coverage对象
    cov = coverage.Coverage()
    # 启动覆盖率监测
    cov.start()

    # 运行测试
    suite = unittest.TestLoader().loadTestsFromTestCase(WebUITest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # 停止覆盖率监测并生成报告
    cov.stop()
    cov.save()
    cov.report()
    cov.html_report(directory='htmlcov')
