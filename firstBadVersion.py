# https://leetcode.com/problems/first-bad-version
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.binarySearch(1, n)

    def binarySearch(self, left, right):
        n = (right - left) // 2
        if n == 0:
            return left if isBadVersion(left) else right
        elif isBadVersion(left + n):
            return self.binarySearch(left, right - n)
        else:
            return self.binarySearch(left + n, right)
