# https://leetcode.com/problems/valid-anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_cnt = {}
        for c in s:
            if c not in word_cnt:
                word_cnt[c] = 0
            word_cnt[c] += 1
        
        for c in t:
            if c not in word_cnt:
                return False
            elif word_cnt[c] <= 0:
                return False
            else:
                word_cnt[c] -= 1
        
        for v in word_cnt.values():
            if v != 0:
                return False
        return True
