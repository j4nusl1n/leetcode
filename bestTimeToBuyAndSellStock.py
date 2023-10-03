from typing import List
import json


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        l, r = 0, 1
        while r < len(prices):
            pl, pr = prices[l], prices[r]
            if (pr - pl) < 0:
                l = r
                r += 1
            else:
                if (pr - pl) > ret:
                    ret = pr - pl
                r += 1
        return ret


if __name__ == "__main__":
    tc = []
    with open("q121_testcase.txt", "r") as f:
        for line in f:
            tc.append(eval(line))

    obj = Solution()
    for t in tc:
        print(obj.maxProfit(t))
