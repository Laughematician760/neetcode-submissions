class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)
        n = len(nums)
        i = 0

        if sorted_list == list(range(n)):
            return n
        else:
            while sorted_list[i] == i:
                i += 1
        return i 



        