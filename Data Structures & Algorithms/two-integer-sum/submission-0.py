class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        o = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    o.append(i)
                    o.append(j)
        return o        