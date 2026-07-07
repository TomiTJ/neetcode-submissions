from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        arr = Counter(nums)
        common = arr.most_common(k)
        output = [num for num, count in common]
        return output


        