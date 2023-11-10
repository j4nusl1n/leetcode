# https://leetcode.com/problems/longest-palindrome
class Solution:
    def longestPalindrome(self, s: str) -> int:
        lower_n, upper_n = 0, 26
        char_cnt = [0] * 26 * 2
        lower_base, upper_base = ord("a"), ord("A")
        for c in s:
            n = ord(c)
            if n >= lower_base:
                n = lower_n + (n - lower_base)
            else:
                n = upper_n + (n - upper_base)

            char_cnt[n] += 1

        palindrome_len = 0
        has_odd = False
        for i in char_cnt:
            if not i:
                continue

            has_odd = (i % 2 == 1) or has_odd
            if i > 1:
                palindrome_len += i // 2 * 2

        if has_odd:
            palindrome_len += 1

        return palindrome_len
