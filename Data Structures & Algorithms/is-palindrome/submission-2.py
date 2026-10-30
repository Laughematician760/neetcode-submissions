class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_no_space = ''.join(c for c in s if c.isalnum()).lower()
        while lower_no_space != "":
            if lower_no_space[0] == lower_no_space[-1]:
                lower_no_space = lower_no_space[1:-1]
            else:
                return False
        return True

        