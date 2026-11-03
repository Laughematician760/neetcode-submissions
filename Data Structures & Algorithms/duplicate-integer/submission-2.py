from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        s = c.most_common()
        for i in range(len(s)):
            if s[i][1] > 1:
                return True
            else:
                continue
        return False
        