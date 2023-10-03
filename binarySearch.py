from typing import List
from utils import get_tc_by_fname


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            i = (r - l + 1) // 2
            if nums[l + i] == target:
                return l + i
            elif nums[l + i] > target:
                r -= i
            else:
                l += i

        if nums[r] == target:
            return r
        else:
            return -1


if __name__ == "__main__":
    obj = Solution()
    for t in get_tc_by_fname("q704_testcase.txt"):
        nums, target = t.split(" ")
        nums, target = eval(nums), eval(target)
        print(obj.search(nums, target))
