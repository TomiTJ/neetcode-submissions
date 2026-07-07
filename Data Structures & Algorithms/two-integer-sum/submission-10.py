class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        # nums[i] + nums[j] = target , nums[j] = target - nums[i]
        for i,val in enumerate(nums):
            complement = target - val
            if complement in seen:
                return [seen[complement],i]
            seen[val] = i  

            