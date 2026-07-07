class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        clean = list(set(nums))

        return len(clean) != len(nums)
        

        