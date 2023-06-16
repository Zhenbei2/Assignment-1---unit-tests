import unittest
from your_file import Solution

class TestSolution(unittest.TestCase):
    def test_partitionLabels_abac(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("abac"), [4])

    def test_partitionLabels_abacd(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("abacd"), [3, 2])

    def test_partitionLabels_abcde(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("abcde"), [1, 1, 1, 1, 1])

    def test_partitionLabels_aabbcc(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("aabbcc"), [2, 2, 2])

    def test_partitionLabels_aaaabbbbcccc(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("aaaabbbbcccc"), [4, 4, 4])

    def test_partitionLabels_abcdefg(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("abcdefg"), [1, 1, 1, 1, 1, 1, 1])

    def test_partitionLabels_abba(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("abba"), [2, 2])

    def test_partitionLabels_a(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("a"), [1])

if __name__ == '__main__':
    unittest.main()
