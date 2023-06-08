from typing import List
import unittest
import HtmlTestRunner
import coverage

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []

        count = {}
        res = []
        i, length = 0, len(S)
        for j in range(length):
            c = S[j]
            count[c] = j

        curLen = 0
        goal = 0
        while i < length:
            c = S[i]
            goal = max(goal, count[c])
            curLen += 1

            if goal == i:
                res.append(curLen)
                curLen = 0
            i += 1
        return res

class TestSolution(unittest.TestCase):
    def test_empty_string(self):
        s = Solution()
        self.assertEqual(s.partitionLabels(""), [])

    def test_no_repeating_chars(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("abcdefg"), [7])

    def test_repeating_chars(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("ababcbacadefegdehijhklij"), [9, 7, 8])

    def test_all_chars(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("abcdefghijklmnopqrstuvwxyz"), [1]*26)

    def test_chars_in_order(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("abcdeghijklmnopqrstuvwxyzf"), [25, 1])

    def test_chars_not_in_order(self):
        s = Solution()
        self.assertEqual(s.partitionLabels("abcdefghijklmnopqrstuvwxyzgfedcba"), [26])


if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_report'))
    cov.stop()
    cov.save()
    cov.html_report(directory='coverage_report')
