class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted(list(set(s)))
        t_list = sorted(list(set(t)))
        if set(s) != set(t) or len(s) != len(t):
            return False
        else:
            for i in range(len(s_list)):
                if s.count(s_list[i]) == t.count(t_list[i]):
                    continue
                else:
                    return False
        return True
        