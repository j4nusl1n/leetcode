from typing import List

# LC: https://leetcode.com/problems/two-sum/description/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remains = {}
        for i in range(len(nums)):
            val = nums[i]
            if val in remains:
                return [i, remains[val]]
            remains[target - val] = i
        return [None, None]


if __name__ == "__main__":
    obj = Solution()
    nums = [-1, -2, -3, -4, -5]
    target = -8
    print(obj.twoSum(nums, target))
