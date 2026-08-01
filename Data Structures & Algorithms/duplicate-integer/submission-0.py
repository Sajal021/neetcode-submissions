class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set69 = set(nums)
        if len(set69) == len(nums):
            return False
        else:
            return True
