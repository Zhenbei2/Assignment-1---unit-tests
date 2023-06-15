import unittest
from your_file import Solution

class TestSolution(unittest.TestCase):
    def test_partitionLabels(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("abac"), [4])
        self.assertEqual(s.partitionLabels("abacd"), [3, 2])
        self.assertEqual(s.partitionLabels("abcde"), [1, 1, 1, 1, 1])
        # 添加更多的测试用例

if __name__ == '__main__':
    unittest.main()
