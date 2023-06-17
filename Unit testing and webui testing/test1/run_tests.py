import unittest
import coverage
from your_file import Solution
from test_your_file import TestSolution

if __name__ == '__main__':
    # 创建Coverage对象
    cov = coverage.Coverage()
    # 启动覆盖率监测
    cov.start()

    # 运行测试
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # 停止覆盖率监测并生成报告
    cov.stop()
    cov.save()
    cov.report()
    cov.html_report(directory='htmlcov')
